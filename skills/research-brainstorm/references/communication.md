# Explain research ideas in language the reader can follow

## Reuse the existing language baseline

Use the general prose principles from [writing-research](../../writing-research/references/composition-and-revision.md), especially "Draft for understanding": clear subjects and actions, connected paragraphs, stable terminology and claims matched to evidence. Reuse [explain-project's reader perspective](../../explain-project/references/report.md#用具体过程解释) and the local diagnosis in [review-manuscript](../../review-manuscript/references/language-audit.md#local-diagnosis) for buried actions, empty contrasts and claims of importance without an explanation. This file makes the brainstorming application self-contained; missing sibling skills do not block the task. Do not load paper-review, submission, bibliography or LaTeX workflows for an ordinary conversation.

## Make the idea understandable before judging it

- Match the language the user is using, normally Chinese here. A mathematically experienced reader may be new to this field. Use their demonstrated familiarity; neither unexplained jargon nor an unnecessary beginner lecture helps.
- Lead with the answer, question or current understanding that matters. Establish what is being studied, what can be observed or changed, what is unknown and why resolving it matters. Use one small example when the setting is unfamiliar; do not invent an application, resource constraint or objective and make it the user's problem.
- Explain the proposed process: what happens first, what information it supplies, how that changes the next action, and why this might help. State the main obstacle in the same setting. An impressive name is not an explanation.
- Give each paragraph a connected step in the reasoning. Prefer subjects and verbs over chains of abstract nouns. Avoid abrupt fragments, comma-heavy clause chains and unnecessary embedded qualifiers. Use semicolons when they help; do not mechanically split every sentence or vary words for the same object.
- Keep necessary technical terms and define them where they first matter. An English translation is not a definition. Preserve formulas, assumptions, mathematical scope and uncertainty; clarity is not achieved by deleting technical substance.
- For an important formula, introduce the objects, explain what the relation predicts or controls, and connect it to the example. Say which step is known and which implication remains to be established.
- Make comparisons concrete: what does the existing method do, under what conditions and budget, what changes here, and which outcome would show that the change matters? Explain the missing work instead of calling an idea "long-term" or "high-potential."
- Read the response once at a natural pace. Can the user restate the question, proposed explanation/actions, obstacle, comparison and next check? Repair missing connections. Do not attach an unsolicited quiz or describe this self-check to the user.

## Use structure to support the discussion

Candidate cards, search-status codes and evaluation dimensions are private completeness checks, not obligatory output labels. Explain a few ideas well rather than returning a wall of near-identical mini-forms. A compact comparison table helps after the ideas are understandable.

Translate workflow labels into actual statements. Say "这篇论文只核对了摘要，还不能判断它是否覆盖我们的定理" rather than displaying ABSTRACT_ONLY or an unexplained confidence grade. Keep source locations and qualifications close to the claims they support.

Avoid self-announcing prose, inflated significance, invented compound labels, reflexive "不是……而是……", and automatic closing summaries when they add no information. Preserve a contrast when both sides specify a real mathematical or scientific distinction. These are reader checks, not a banned-word list, punctuation quota or AI-authorship detector.

Do not force casual speech, anecdotes, deliberate imperfections, a dramatic research story or a polished proposal onto open brainstorming. A mechanism may still be incomplete. Say exactly what remains unclear; never supply a smooth causal bridge that the evidence does not establish.

## Examples

These are constructed communication examples, not established findings, recommended research models or novelty claims.

- Instead of "识别机制缺口并构建证据闭环", explain the actual uncertainty: "现有分析把这个结构看成不变，但你观察到它在训练中会变化。可以先问：这种变化会不会影响原来的结论？第一步需要核对原文到底固定了什么，以及实验中的变化是否属于同一个量。" An observation outside a theorem's assumptions does not refute that theorem.
- Instead of "nearest-work delta", write "已有论文能在……条件下得到……；这里希望进一步解释/证明……。目前还没核对……，所以差别是否成立仍要查证。"
- "反馈接口与权限" becomes "每次真实实验后，我们能看到什么？只有一个带噪声的梯度，还是也记录了当时的状态和外部扰动？只有确实记录了某个扰动，才可能把它输入模拟器。" This concerns observations and operations, not user approval or access control.
- "增量精度" becomes "我们想预测参数从 x 改成 x+h 时，平均梯度会改变多少。例如真实变化只有 0.01，但两次测量各自都有约 1 的随机波动，直接相减就很难看出变化。还需要说明怎样利用持续到来的反馈学到这种关系。" The numbers illustrate the explanation; a theorem still needs a noise model.
- "按真实物理时间结算校准收益" becomes "如果实验需要等待，就把等待也算进去，再比较谁更快达到同一个目标。" Introduce waiting costs only when the application has them; do not replace a query-count objective.
- "尾部抵消" becomes "两种测量可能被同一次冲击同时推高。如果能记录并模拟这次冲击，相减可能减弱它的影响；若两次冲击独立，就不能指望这样相减能去掉它。" Explain the actual dependence before writing a control-variate equation; do not assume all heavy-tailed noise has an observed common cause.
- Instead of "该方向具备高创新性和可行性", write a conditional judgment: "这个问题值得继续看，因为它可能解释现有结论不一致的原因。但目前还不能判断是否新；应先核对最接近的两篇工作，并确认差异不是实验设置造成的。"

## Communication provenance

The existing examples and explanation requirements were retained from the previous version, including guidance adapted from explain-paper's "Default explanation" and "Understand the argument"; explain-project's "使用人话"; and writing-research's "Draft for understanding". Review-manuscript adds meaning-preserving diagnosis, not a mandatory manuscript audit.

Previously recorded supporting sources are [CDC, Writing for a Scientific Audience](https://www.cdc.gov/nceh/clearwriting/writing-tips/2024/writing-tip-wed-06-05-2024.html), points 1–3; [CDC Clear Communication Index](https://www.cdc.gov/ccindex/widget.html), Part A item 7; [IES, Organizing Instruction and Study](https://ies.ed.gov/ncee/WWC/Docs/PracticeGuide/20072004.pdf), Recommendation 4 pp. 15–16 and Recommendation 7 pp. 29–31; and [AERO, Explicit Instruction](https://www.edresearch.edu.au/guides-resources/practice-guides/explicit-instruction-practice-guide-full-publication), key practices 1–2. They motivate definitions, examples and connecting concrete situations to abstractions; they do not validate this particular research workflow.
