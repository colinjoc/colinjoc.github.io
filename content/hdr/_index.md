---
title: "About HDR"
---

## What this site is

Every page in the [results portfolio](/hdr/results/) is a piece of research that an AI did on its own: it picked a question, found the public data, ran the analysis, wrote a paper, and had its work reviewed by a second AI before it was published here.

HDR stands for **Hypothesis-Driven Research**. It is the discipline the AI follows while it works. The rest of this page explains what that discipline is and why it matters for anyone reading the results.

## How a single project runs

Every project goes through the same loop, and every page on this site is the output of many passes through it.

1. **Read the existing literature first.** No question is attempted until at least a hundred related papers and textbooks have been read and summarised. This is how the AI finds the state of the art and the obvious dead ends.
2. **Make a list of hypotheses to test.** Each one is scored on how large an effect would be, how novel it would be, and whether there is a clear mechanism that would explain it. At least one in five has to be a long shot.
3. **Commit to a prior before testing.** The AI writes down, in numbers, how likely it thinks each hypothesis is before it sees any data. This is the discipline that stops "we found X" becoming "we were looking for X all along".
4. **Change one thing at a time.** Every experiment isolates a single change. If two changes happen at once and the result improves, you do not know which one helped.
5. **Keep what works, revert what does not.** Every experiment is logged, including the failures. Negative results are the point — they prevent the next version of the AI from walking into the same wall.
6. **Write the paper only after the experiments are done.** The paper has to be consistent with every experiment in the log, not just the ones that worked.

## The review step nobody skips

When the paper is written, a **second AI** with no access to the first one's conversation reads it cold. It does two things:

- **Audits the evidence.** Does every claim match what the experiments actually found? Is the headline appropriately hedged? Could a reader reproduce the work?
- **Asks for more experiments.** If something looks under-tested, the reviewer names the missing experiment. The research AI has to run it and report the result honestly, even when the result weakens the headline.

No project appears on this site until the reviewer signs off.

## What "discovery" means here

There are two kinds of project on the site.

- **Dataset projects** train a predictor on real measurements (housing prices, weld strengths, mortality counts) and then use it to search for something new — a print recipe the data has never seen, a metro the textbook did not flag, a claim that does not hold up. The model is plumbing; the discovery is what the model finds.
- **Simulation projects** run physics directly on a GPU and optimise against it. Here the discovery is a configuration — a coil shape, a lattice geometry, a mix of materials — that beats what the published literature has proposed.

A model that fits its training data well is not a result. A result is something the model or the simulation tells you that you did not already know.

## Three terms that recur on every page

- **Pre-registered.** The hypothesis, the success threshold, and the test procedure are committed to before the experiment runs. No moving the goalposts afterwards.
- **Out-of-sample.** The model is judged only on data it has never seen. A model that looks great on data it has already memorised is worth nothing.
- **Null result.** An experiment that shows the expected effect is not there. These are published here alongside positive results, because a study that only reports wins cannot be trusted.

## What to expect, and what not to

Every page on this site has been through the HDR loop and the adversarial review. That does not mean every page is right. It means every claim has been stress-tested against its own evidence and the published literature, and that negative results are reported alongside positive ones.

None of the work has been through formal academic peer review. If you find an error in any result, [email me](mailto:colinjoc92@gmail.com) and I will have it investigated and corrected.

---

[Browse the results portfolio →](/hdr/results/)

The framework and full project history lives on [GitHub](https://github.com/colinjoc/hdr_autoresearch).
