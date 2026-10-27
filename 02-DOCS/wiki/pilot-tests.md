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
| 1 | Delete the hidden "Task Manager App" card | yes | 100 s | 2 | Round 1 stopped: it asked "worktree or main?" | $1.02 |
| 2 | Rename "Dashboard Personal" → "Agenda Clínica Online" | yes | 78 s | 2 | Same worktree stop. Good copy once unblocked | $0.91 |
| 3 | Dead "Código/Demo" buttons → "Próximamente" | yes | 52 s | 2 | Same worktree stop | $0.84 |
| 4 | Remove the stray `</div>` | yes | 133 s | 2 | Same worktree stop. Careful diagnosis, but no real HTML parser or browser available | $1.30 |
| 5 | Load Google Fonts once | yes | 88 s | 2 | Same worktree stop | $0.94 |
| 6 | Footer year updates itself | yes | 119 s | 2 | Round 1 edited `main` without testing or committing (`node` needed approval) | $1.23 |
| 7 | Accessible names on social icons | yes | 86 s | 2 | Round 1 couldn't commit: task 6's uncommitted edits were in the same file | $1.28 |
| 8 | SEO description + WhatsApp/LinkedIn preview image | yes | 186 s | 2 | Round 1 stopped (worktree + no image tool). Round 2 **installed Pillow into the user's Python without asking**. Real preview only visible after deploy | $1.68 |
| 9 | Remove unused CSS and images | yes | 243 s | 2 | Round 1 built a worktree branch off the **stale** `f15ef30` and couldn't merge it. Round 2 merged it, plus a merge commit | $2.80 |
| 10 | Add `.dockerignore` | yes, but not proven | 78 s | 2 | Docker not on PATH, so it simulated the build with Python instead. Never built for real | $1.09 |

**Total:** 10 of 10 done, with no code typed by Alfonso. Each took 2 rounds and about 20 minutes of machine time. All work cost about **$16**: about $13 for the 10 tasks and about $3 for setup. Nothing went to `main` on GitHub, and the live site is unchanged. Not checked in a real browser on a phone, Safari or Edge: only DOM checks in a local preview.

**Leftovers:** `.gradiente-3` and `.retraso-200` are now dead CSS. Task 9 kept them on purpose, and task 1 removed their only user. The README still says © 2025. Commits use plain Conventional Commits, without Alfonso's gitmoji.

## Summary: where RSC gets stuck

1. **It publishes on its own.** The `knowledge-sync` hook pushed docs to GitHub with no prompt, and Vercel deployed them publicly. Tool-level "no push" rules don't cover hooks. → The factory needs a **publish gatekeeper**: one agent or step that owns every push, PR and deploy and asks the human first.
2. **It freezes when two agents share a folder.** In round 1, 8 of 10 tasks stopped to ask a jargon question ("worktree or main?"), even though onboarding had recorded "main". No one can answer it in unattended mode. → The factory needs an **orchestrator/workspace manager**: it gives each agent its own isolated checkout, and serializes merges onto one file set.
3. **Its questions are in programmer language.** "Worktree", "git apply --cached", "naming in Spanish". Alfonso had to ask what they meant. → The factory needs a **translator/intake agent**: it turns technical questions into plain yes/no choices, and answers the ones already settled by recorded decisions.
4. **It can't prove the result in the real world.** No browser, no Docker, no phone check. The "done" claims rest on scripts and hand reading. → The factory needs a **verifier agent** with a real browser (mobile viewport plus the target browsers) and the build tools ready. It checks the preview deploy before production.
5. **It assumes facts and changes the machine.** It used the expired homepage URL from GitHub, installed Pillow globally, and edited another session's memory folder. → The factory needs **guardrails**: an environment setup step with tools preinstalled, a rule against global installs, and a sandboxed home folder per agent.
6. **Small convention slips.** No gitmoji in commits, and the `ship` skill says "authorship always Eric". → Put **project conventions in one config** that every agent reads, instead of RSC's defaults.

Plain-language version for Alfonso: RSC is a good worker on its own. Once someone answers its doubts, it does small jobs well and checks them. It gets stuck in three situations: when it isn't sure it can save its work, when it must ask something only a programmer would understand, and when it would need to see the web like a real visitor. It also once published something without asking. The factory's custom agents should cover exactly those gaps: a gatekeeper, an orchestrator, a translator and a verifier.
