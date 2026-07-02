---
layout: default
title: VeryMath
---

<style>
  :root {
    --vm-ink: #16213d;
    --vm-muted: #5a6680;
    --vm-line: #dfe6f2;
    --vm-red: #b0182f;
    --vm-gold: #c99a2e;
    --vm-blue: #0b4f9c;
    --vm-bg: #f8fbff;
  }

  .vm-page {
    color: var(--vm-ink);
  }

  .vm-page img {
    max-width: 100%;
  }

  #header_wrap {
    min-height: 260px;
    border-bottom: 4px solid var(--vm-gold);
    background: linear-gradient(135deg, #07183d 0%, #123d7a 58%, #b0182f 100%);
  }

  #header_wrap .inner {
    max-width: 1120px;
    padding: 56px 10px 48px;
  }

  #project_title,
  #project_tagline {
    width: fit-content;
    max-width: 860px;
    color: #fff;
    text-shadow: none;
    background: rgba(7, 24, 61, 0.88);
    box-shadow: 0 14px 36px rgba(0, 0, 0, 0.28);
  }

  #project_title {
    margin: 0;
    padding: 12px 18px 14px;
    border-radius: 8px 8px 0 0;
    letter-spacing: 0;
  }

  #project_tagline {
    margin-top: 0;
    padding: 10px 18px 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 0 8px 8px 8px;
    font-size: 20px;
    line-height: 1.45;
  }

  #main_content_wrap {
    border: 0;
    background: #f7f9fd;
  }

  #main_content {
    max-width: 1120px;
    padding: 38px 10px 58px;
  }

  #forkme_banner {
    display: none;
  }

  .vm-hero {
    display: grid;
    grid-template-columns: minmax(0, 0.86fr) minmax(380px, 1.14fr);
    gap: 24px;
    align-items: center;
    margin-bottom: 30px;
    padding: 24px;
    border: 1px solid var(--vm-line);
    border-radius: 8px;
    background: #fff;
    box-shadow: 0 16px 42px rgba(22, 33, 61, 0.08);
  }

  .vm-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 10px;
  }

  .vm-logo {
    width: 58px;
    height: 58px;
    flex: 0 0 58px;
    border-radius: 14px;
    object-fit: cover;
    box-shadow: 0 10px 24px rgba(176, 24, 47, 0.16);
  }

  .vm-hero-visual {
    display: block;
    width: 100%;
    border-radius: 8px;
    border: 1px solid var(--vm-line);
    box-shadow: 0 18px 46px rgba(22, 33, 61, 0.14);
  }

  .vm-kicker {
    margin: 0 0 4px;
    color: var(--vm-red);
    font-weight: 700;
    letter-spacing: 0;
  }

  .vm-title {
    margin: 0;
    font-size: 42px;
    line-height: 1.06;
    letter-spacing: 0;
  }

  .vm-subtitle {
    margin: 14px 0 0;
    color: var(--vm-muted);
    font-size: 18px;
    line-height: 1.65;
  }

  .vm-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 20px;
  }

  .vm-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 40px;
    padding: 0 16px;
    border: 1px solid var(--vm-line);
    border-radius: 7px;
    font-weight: 700;
    text-decoration: none;
    background: #fff;
  }

  .vm-button-primary {
    background: var(--vm-red);
    border-color: var(--vm-red);
    color: #fff;
  }

  .vm-section {
    padding: 30px 0 8px;
  }

  .vm-section h2 {
    margin: 0 0 12px;
    font-size: 26px;
    letter-spacing: 0;
  }

  .vm-lead {
    margin: 0 0 18px;
    color: var(--vm-muted);
    line-height: 1.7;
  }

  .vm-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
  }

  .vm-card {
    border: 1px solid var(--vm-line);
    border-radius: 8px;
    padding: 16px;
    background: #fff;
  }

  .vm-card h3 {
    margin: 0 0 8px;
    font-size: 18px;
    letter-spacing: 0;
  }

  .vm-card p,
  .vm-card li {
    color: var(--vm-muted);
    line-height: 1.62;
  }

  .vm-card p {
    margin: 0;
  }

  .vm-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 12px 0 14px;
  }

  .vm-pill {
    display: inline-flex;
    align-items: center;
    min-height: 26px;
    padding: 0 10px;
    border-radius: 999px;
    background: var(--vm-bg);
    border: 1px solid var(--vm-line);
    color: var(--vm-muted);
    font-size: 13px;
    font-weight: 600;
  }

  .vm-project {
    border-left: 4px solid var(--vm-gold);
  }

  .vm-project-wide {
    grid-column: 1 / -1;
  }

  .vm-repo-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
  }

  .vm-repo-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 14px;
    margin-bottom: 8px;
  }

  .vm-repo-title {
    margin: 0;
  }

  .vm-repo-note {
    margin-top: 14px;
    padding: 12px 14px;
    border: 1px dashed var(--vm-line);
    border-radius: 8px;
    background: var(--vm-bg);
    color: var(--vm-muted);
    line-height: 1.62;
  }

  .vm-route-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
  }

  .vm-route {
    border-left: 3px solid var(--vm-blue);
  }

  .vm-feature-image {
    margin-top: 8px;
    border-radius: 8px;
    border: 1px solid var(--vm-line);
    box-shadow: 0 16px 40px rgba(22, 33, 61, 0.1);
  }

  .vm-timeline {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-top: 14px;
  }

  .vm-step {
    padding: 14px;
    border-top: 3px solid var(--vm-blue);
    background: var(--vm-bg);
    border-radius: 7px;
  }

  .vm-step strong {
    display: block;
    margin-bottom: 6px;
  }

  .vm-step span {
    color: var(--vm-muted);
    line-height: 1.56;
  }

  @media (max-width: 760px) {
    .vm-grid,
    .vm-hero,
    .vm-repo-list,
    .vm-route-grid,
    .vm-timeline {
      grid-template-columns: 1fr;
    }

    .vm-title {
      font-size: 34px;
    }

    #header_wrap {
      min-height: 230px;
    }

    #header_wrap .inner {
      padding: 56px 10px 42px;
    }

    #project_title {
      font-size: 36px;
    }

    #project_tagline {
      font-size: 17px;
    }

    .vm-logo {
      width: 52px;
      height: 52px;
      flex-basis: 52px;
    }

    .vm-repo-head {
      flex-direction: column;
      gap: 10px;
    }

    .vm-hero {
      padding: 18px;
    }
  }
</style>

<div class="vm-page">
  <section class="vm-hero">
    <div>
      <div class="vm-brand">
        <img class="vm-logo" src="/assets/img/VeryMathlogo.jpeg" alt="VeryMath logo">
        <div>
          <p class="vm-kicker">ECNU &gt;&gt; VeryMath</p>
          <h1 class="vm-title">VeryMath</h1>
        </div>
      </div>
      <div>
        <p class="vm-subtitle">
          VeryMath is an open-source organization for AI-assisted mathematical research.
          We build reusable, verifiable, and collaborative workflows for paper reading,
          computation, formalization, and research automation.
        </p>
        <p class="vm-subtitle">
          让数学科研流程可复用、可验证、可协作。
        </p>
        <div class="vm-actions">
          <a class="vm-button vm-button-primary" href="https://github.com/orgs/VeryMath/repositories">Browse Repositories</a>
          <a class="vm-button" href="https://github.com/VeryMath/co-mathematician">Start with co-mathematician</a>
        </div>
      </div>
    </div>
    <img class="vm-hero-visual" src="/assets/img/VeryMath.jpg" alt="VeryMath AI for Mathematical Research overview">
  </section>

  <section class="vm-section">
    <h2>What VeryMath Builds</h2>
    <p class="vm-lead">
      VeryMath focuses on practical infrastructure for mathematicians and research groups:
      not only chat-style assistance, but repository-backed processes where questions,
      assumptions, computations, failed attempts, reviews, and final writing can all be
      preserved as durable artifacts.
    </p>
    <div class="vm-grid">
      <div class="vm-card">
        <h3>Paper Reading</h3>
        <p>Extract definitions, assumptions, proof structure, citation trails, and open problems from research papers.</p>
      </div>
      <div class="vm-card">
        <h3>Computational Math</h3>
        <p>Turn numerical experiments, optimization routines, and symbolic checks into reproducible project files.</p>
      </div>
      <div class="vm-card">
        <h3>Lean Formalization</h3>
        <p>Connect informal arguments with formal proof workflows, theorem statements, and verification-oriented review.</p>
      </div>
      <div class="vm-card">
        <h3>Evolving Research</h3>
        <p>Support long-running research projects through workstreams, reviewer loops, skill libraries, and final-paper gates.</p>
      </div>
    </div>
  </section>

  <section class="vm-section">
    <h2>Repository Directory</h2>
    <p class="vm-lead">
      This page points visitors to VeryMath's public project repositories. The homepage
      repository, <code>verymath.github.io</code>, is intentionally omitted from the project
      directory so the list stays focused on reusable research tools and skill packages.
    </p>
    <div class="vm-repo-list">
      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Paper-Reading">AI4Math-Paper-Reading</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Paper-Reading">Open Repo</a>
        </div>
        <p>
          Structured workflows for reading mathematical papers, extracting proof dependencies,
          and turning papers into reusable AI4Math skills.
        </p>
        <div class="vm-meta">
          <span class="vm-pill">Paper Reading</span>
          <span class="vm-pill">2 skills</span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          Best for: theorem dependency analysis, source-grounded reading notes, and
          paper-to-skill extraction.
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Optimization">AI4Math-Optimization</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Optimization">Open Repo</a>
        </div>
        <p>
          Skill packages for mathematical optimization modeling, solver setup, LP/MIP/SOCP
          workflows, and manifold-constrained optimization.
        </p>
        <div class="vm-meta">
          <span class="vm-pill">Optimization</span>
          <span class="vm-pill">6 skills</span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          Best for: modeling mathematical programs, selecting solvers, adapting examples,
          and reporting evidence from optimization runs.
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Computational-Mathematics">AI4Math-Computational-Mathematics</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Computational-Mathematics">Open Repo</a>
        </div>
        <p>
          Computational workflows for numerical evidence, symbolic structure, finite element
          reasoning, and mathematical invariant computation.
        </p>
        <div class="vm-meta">
          <span class="vm-pill">Computational Math</span>
          <span class="vm-pill">4 skills</span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          Best for: turning mathematical objects, equations, data, or paper excerpts into
          reproducible computational evidence.
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Lean-Agents">AI4Math-Lean-Agents</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Lean-Agents">Open Repo</a>
        </div>
        <p>
          Lean 4 setup, formalization, proof repair, patch review, and optional
          Lean-specialist backend workflows for coding agents.
        </p>
        <div class="vm-meta">
          <span class="vm-pill">Lean 4</span>
          <span class="vm-pill">2 skills</span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          Best for: inspecting Lean projects, preparing mathlib workspaces, repairing proofs,
          and validating final patches with evidence.
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Evolving">AI4Math-Evolving</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Evolving">Open Repo</a>
        </div>
        <p>
          Agent-led workflows for iterative mathematical experiments, OpenEvolve runs,
          evaluation loops, and skill refinement.
        </p>
        <div class="vm-meta">
          <span class="vm-pill">Evolving Research</span>
          <span class="vm-pill">1 skill</span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          Best for: bounded experiment sessions, metric review, short probes, and
          next-step iteration.
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Auto-Research">AI4Math-Auto-Research</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Auto-Research">Open Repo</a>
        </div>
        <p>
          Agentic workflows for mathematical problem discovery, research-loop orchestration,
          and proof-blueprint review.
        </p>
        <div class="vm-meta">
          <span class="vm-pill">Auto Research</span>
          <span class="vm-pill">3 skills</span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          Best for: turning broad mathematical intent into structured problems, bounded
          research runs, and reviewed proof plans.
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Paper-Writing">AI4Math-Paper-Writing</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Paper-Writing">Open Repo</a>
        </div>
        <p>
          Source-grounded workflows for mathematical paper drafting, proof-obligation review,
          and submission-ready LaTeX checks.
        </p>
        <div class="vm-meta">
          <span class="vm-pill">Paper Writing</span>
          <span class="vm-pill">1 skill</span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          Best for: converting verified materials into paper text and review artifacts
          without losing source evidence.
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Sagemath-skill">AI4Math-Sagemath-skill</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Sagemath-skill">Open Repo</a>
        </div>
        <p>
          A SageMath skill that helps agents search SageMath documentation, write runnable
          SageMath Python code, execute checks, and report verified mathematical conclusions.
        </p>
        <div class="vm-meta">
          <span class="vm-pill">SageMath</span>
          <span class="vm-pill">Computation</span>
          <span class="vm-pill">GPL</span>
        </div>
        <p>
          Best for: algebra, number theory, combinatorics, symbolic computation, and
          SageMath-backed verification.
        </p>
      </div>

      <div class="vm-card vm-project vm-project-wide">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/co-mathematician">co-mathematician</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/co-mathematician">Open Repo</a>
        </div>
        <p>
          A repository-backed mathematical research workspace for coding agents, designed to
          make goals, messages, workstreams, reports, reviews, and final papers durable.
        </p>
        <div class="vm-meta">
          <span class="vm-pill">Research Workspace</span>
          <span class="vm-pill">Python</span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          Best for: starting a long-running AI-assisted math project and coordinating the
          other AI4Math skill repositories inside a reviewed workflow.
        </p>
      </div>
    </div>
  </section>

  <section class="vm-section">
    <h2>Choose a Starting Point</h2>
    <div class="vm-route-grid">
      <div class="vm-card vm-route">
        <h3>Read, Compute, Formalize</h3>
        <p>Start with the AI4Math skill repository closest to the immediate task: paper reading, optimization, computational mathematics, Lean, SageMath, or paper writing.</p>
      </div>
      <div class="vm-card vm-route">
        <h3>Run a Research Project</h3>
        <p>Use <a href="https://github.com/VeryMath/co-mathematician">co-mathematician</a> when the work needs tracked goals, multiple workstreams, reviewer gates, and a final working paper.</p>
      </div>
      <div class="vm-card vm-route">
        <h3>Browse Everything</h3>
        <p>Use the <a href="https://github.com/orgs/VeryMath/repositories">VeryMath repository list</a> to see all public repositories, including this homepage repository and future additions.</p>
      </div>
    </div>
  </section>

  <section class="vm-section">
    <h2>Research Workflow</h2>
    <p class="vm-lead">
      The current VeryMath stack is designed around a human mathematician working with
      repository-aware agents. The repository keeps the process inspectable and lets research
      output grow from reviewed intermediate artifacts rather than transient conversation.
    </p>
    <div class="vm-timeline">
      <div class="vm-step">
        <strong>1. Frame</strong>
        <span>Record the research question, notation, constraints, language policy, and approved goals.</span>
      </div>
      <div class="vm-step">
        <strong>2. Work</strong>
        <span>Create proof, computation, literature, and review workstreams with durable reports.</span>
      </div>
      <div class="vm-step">
        <strong>3. Verify</strong>
        <span>Use reviewer loops and completion gates before rendering a final working paper.</span>
      </div>
    </div>
  </section>

  <section class="vm-section">
    <h2>Join the Ecosystem</h2>
    <p class="vm-lead">
      VeryMath welcomes collaborators interested in AI for mathematics, formal methods,
      optimization, computational research, academic workflows, and open-source research tools.
    </p>
    <div class="vm-actions">
      <a class="vm-button vm-button-primary" href="https://github.com/orgs/VeryMath/repositories">View Repositories</a>
      <a class="vm-button" href="https://github.com/VeryMath/co-mathematician/issues">Open Issues</a>
    </div>
  </section>
</div>
