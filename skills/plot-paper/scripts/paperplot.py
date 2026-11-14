"""paperplot: one reusable matplotlib style for paper figures (plot-paper skill, v1.2).

Copy this file into a project (or import it from the skill path), choose the venue's page widths and
register the paper's methods once. What it enforces:
- every figure is drawn at its printed width (one column or the full text width) and is included in
  LaTeX at its natural size, so type keeps its size and no figure is rescaled;
- constrained layout at that fixed size; save() fails when any text leaves the canvas, when tick
  labels collide, or when a data curve lies mostly outside its axes or leaves and re-enters them;
- sans-serif type at print size; one colour and line style per method; ours highlighted, baselines
  muted and grouped in families; low-opacity confidence bands; continuous curves; crossing marks
  interpolated on the drawn line; legends laid out row by row, one family per row.

Typical use:

    import paperplot as P
    P.page("aistats")                                   # P.COL = 3.25 in, P.TEXT = 6.75 in
    P.register({"ours": ("Ours", P.OURS_COLOUR, "-"),
                "zo_a": ("ZO-A", P.FAMILY_BLUE[0], "-"), "zo_b": ("ZO-B", P.FAMILY_BLUE[1], "-"),
                "sgd": ("SGD", P.ONE_OFF, P.DASHDOT)})
    fig, axes = P.figure(P.COL, 3.0, nrows=2, ncols=2)  # a one-column 2 x 2 grid
    P.curve(axes[0], N, mean, lo, hi, "ours")
    x = P.crossing(N, mean, target); P.mark(axes[0], x, target, "ours"); P.target(axes[0], target)
    P.logx(axes[0], "Scenarios $N$", 10, 5000); axes[0].set_ylabel(r"$F(x_t)$"); axes[0].set_title("Pricing")
    P.legend(fig, [("ours", "sgd"), ("zo_a", "zo_b")])
    P.save(fig, out_dir, "fig_comparison")            # runs the layout and curve checks
    P.tile(sorted(out_dir.glob("*.png")), out_dir / "_check.png")   # look at it; then compile a preview
"""
from __future__ import annotations

import math
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np

# Printed widths in inches: (one column, full text width). Check the venue's style file.
PAGES = {"aistats": (3.25, 6.75), "icml": (3.25, 6.75), "neurips": (5.5, 5.5), "iclr": (5.5, 5.5)}
COL, TEXT = PAGES["aistats"]

FONT = ["Helvetica", "Arial", "DejaVu Sans"]
FS_LABEL, FS_TICK, FS_LEGEND, FS_TITLE, FS_NOTE = 8.0, 7.0, 7.0, 8.0, 6.5
LW, BAND = 1.1, 0.15
INK, INK2, GRID, REF = "#222222", "#555555", "#e8e8e8", "#8a8a8a"
DASH, DASHDOT, DOT = (0, (4, 1.6)), (0, (5, 1.5, 1.2, 1.5)), (0, (1.2, 1.4))

# Ours is the one saturated colour; baselines come in families (one hue, one line style, shades within).
# Checked with the dataviz validator: ours vs every colour below has protan/deutan Delta E >= 10; the
# closest cross-family pair (ONE_OFF vs FAMILY_GREEN[0], 7.6) must differ in line style.
OURS_COLOUR = "#D55E00"                                   # vermillion
FAMILY_BLUE = ["#0072B2", "#56B4E9", "#1B3F8B"]           # solid
FAMILY_GREEN = ["#009E73", "#5CC8A8", "#00674B"]          # dashed
ONE_OFF = "#CC79A7"                                       # dash-dot
CONTROLS = ["#737373", "#ABABAB"]                         # grey: solid, dashed, dotted
OURS_RAMP = ["#F2A365", OURS_COLOUR, "#953A05", "#4A1C02"]  # ordinal factor of ours; grey #8C8C8C = "off"
OUTCOME = {"low": "#2C7FB8", "middle": "#7FCDBB", "high": "#EDF8B1", "none": "#FFFFFF"}  # like the contour fill

METHODS: Dict[str, Tuple[str, str, object]] = {}


def page(venue: str) -> Tuple[float, float]:
    """Set COL and TEXT for a venue in PAGES."""
    global COL, TEXT
    COL, TEXT = PAGES[venue]
    return COL, TEXT


def register(methods: Dict[str, Tuple[str, str, object]]) -> None:
    """key -> (label, colour, line style); call once per paper. A colour must not name two methods."""
    colours = {}
    for k, (lab, col, ls) in methods.items():
        if (col, str(ls)) in colours and colours[(col, str(ls))] != k:
            raise ValueError(f"{k} and {colours[(col, str(ls))]} share colour and line style")
        colours[(col, str(ls))] = k
    METHODS.update(methods)


def setup():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        "font.family": "sans-serif", "font.sans-serif": FONT, "mathtext.fontset": "custom",
        "mathtext.rm": FONT[0], "mathtext.it": f"{FONT[0]}:italic", "mathtext.bf": f"{FONT[0]}:bold",
        "mathtext.sf": FONT[0], "font.size": FS_LABEL, "axes.titlesize": FS_TITLE, "axes.labelsize": FS_LABEL,
        "legend.fontsize": FS_LEGEND, "xtick.labelsize": FS_TICK, "ytick.labelsize": FS_TICK,
        "axes.linewidth": 0.6, "axes.edgecolor": "#8a8a8a", "axes.labelcolor": INK, "xtick.color": INK2,
        "ytick.color": INK2, "xtick.major.size": 2.5, "ytick.major.size": 2.5, "xtick.minor.size": 1.5,
        "ytick.minor.size": 1.5, "xtick.major.pad": 1.8, "ytick.major.pad": 1.8, "axes.labelpad": 1.5,
        "axes.titlepad": 2.5, "axes.titlelocation": "left", "axes.spines.top": False,
        "axes.spines.right": False, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.5,
        "lines.linewidth": LW, "legend.frameon": False, "legend.handlelength": 1.8, "legend.handletextpad": 0.4,
        "legend.labelspacing": 0.25, "legend.columnspacing": 0.9, "legend.borderaxespad": 0.1,
        "legend.borderpad": 0.1, "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.dpi": 300,
        "figure.facecolor": "white", "axes.facecolor": "white"})
    return plt


def figure(width: float, height: float, nrows: int = 1, ncols: int = 1, sharex: bool = False,
           sharey: bool = False, wspace: float = 0.03, hspace: float = 0.04, **subplot_kw):
    """A figure of exactly width x height inches (width = COL or TEXT, or a fraction of COL for panels
    placed side by side in LaTeX), with axes placed by constrained layout."""
    plt = setup()
    fig = plt.figure(figsize=(width, height), layout="constrained")
    fig.get_layout_engine().set(w_pad=1.5 / 72, h_pad=1.5 / 72, wspace=wspace, hspace=hspace)
    axes = fig.subplots(nrows, ncols, sharex=sharex, sharey=sharey, squeeze=False, subplot_kw=subplot_kw)
    return fig, axes.ravel().tolist()


def share_y(*axes) -> None:
    """One y range for a row of panels; tick labels only on the first."""
    lo = min(a.get_ylim()[0] for a in axes)
    hi = max(a.get_ylim()[1] for a in axes)
    for a in axes:
        a.set_ylim(lo, hi)
    for a in axes[1:]:
        a.tick_params(labelleft=False)
        a.set_ylabel("")


def curve(ax, x, mid, lo=None, hi=None, key: str = "ours", label: Optional[str] = None, z: Optional[int] = None):
    lab, colour, ls = METHODS[key]
    z = (6 if key == "ours" else 3) if z is None else z
    x = np.asarray(x, float)
    mid = np.asarray(mid, float)
    if x.ndim != 1 or mid.ndim != 1 or x.shape != mid.shape or not x.size:
        raise ValueError(f"{key}: x and curve must be nonempty 1-D arrays of equal length")
    if np.any(~np.isfinite(x)) or np.any(~np.isfinite(mid)):
        raise ValueError(f"{key}: nonfinite data would make the line discontinuous")
    if (lo is None) != (hi is None):
        raise ValueError(f"{key}: supply both confidence bounds or neither")
    if lo is not None:
        lo, hi = np.asarray(lo, float), np.asarray(hi, float)
        if lo.shape != mid.shape or hi.shape != mid.shape:
            raise ValueError(f"{key}: confidence bounds must match the curve")
        if np.any(~np.isfinite(lo)) or np.any(~np.isfinite(hi)) or np.any(lo > hi):
            raise ValueError(f"{key}: confidence bounds must be finite and ordered")
    if lo is not None and BAND:
        ax.fill_between(x, lo, hi, color=colour, alpha=BAND, linewidth=0, zorder=z - 1)
    line = ax.plot(x, mid, color=colour, linestyle=ls, linewidth=LW, zorder=z, label=label or lab)[0]
    line.set_gid("data")  # check_lines inspects these
    return line


def grouped_bars(ax, categories: Sequence[str], values: Dict[str, Sequence[float]],
                 hatches: Optional[Dict[str, str]] = None, group_width: float = 0.78):
    """Small categorical comparison using registered method colours and a zero baseline."""
    categories = list(categories)
    if not categories or not values:
        raise ValueError("grouped bars need categories and method values")
    if not 0 < group_width < 1:
        raise ValueError("group_width must lie between 0 and 1")
    x = np.arange(len(categories), dtype=float)
    width = group_width / len(values)
    bars = {}
    for j, (key, series) in enumerate(values.items()):
        if key not in METHODS:
            raise ValueError(f"unregistered method: {key}")
        y = np.asarray(series, float)
        if y.ndim != 1 or y.size != len(categories) or np.any(~np.isfinite(y)):
            raise ValueError(f"{key}: one finite value is required per category")
        label, colour, _ = METHODS[key]
        position = x - group_width / 2 + (j + 0.5) * width
        bars[key] = ax.bar(position, y, width, label=label, color=colour,
                           edgecolor=INK2, linewidth=0.45, hatch=(hatches or {}).get(key, ""))
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_xlim(-0.5, len(categories) - 0.5)
    low, high = ax.get_ylim()
    if low > 0:
        ax.set_ylim(bottom=0)
    if high < 0:
        ax.set_ylim(top=0)
    ax.set_axisbelow(True)
    ax.xaxis.grid(False)
    return bars


def crossing(x, y, level: float, logx: bool = True, logy: bool = False) -> Optional[float]:
    """First x where the drawn polyline reaches level (from above), interpolated in the axes' scale."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    if y[0] <= level:
        return float(x[0])
    fx = np.log if logx else (lambda v: v)
    fy = np.log if logy else (lambda v: v)
    for i in range(1, len(y)):
        if y[i] <= level < y[i - 1]:
            t = (fy(y[i - 1]) - fy(level)) / (fy(y[i - 1]) - fy(y[i]))
            u = fx(x[i - 1]) + t * (fx(x[i]) - fx(x[i - 1]))
            return float(np.exp(u) if logx else u)
    return None


def mark(ax, x: Optional[float], level: float, key: str) -> None:
    if x is not None:
        ax.plot([x], [level], "o", markersize=3.6, color=METHODS[key][1], markeredgecolor="white",
                markeredgewidth=0.6, zorder=8)


def target(ax, level: float) -> None:
    ax.axhline(level, color=REF, linewidth=0.7, linestyle=(0, (1.5, 1.5)), zorder=1)


def level_line(ax, level: float) -> None:
    ax.axhline(level, color=REF, linewidth=0.7, linestyle=(0, (4, 2)), zorder=1)


def plain_log_ticks(axis) -> None:
    from matplotlib.ticker import FuncFormatter, NullFormatter
    axis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}" if v >= 1 else f"{v:g}"))
    axis.set_minor_formatter(NullFormatter())


def decades(lo: float, hi: float) -> List[float]:
    return [10.0 ** k for k in range(math.floor(math.log10(lo) + 1e-9), math.floor(math.log10(hi) + 1e-9) + 1)
            if lo * (1 - 1e-9) <= 10.0 ** k <= hi * (1 + 1e-9)]


def logx(ax, label: Optional[str], lo: float, hi: float, ticks: Optional[Sequence[float]] = None) -> None:
    """Log x axis labelled at every decade in range with plain numbers."""
    from matplotlib.ticker import FixedLocator, LogLocator
    ax.set_xscale("log")
    ax.set_xlim(lo, hi)
    ax.xaxis.set_major_locator(FixedLocator(list(ticks) if ticks else decades(lo, hi)))
    ax.xaxis.set_minor_locator(LogLocator(base=10, subs=np.arange(2, 10), numticks=50))
    plain_log_ticks(ax.xaxis)
    if label:
        ax.set_xlabel(label)


def logy(ax, ticks: Sequence[float], lo: float, hi: float) -> None:
    from matplotlib.ticker import FixedLocator
    ax.set_yscale("log")
    ax.set_ylim(lo, hi)
    ax.yaxis.set_major_locator(FixedLocator(list(ticks)))
    plain_log_ticks(ax.yaxis)


def legend(fig, rows: Sequence[Sequence], labels: Optional[dict] = None, loc: str = "outside lower center", **kw):
    """Legend read row by row: rows is a list of rows of method keys or (handle, label) pairs, for example
    [("ours", "sgd"), family_a, family_b]; short rows are padded so each family keeps its row."""
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    ncol = max(len(r) for r in rows)
    grid = []
    for r in rows:
        cells = []
        for k in r:
            if isinstance(k, tuple):
                cells.append(k)
            else:
                lab, colour, ls = METHODS[k]
                cells.append((Line2D([], [], color=colour, linestyle=ls, linewidth=LW), (labels or {}).get(k, lab)))
        cells += [(Patch(visible=False), "")] * (ncol - len(cells))
        grid.append(cells)
    order = [grid[r][c] for c in range(ncol) for r in range(len(grid))]  # matplotlib fills columns first
    return fig.legend([h for h, _ in order], [s for _, s in order], loc=loc, ncol=ncol, **kw)


def halo(artist, width: float = 2.2) -> None:
    """White outline keeping a path readable over a coloured fill (avoid on dashed lines over other lines)."""
    import matplotlib.patheffects as pe
    artist.set_path_effects([pe.Stroke(linewidth=width + LW, foreground="white", alpha=0.9), pe.Normal()])


def note(ax, text: str, xy, offset=(0, 0), ha: str = "center", va: str = "center"):
    """Small haloed label beside a landmark."""
    import matplotlib.patheffects as pe
    t = ax.annotate(text, xy, xytext=offset, textcoords="offset points", fontsize=FS_NOTE, color=INK, ha=ha,
                    va=va, zorder=10)
    t.set_path_effects([pe.withStroke(linewidth=1.8, foreground="white", alpha=0.85)])
    return t


def landmark(ax, xy, marker: str = "*", size: float = 7.5) -> None:
    """Hollow landmark marker above the data, so it never hides an end point drawn at the same place."""
    ax.plot(*xy, marker, markersize=size, markerfacecolor="none", markeredgecolor=INK, markeredgewidth=0.9,
            zorder=9, linestyle="none")


def contour_background(ax, X, Y, Z, levels: Sequence[float], fill_levels: Optional[Sequence[float]] = None):
    """Light blue-green-yellow fill (valleys blue, hills yellow), every band filled including the lowest,
    with dense thin grey level lines; choose levels so each local minimum has closed rings."""
    from matplotlib.colors import LinearSegmentedColormap
    import matplotlib.pyplot as plt
    base = plt.get_cmap("YlGnBu")
    cmap = LinearSegmentedColormap.from_list("landscape", [base(v) for v in np.linspace(0.62, 0.02, 64)])
    top, bottom = float(np.max(Z)), float(np.min(Z))
    fl = [bottom] + [v for v in (fill_levels if fill_levels is not None else levels) if bottom < v < top] + [top]
    ax.contourf(X, Y, Z, levels=fl, cmap=cmap, alpha=0.55, zorder=0)
    ax.contour(X, Y, Z, levels=[v for v in levels if v < top], colors="#6f6f6f", linewidths=0.3, alpha=0.75, zorder=1)


# ---------------------------------------------------------------- checks run by save()

def check_inside(fig) -> None:
    """Everything drawn lies inside the canvas and no axis has colliding tick labels."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    W, H = fig.bbox.width, fig.bbox.height
    bad = []
    parts = [(f"axes {i} ({a.get_title(loc='left') or a.get_xlabel()})", a.get_tightbbox(r)) for i, a in enumerate(fig.axes)]
    parts += [("legend", leg.get_window_extent(r)) for leg in fig.legends]
    parts += [(repr(t.get_text()), t.get_window_extent(r)) for t in fig.texts if t.get_visible() and t.get_text()]
    for name, b in parts:
        if b is not None and (b.x0 < -1 or b.y0 < -1 or b.x1 > W + 1 or b.y1 > H + 1):
            bad.append(f"{name} leaves the canvas")
    for i, a in enumerate(fig.axes):
        for axis, lim, k in ((a.xaxis, a.get_xlim(), 0), (a.yaxis, a.get_ylim(), 1)):
            lo, hi = sorted(lim)
            boxes = sorted((t.get_window_extent(r) for t in axis.get_majorticklabels()
                            if t.get_visible() and t.get_text() and lo - 1e-12 <= t.get_position()[k] <= hi + 1e-12),
                           key=lambda b: b.x0 if k == 0 else b.y0)
            if any((b2.x0 < b1.x1 - 0.5) if k == 0 else (b2.y0 < b1.y1 - 0.5) for b1, b2 in zip(boxes, boxes[1:])):
                bad.append(f"axes {i}: overlapping tick labels")
    if bad:
        raise ValueError(f"layout check failed ({W / fig.dpi:.2f} x {H / fig.dpi:.2f} in): {'; '.join(bad[:8])}")


def check_lines(ax, min_inside: float = 0.85) -> None:
    """Every data curve shows its trend: most points inside the view, and never leaving and re-entering."""
    (x0, x1), (y0, y1) = sorted(ax.get_xlim()), sorted(ax.get_ylim())
    for line in ax.get_lines():
        if line.get_gid() != "data":
            continue
        x, y = (np.asarray(v, float) for v in line.get_data())
        keep = (x >= x0 * (1 - 1e-9)) & (x <= x1 * (1 + 1e-9))
        y = y[keep]
        if y.size == 0:
            raise ValueError(f"{line.get_label()}: no point inside the x range")
        tol = 1e-9 * max(abs(y0), abs(y1), 1.0)
        inside = (y >= y0 - tol) & (y <= y1 + tol)
        if inside.mean() < min_inside:
            raise ValueError(f"{line.get_label()}: only {inside.mean():.0%} of the curve is inside the axes; "
                             "widen the axis, use a log scale, or leave the method out")
        idx = np.flatnonzero(inside)
        if idx.size and not np.all(inside[idx[0]:idx[-1] + 1]):
            raise ValueError(f"{line.get_label()}: the curve leaves the axes and comes back")


def save(fig, out: Path, name: str, lines: bool = True) -> List[Path]:
    """PDF and PNG at the fixed size (no tight bounding box), after the layout and curve checks."""
    check_inside(fig)
    if lines:
        for ax in fig.axes:
            check_lines(ax)
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    paths = [out / f"{name}.{ext}" for ext in ("pdf", "png")]
    for p in paths:
        fig.savefig(p)
    import matplotlib.pyplot as plt
    plt.close(fig)
    return paths


def label_number(n: Optional[float]) -> str:
    return "—" if n is None or not math.isfinite(n) else f"{int(round(n)):,}"


def tortuosity(path) -> float:
    """Path length over net displacement (1 = straight); for choosing a single-run panel by a stated rule."""
    path = np.asarray(path, float)
    return float(np.linalg.norm(np.diff(path, axis=0), axis=1).sum() / max(np.linalg.norm(path[-1] - path[0]), 1e-12))


def tile(pngs: Sequence[Path], out: Path, ncols: int = 3, grayscale: bool = False) -> Path:
    """One colour or grayscale contact sheet for checking figures at a glance."""
    from PIL import Image
    mode = "L" if grayscale else "RGB"
    ims = []
    for path in pngs:
        with Image.open(path) as im:
            ims.append(im.convert(mode))
    rows = [ims[i:i + ncols] for i in range(0, len(ims), ncols)]
    W = max(sum(i.size[0] for i in r) for r in rows)
    H = sum(max(i.size[1] for i in r) for r in rows)
    canvas = Image.new(mode, (W, H), 255 if grayscale else "white")
    y = 0
    for r in rows:
        x = 0
        for i in r:
            canvas.paste(i, (x, y))
            x += i.size[0]
        y += max(i.size[1] for i in r)
    canvas.save(out)
    return Path(out)
