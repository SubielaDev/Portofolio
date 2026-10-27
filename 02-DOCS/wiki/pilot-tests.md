---
title: RSC pilot tests
tags: [pilot, rsc, fabrica-de-ia]
---

# RSC pilot tests

Pilot for the AI Factory (`SubielaDev/fabrica-de-ia`). We ran 10 small, real tasks on this portfolio with RSC `@ericrisco/rsc@3.5.0`, unmodified, and recorded where it gets stuck.

**How the tasks were run:** each task went to a fresh Claude Code session started headless in this repo (`claude -p`), with RSC's hooks and skills active. Alfonso's corrections were sent back with `--resume`. `git push` and `gh` were blocked on the tool side, and every change stayed local.

## Setup (before the 10 tasks)

| Step | Without Alfonso touching code | Time | Rounds | What failed or got stuck | Cost |
| --- | --- | --- | --- | --- | --- |
| `onboard` (plan + accept) | yes | ~10 min (mostly questions) | 0 | Asks 5 questions in jargon ("software-scope", "workflow main/branches"). The plan text never says it grants `git commit`/`git push`/`gh pr create` without asking: you only see it in `.claude/settings.json`. No `CLAUDE.md` is created. | free |
| Fill the brain (`02-DOCS`) | yes | 66 s + 114 s | 1 (4 open questions) | Good questions, but phrased in programmer terms. Alfonso didn't understand "naming in Spanish". It wrote an expired production URL (taken from the GitHub homepage field); Alfonso caught it. | $0.78 + $2.14 |
| **Auto-publish incident** | — | — | — | The `knowledge-sync` Stop hook **pushed `02-DOCS`/`01-TOOLS` to the remote branch `rsc/knowledge` without asking**, and Vercel built a public Preview from it. Blocking `git push` in tool permissions does not stop it, because a hook runs it. Fix: `.rsc/.no-knowledge-sync` (machine-local only); the branch was deleted on GitHub. | — |
| Commit message | — | — | — | RSC wrote `chore: …` with no gitmoji, while Alfonso's convention is gitmoji + Conventional Commits. The auto-sync commit did use gitmoji. The `ship` skill says "authorship always Eric", hardcoded to the RSC author. | — |
| Shared memory | — | — | — | The headless RSC session edited the parent Claude session's private memory folder (`~/.claude/projects/.../memory`). | — |

## The 10 tasks

| # | Task | Without Alfonso touching code | Time | Rounds | What failed or got stuck | Cost |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | |

## Summary: where RSC gets stuck

_(filled in at the end)_
