---
layout: default
title: VeryMath Handbook
permalink: /handbook/HANDBOOK.html
---

# VeryMath Handbook

[中文说明](/handbook/HANDBOOK.zh-CN.html)

VeryMath is a collection of mathematical tooling for coding agents, in two main parts:

- **Skill packages**: install them into your coding agent, and the agent invokes them automatically or when you name them.
- **Standalone programs, such as agent harnesses**: tools you deploy and run yourself, with their own UI or CLI.

---

## 1. Installing a Skill

Every AI4Math Skill installs the same way: **open your coding agent and send it a message asking it to do the install**. You do not run commands or configure paths yourself.

This works with Codex, Claude Code, OpenCode, Cursor, or any coding agent that can read and write local files and run terminal commands.

### General template

Send this to your agent, substituting the repository and the packages you want:

```text
Please install these AI4Math Skills for me.

Repository: <repository URL>
Branch: main
Skill paths:
- skills/<package-1>
- skills/<package-2>

Steps:
1. Clone or update the repository locally.
2. Read README.md, SKILL.md, and each target Skill entrypoint.
3. If this environment supports local Skill discovery, link each directory that contains SKILL.md into the local skills directory.
4. Keep shared sibling support directories in place when a Skill depends on them.
5. Verify that the installed Skills are discoverable.
6. Tell me the installed paths, whether a restart is needed, and give me one test prompt.
```

The agent figures out where your environment keeps its skills directory (`~/.codex/skills` for Codex, `~/.claude/skills` for Claude Code, `~/.config/opencode/skills` for OpenCode, elsewhere for others). You do not need to know.

### Worked example: `math-paper-reading`

This walkthrough uses [`math-paper-reading`](https://github.com/VeryMath/AI4Math-Paper-Reading) from the AI4Math · Paper Reading repository (`skills/math-paper-reading/`).

**You:**

```text
Please install the AI4Math math-paper-reading Skill for me.

Repository: https://github.com/VeryMath/AI4Math-Paper-Reading
Branch: main
Skill path: skills/math-paper-reading

Steps:
1. Clone or update the repository locally.
2. Read README.md, SKILL.md, and the entry files under skills/math-paper-reading/.
3. If this environment supports local Skill discovery, install the directory that contains SKILL.md into the local skills directory.
4. Keep shared sibling support directories in place if this Skill depends on them.
5. Verify that the installed Skill is discoverable.
6. Tell me the installed path, whether a restart is needed, and give me one test prompt.
```

**The agent:** clones the repository, reads `skills/math-paper-reading/SKILL.md`, installs that directory into your local skills directory, and reports the path.

**Verify install:** in a fresh session with a prompt that names the skill:

```text
Using math-paper-reading, what is your first workflow step when given a PDF math paper?
Do not read a file yet; outline the process exactly as the Skill specifies.
```

If the answer clearly reflects the installed `SKILL.md` (steps and terminology match the repo docs) rather than a generic summary, the install worked.

In daily use you do not need to name a Skill every time; the agent matches the relevant installed Skill from your task on its own.

### Updating and removing

Also one message:

```text
Update the AI4Math Skills installed on this machine: pull the latest main branch
for each repository, sync the installed Skill directories, and tell me what changed.
```

```text
Uninstall the <package> Skill: remove it from the local skills directory
but keep the cloned repository.
```

### Things to know

- **A Skill is instructions, not a runtime.** The SageMath Skill needs SageMath on your machine, the Lean Skills need Lean 4 and mathlib, the optimization Skills need their solvers. The Skills themselves usually guide the agent through installing these, but they ask for your approval first.
- **Review anything that downloads, installs an environment, or creates a conda environment before approving it.**
- **Account logins are yours to do.** Never hand an agent an API key to commit into a repository.
- A restart may be needed before a newly installed Skill is discovered; the agent will tell you.

---

## 2. Applications

### VeryMath Textbook Copilot

A self-hosted course workspace. Read your textbook PDF on the left, talk to the Copilot on the right. Import your own textbook, connect a coding agent, and you can ask about any chapter, get explanations, generate exercises, mind maps, knowledge graphs, and LaTeX slides. All data stays on your own machine (`~/.course-copilot/` by default) and runs under your own agent account.

**Core features**

- Textbook parsing: turn selected pages or chapters into a readable digital textbook with body text, formulas, images, and outline
- Explanations: layered treatment of concepts, theorems, algorithms, and worked examples, with figures where useful
- Quiz generation: exercise cards with progressive hints and reference answers
- Mind maps and knowledge graphs: hierarchical knowledge trees and concept networks, with nodes that jump back to the source page
- Slides: compile chapters into 16:9 PDF decks via LaTeX Beamer
- Free-form Q&A: no fixed template, organized around whatever you ask
- Supporting materials: attach handouts, solutions, and references per textbook, with full-text search and OCR for scans

**Requirements:** Node.js ≥ 22.13. Slide generation needs XeLaTeX, Beamer, ctex, and CJK fonts. OCR needs Tesseract (plus `chi_sim`/`chi_tra` for Chinese) and Poppler. On Windows, install everything inside WSL2.

**Installation** is again a single message to your agent:

```text
Pull https://github.com/VeryMath/VeryMath-textbook-copilot and follow
skills/verymath-install/SKILL.md to deploy VeryMath Textbook Copilot on this machine:
check and install the required dependencies, configure the built-in course Skills,
connect my existing agent, start the workspace, and give me the URL.
```

The agent installs dependencies, configures the built-in course Skills, connects your agent, starts the service, and returns the address (production defaults to `http://127.0.0.1:4173`, bound to localhost only). In the browser, click "Import textbook" to select a PDF, then connect your agent under workspace settings.

The bundled course Skills are `textbook-parse`, `explain`, `quiz`, `mindmap`, `knowledge-graph`, and `textbook-to-ppt`, plus `verymath-install` which performs the deployment.

Supported agents: Codex, Claude Code, OpenCode, Cursor, Gemini CLI, Copilot CLI, Qwen Code, Kimi Code, Kiro CLI. Pick one.

Current releases: v0.1.0 (macOS preview), v0.1.1 (Windows preview).

Full documentation → [VeryMath-textbook-copilot](https://github.com/VeryMath/VeryMath-textbook-copilot) ｜ [User guide](https://github.com/VeryMath/VeryMath-textbook-copilot/blob/main/docs/user-guide.md) ｜ [Architecture](https://github.com/VeryMath/VeryMath-textbook-copilot/blob/main/docs/architecture.md) ｜ [Skill development](https://github.com/VeryMath/VeryMath-textbook-copilot/blob/main/docs/skill-development.md)

---

### Co-Mathematician

Turns a mathematical research conversation into a file-backed project. The formula is "coding agent + repo filesystem + gates + reviewer loop = research workspace": the agent's main thread acts as Project Coordinator, the research question, goals, status, and messages live in `workspace/project/`, proof, computation, literature, and review work each become their own workstream, and the final paper is rendered only from reviewed reports.

The Python harness does not run agents. It initializes files, appends messages, creates approved workstreams, checks gates, and renders the working paper. Your coding agent does the work.

**How it works**

- A goal must be marked `approved` before it can receive workstreams; draft goals are not executable
- Workstream kinds are `proof`, `computation`, `literature`, and `review`
- Each report carries provenance for important claims, explicit uncertainty, failed explorations, and independent reviewer output under `reviews/`
- `workspace/final/working_paper.md` is a working paper, not a chat summary
- AI4Math domain Skills can be installed into a project's `.agents/skills/`, and the Coordinator suggests and hands off to them as needed

**Installation**, again through your agent:

```text
Install Co-Math from https://github.com/VeryMath/co-mathematician.git,
set ~/CoMathProjects as the projects directory, and create a project named
Muon Convergence. Return its path but do not start the research yet.
```

Then open that project directory in your coding agent and say "Continue this Co-Math project." Day to day, manage projects with `co-math list / resume / next / archive / reopen`.

Full documentation → [co-mathematician](https://github.com/VeryMath/co-mathematician)

---

## 3. The Skill repositories

### AI4Math · SageMath — exact symbolic computation

Verified SageMath computation for mathematical agents: the agent searches the bundled SageMath reference first, writes Sage code in ordinary Python form, executes it locally, and reports results backed by real runtime output. Covers algebra, number theory, combinatorics, graph theory, polynomial rings, matrices, calculus, finite fields, elliptic curves, Galois groups, coding theory, cryptography, manifolds, and modular forms. Windows users should install and run SageMath inside WSL.

| Package | Use it for |
| --- | --- |
| `sagemath-skill` | Reference lookup, code execution, and reproducible results |

Full documentation → [AI4Math-Sagemath-skill](https://github.com/VeryMath/AI4Math-Sagemath-skill)

---

### AI4Math · Auto Research — problem discovery and research loops

Turns broad mathematical intent into structured problems, bounded research runs, and reviewed proof plans. The largest repository by package count; it also includes helpers that install and drive external research systems (Rethlas, Archon, Danus).

| Package | Use it for |
| --- | --- |
| `discover-math-problems` | Ranked problems, conjecture lattices, evidence ledgers, and work orders from fuzzy background |
| `proof-blueprint-review` | Proof blueprints, verifier-style reviews, repair hints, strict proof-status reports |
| `open-problem-research-pipeline` | Staged literature search, method analysis, proof framework, and report workflow |
| `graph-theory-researcher` | Read graph theory papers, select questions through user gates, produce verified LaTeX/PDF |
| `agent-laboratory-workflow` | Deploy, validate, and launch bounded Agent Laboratory runs |
| `rethlas-helper` | Install Rethlas and run natural-language proof generation from any project |
| `archon-helper` | Install Archon and run formalization workflows |
| `danus-helper` / `danus-helper-dsh` | Install Danus (OpenCode / DeepSeek Harness variants) for multi-agent research, monitoring, summaries, and paper writing |

Full documentation → [AI4Math-Auto-Research](https://github.com/VeryMath/AI4Math-Auto-Research)

---

### AI4Math · Paper Reading — deep reading and extraction

Structured reading of mathematical papers, theorem dependency extraction, and conversion of papers into reusable Skills.

| Package | Use it for |
| --- | --- |
| `math-paper-reading` | Deep reading, theorem dependencies, proof pathways, local reference notes |
| `paper-to-skill` | PDF preparation, paper triage, proof-pattern extraction, cross-paper synthesis |
| `after-ocr` | Audit and repair formula-heavy OCR Markdown with coverage tracking, evidence logs, multi-pass reconciliation |
| `graph-theory-paper-reading` | Deep-read graph theory papers into structured LaTeX reports with proof trees |

Full documentation → [AI4Math-Paper-Reading](https://github.com/VeryMath/AI4Math-Paper-Reading)

---

### AI4Math · Writing — papers and slides

Writing from verified material. It does not replace source evidence, proof checking, or experiment validation; every claim should trace back to a source.

| Package | Use it for |
| --- | --- |
| `paper-writing` | Draft, revise, structure, and audit papers, with claim-evidence review, proof-obligation checks, notation checks, formula readability, and LaTeX preflight |
| `math-beamer` | Source-grounded Beamer decks: auditable templates, compilation, layout inspection, slide-to-source ledger |

Full documentation → [AI4Math-Writing](https://github.com/VeryMath/AI4Math-Writing)

---

### AI4Math · Lean Agents — Lean 4 formalization

A structured way for agents to inspect Lean projects, set up reusable Lean/mathlib workspaces, formalize theorem statements, repair proofs, complete `sorry`s, and validate patches locally. Final patches must not introduce `sorry`, `admit`, new axioms, or silent theorem-statement drift.

| Package | Use it for |
| --- | --- |
| `lean-setup` | Install or verify Lean 4, `elan`, `lake`, and mathlib workspace readiness |
| `lean-formalization` | Formalize statements, repair proofs, complete `sorry`s, review patches, coordinate optional backends |

`skills/lean-runtime/` is a shared support layer (scripts, schemas, prompts, tests) that you never invoke directly, but it must stay next to the two public packages. Numina, Archon, and other backends are optional adapters requiring your explicit approval.

Full documentation → [AI4Math-Lean-Agents](https://github.com/VeryMath/AI4Math-Lean-Agents)

---

### AI4Math · Optimization — modeling and solving

Modeling mathematical programs, selecting and configuring solvers, and reporting evidence from runs.

| Package | Use it for |
| --- | --- |
| `optskills` | 103 released OptSkills problem-archetype cards, usable on their own for modeling and solving |
| `mixed-integer-programming` | MILP/MIP with binary, integer, and continuous decision variables |
| `second-order-cone-programming` | SOCP modeling and cvxpy-based conic solver workflows |
| `osqp-solver` | OSQP modeling, repeated solves, status gates, independent verification for continuous convex QPs |
| `cdopt-optimization` | CDOpt and manifold-constrained optimization: modeling, validation, runner generation, evidence reports |
| `or-solver` | Dependencies, installation, licenses, environment variables, and setup troubleshooting for a chosen solver |

The division of labor: you or the modeling Skill choose the solver; `or-solver` configures that solver.

Full documentation → [AI4Math-Optimization](https://github.com/VeryMath/AI4Math-Optimization)

---

### AI4Math · Computational Mathematics

Turning mathematical objects, equations, data, or paper excerpts into reviewed computational representations and reproducible evidence.

| Package | Use it for |
| --- | --- |
| `invariant-computation` | Route and validate algebraic, topological, geometric, TDA, and certified numerical invariants |
| `least-squares` | Linear, polynomial, nonlinear, regularized, constrained, and Bayesian least-squares fitting |
| `scientific-computing-reproduction` | Reproduce, diagnose, tune, visualize, and report research code with human approval checkpoints |

Full documentation → [AI4Math-Computational-Mathematics](https://github.com/VeryMath/AI4Math-Computational-Mathematics)

---

### AI4Math · Evolving — iterative experiments

Currently focused on bounded OpenEvolve experiment sessions.

| Package | Use it for |
| --- | --- |
| `openevolve-experiment-workflow` | Inspect or create OpenEvolve projects, validate runtime config, run bounded probes, summarize metrics, guide iteration |

Full documentation → [AI4Math-Evolving](https://github.com/VeryMath/AI4Math-Evolving)

---

### AI4Math · MathTool — standalone tools

Standalone mathematical tools and lightweight agent adapters. Each package keeps its own workflow, dependencies, provenance, and tests.

| Package | Use it for | Status |
| --- | --- | --- |
| `math-glossary` | Build, review, back up, import, export, and maintain bilingual mathematical glossaries | Released as v0.1.0 (MIT) |
| `matlab-runner` | Route explicit MATLAB tasks through a MATLAB MCP server with execution, testing, and numerical-validation evidence | Review candidate, unreleased |

Full documentation → [AI4Math-MathTool](https://github.com/VeryMath/AI4Math-MathTool)

---

## 4. Website

The VeryMath project homepage: organization overview, repository navigation, and updates.

- [VeryMath homepage](https://verymath.github.io/)
- [中文使用手册](/handbook/HANDBOOK.zh-CN.html) · [English Handbook](/handbook/HANDBOOK.html)
- [Site source](https://github.com/VeryMath/verymath.github.io)
