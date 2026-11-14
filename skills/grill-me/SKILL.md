---
name: grill-me
description: Stress-test a plan, research idea, design, or decision through a focused interview. Use only when the user explicitly invokes grill-me or asks to be grilled; ask compact batches of independent high-value questions and provide a recommended answer for each.
---

# Grill Me

Interview the user until the material decisions, assumptions, tradeoffs, risks, and open questions are explicit.

## Rules

- Ask a compact batch of typically 3-5 high-value questions per round when they can be answered independently. Use fewer when only one or two questions are currently useful.
- Do not put dependent questions in the same round. Hold a question until the answers it depends on are settled, then recompute the next batch.
- Number the questions. With every question, give a recommended answer and a short reason so the user can reply by number and accept, reject, or revise it.
- If a factual question can be answered from available files or tools, investigate it instead of asking the user.
- Push back on vague, inconsistent, or evasive answers. Name the consequence that makes clarification necessary.
- Track settled decisions, assumptions, risks, unresolved questions, and out-of-scope branches in the conversation.
- After each response, update that state and ask the next independent batch rather than repeating settled questions.
- Stop when the material branches are resolved, the user asks to stop, or another round would add little value.

End with a compact summary of decisions, remaining uncertainties, and the next useful action. Do not execute the plan or write files unless the user separately asks.
