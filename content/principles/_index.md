---
title: "AI Design Principles"
---

> *Now that prose is essentially free, conciseness is the only thing that's valuable.*

## Communication

- **Bullet points over prose.** If it can be a list, make it a list.
- **Tables over paragraphs.** If it has structure, show the structure.
- **Numbers over adjectives.** "3.4× faster" beats "significantly faster."
- **One sentence per idea.** Compound sentences hide compound failures.
- **Lead with the answer.** Save context for after the punchline.
- **Cut every word that doesn't change the meaning.**
- **No throat-clearing.** Skip "I think," "it's worth noting," "as we discussed."

## Building with AI

- **The model is infrastructure. The discovery is the product.**
- **Test before you trust.** Even on tiny samples. Especially on tiny samples.
- **One change per experiment.** Bundled changes hide which one worked.
- **Commit before you run.** Reverts are free. Lost code isn't.
- **Cheap evaluation > clever model.** A 10× faster eval enables 100× more experiments.
- **Prefer published tools to custom ones.** Custom simulators encode the same simplifications as the analytical baseline you're trying to beat.
- **Negative results compound.** A knowledge base of dead ends is more valuable than a leaderboard of bests.

## Working with LLMs

- **State your prior before you look at the data.** This is what makes it research, not narrative.
- **Articulate the mechanism.** "Why should this work?" is the only filter that catches noise.
- **The agent will exploit any gap between your simulator and reality.** Add realism *before* optimising, not after.
- **Trust the loop, not the individual experiment.** Single results are noise; patterns over 10+ experiments are signal.
- **Delegate execution, not understanding.** If you can't explain why the result is what it is, you don't have a result.

## Output Discipline

- **Code over diagrams.** Code is unambiguous; diagrams require interpretation.
- **Markdown over slides.** Slides hide the structure of an argument.
- **Reproducible over polished.** A working notebook beats a beautiful PDF.
- **Link, don't copy.** Data lives at its canonical source. The repo links to it.

## Stopping

- **Stop when you've answered the question, not when you've filled the page.**
- **Plateau = explore, not tune.** Five reverts means it's time for a new approach.
- **Done means novel.** If you haven't found something the literature didn't predict, you haven't finished.
