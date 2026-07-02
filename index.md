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
    display: flex;
    flex-direction: column;
    gap: 22px;
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
    justify-content: center;
    gap: 12px;
    margin-bottom: 8px;
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
    text-align: justify;
    text-align-last: left;
  }

  .vm-hero-copy {
    width: 100%;
    max-width: 880px;
    margin: 0 auto;
  }

  .vm-actions {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
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

  .vm-language-toggle {
    display: flex;
    justify-content: flex-end;
    gap: 8px;
    margin: 0 0 14px;
  }

  .vm-lang-button {
    min-height: 34px;
    padding: 0 12px;
    border: 1px solid var(--vm-line);
    border-radius: 7px;
    background: #fff;
    color: var(--vm-muted);
    font-weight: 700;
    cursor: pointer;
  }

  .vm-lang-button[aria-pressed="true"] {
    border-color: var(--vm-red);
    background: var(--vm-red);
    color: #fff;
  }

  html[data-vm-lang="zh"] .lang-en {
    display: none;
  }

  html:not([data-vm-lang="zh"]) .lang-zh {
    display: none;
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
  <div class="vm-language-toggle" aria-label="Language switcher">
    <button class="vm-lang-button" type="button" data-set-lang="en" aria-pressed="true">English</button>
    <button class="vm-lang-button" type="button" data-set-lang="zh" aria-pressed="false">中文</button>
  </div>

  <section class="vm-hero">
    <div class="vm-hero-copy">
      <div class="vm-brand">
        <img class="vm-logo" src="/assets/img/VeryMathlogo.jpeg" alt="VeryMath logo">
        <div>
          <p class="vm-kicker">ECNU &gt;&gt; VeryMath</p>
          <h1 class="vm-title">VeryMath</h1>
        </div>
      </div>
      <div>
        <p class="vm-subtitle">
          <span class="lang-en">VeryMath is an open-source organization for AI-assisted mathematical research. We build reusable, verifiable, and collaborative workflows for paper reading, computation, formalization, and research automation.</span>
          <span class="lang-zh">VeryMath 是面向 AI 辅助数学研究的开源组织，致力于构建可复用、可验证、可协作的科研流程，覆盖论文阅读、数学计算、形式化验证与自动化研究。</span>
        </p>
        <div class="vm-actions">
          <a class="vm-button vm-button-primary" href="https://github.com/orgs/VeryMath/repositories"><span class="lang-en">Browse Repositories</span><span class="lang-zh">浏览仓库</span></a>
          <a class="vm-button" href="https://github.com/VeryMath/co-mathematician"><span class="lang-en">Start with co-mathematician</span><span class="lang-zh">从 co-mathematician 开始</span></a>
        </div>
      </div>
    </div>
    <img class="vm-hero-visual" src="/assets/img/VeryMath.jpg" alt="VeryMath AI for Mathematical Research overview">
  </section>

  <section class="vm-section">
    <h2><span class="lang-en">What VeryMath Builds</span><span class="lang-zh">VeryMath 在构建什么</span></h2>
    <p class="vm-lead">
      <span class="lang-en">VeryMath focuses on practical infrastructure for mathematicians and research groups: not only chat-style assistance, but repository-backed processes where questions, assumptions, computations, failed attempts, reviews, and final writing can all be preserved as durable artifacts.</span>
      <span class="lang-zh">VeryMath 关注数学家和研究团队真正可使用的基础设施：不只是聊天式辅助，而是用仓库承载研究过程，让问题、假设、计算、失败尝试、评审意见和最终写作都成为可追踪的持久成果。</span>
    </p>
    <div class="vm-grid">
      <div class="vm-card">
        <h3><span class="lang-en">Paper Reading</span><span class="lang-zh">论文阅读</span></h3>
        <p><span class="lang-en">Extract definitions, assumptions, proof structure, citation trails, and open problems from research papers.</span><span class="lang-zh">从数学论文中抽取定义、假设、证明结构、引用脉络和开放问题。</span></p>
      </div>
      <div class="vm-card">
        <h3><span class="lang-en">Computational Math</span><span class="lang-zh">计算数学</span></h3>
        <p><span class="lang-en">Turn numerical experiments, optimization routines, and symbolic checks into reproducible project files.</span><span class="lang-zh">将数值实验、优化流程和符号检验整理为可复现的项目文件。</span></p>
      </div>
      <div class="vm-card">
        <h3><span class="lang-en">Lean Formalization</span><span class="lang-zh">Lean 形式化</span></h3>
        <p><span class="lang-en">Connect informal arguments with formal proof workflows, theorem statements, and verification-oriented review.</span><span class="lang-zh">连接非形式化论证、定理陈述、形式化证明流程和面向验证的审查。</span></p>
      </div>
      <div class="vm-card">
        <h3><span class="lang-en">Evolving Research</span><span class="lang-zh">演化式研究</span></h3>
        <p><span class="lang-en">Support long-running research projects through workstreams, reviewer loops, skill libraries, and final-paper gates.</span><span class="lang-zh">通过工作流、评审循环、技能库和最终论文门控支持长期研究项目。</span></p>
      </div>
    </div>
  </section>

  <section class="vm-section">
    <h2><span class="lang-en">Repository Directory</span><span class="lang-zh">仓库导览</span></h2>
    <p class="vm-lead">
      <span class="lang-en">Explore VeryMath's public repositories by research task, from paper reading and computation to formalization, automated research, writing, and long-running project workspaces.</span>
      <span class="lang-zh">按研究任务浏览 VeryMath 的公开仓库：从论文阅读、数学计算到形式化验证、自动化研究、论文写作和长期项目工作区。</span>
    </p>
    <div class="vm-repo-list">
      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Paper-Reading">AI4Math-Paper-Reading</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Paper-Reading"><span class="lang-en">Open Repo</span><span class="lang-zh">打开仓库</span></a>
        </div>
        <p>
          <span class="lang-en">Structured workflows for reading mathematical papers, extracting proof dependencies, and turning papers into reusable AI4Math skills.</span>
          <span class="lang-zh">用于阅读数学论文、抽取证明依赖，并将论文内容转化为可复用 AI4Math 技能的结构化流程。</span>
        </p>
        <div class="vm-meta">
          <span class="vm-pill"><span class="lang-en">Paper Reading</span><span class="lang-zh">论文阅读</span></span>
          <span class="vm-pill"><span class="lang-en">2 skills</span><span class="lang-zh">2 个技能</span></span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          <span class="lang-en">Best for: theorem dependency analysis, source-grounded reading notes, and paper-to-skill extraction.</span>
          <span class="lang-zh">适合：定理依赖分析、基于原文证据的阅读笔记，以及从论文抽取技能。</span>
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Optimization">AI4Math-Optimization</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Optimization"><span class="lang-en">Open Repo</span><span class="lang-zh">打开仓库</span></a>
        </div>
        <p>
          <span class="lang-en">Skill packages for mathematical optimization modeling, solver setup, LP/MIP/SOCP workflows, and manifold-constrained optimization.</span>
          <span class="lang-zh">面向数学优化建模、求解器配置、LP/MIP/SOCP 工作流和流形约束优化的技能包。</span>
        </p>
        <div class="vm-meta">
          <span class="vm-pill"><span class="lang-en">Optimization</span><span class="lang-zh">优化</span></span>
          <span class="vm-pill"><span class="lang-en">6 skills</span><span class="lang-zh">6 个技能</span></span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          <span class="lang-en">Best for: modeling mathematical programs, selecting solvers, adapting examples, and reporting evidence from optimization runs.</span>
          <span class="lang-zh">适合：建立数学规划模型、选择求解器、改写示例，以及汇报优化运行证据。</span>
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Computational-Mathematics">AI4Math-Computational-Mathematics</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Computational-Mathematics"><span class="lang-en">Open Repo</span><span class="lang-zh">打开仓库</span></a>
        </div>
        <p>
          <span class="lang-en">Computational workflows for numerical evidence, symbolic structure, finite element reasoning, and mathematical invariant computation.</span>
          <span class="lang-zh">面向数值证据、符号结构、有限元推理和数学不变量计算的计算工作流。</span>
        </p>
        <div class="vm-meta">
          <span class="vm-pill"><span class="lang-en">Computational Math</span><span class="lang-zh">计算数学</span></span>
          <span class="vm-pill"><span class="lang-en">4 skills</span><span class="lang-zh">4 个技能</span></span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          <span class="lang-en">Best for: turning mathematical objects, equations, data, or paper excerpts into reproducible computational evidence.</span>
          <span class="lang-zh">适合：将数学对象、方程、数据或论文片段转化为可复现的计算证据。</span>
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Lean-Agents">AI4Math-Lean-Agents</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Lean-Agents"><span class="lang-en">Open Repo</span><span class="lang-zh">打开仓库</span></a>
        </div>
        <p>
          <span class="lang-en">Lean 4 setup, formalization, proof repair, patch review, and optional Lean-specialist backend workflows for coding agents.</span>
          <span class="lang-zh">面向编码代理的 Lean 4 环境配置、形式化、证明修复、补丁审查和可选 Lean 专家后端流程。</span>
        </p>
        <div class="vm-meta">
          <span class="vm-pill">Lean 4</span>
          <span class="vm-pill"><span class="lang-en">2 skills</span><span class="lang-zh">2 个技能</span></span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          <span class="lang-en">Best for: inspecting Lean projects, preparing mathlib workspaces, repairing proofs, and validating final patches with evidence.</span>
          <span class="lang-zh">适合：检查 Lean 项目、准备 mathlib 工作区、修复证明，并用证据验证最终补丁。</span>
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Evolving">AI4Math-Evolving</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Evolving"><span class="lang-en">Open Repo</span><span class="lang-zh">打开仓库</span></a>
        </div>
        <p>
          <span class="lang-en">Agent-led workflows for iterative mathematical experiments, OpenEvolve runs, evaluation loops, and skill refinement.</span>
          <span class="lang-zh">由智能体驱动的迭代数学实验、OpenEvolve 运行、评估循环和技能改进流程。</span>
        </p>
        <div class="vm-meta">
          <span class="vm-pill"><span class="lang-en">Evolving Research</span><span class="lang-zh">演化研究</span></span>
          <span class="vm-pill"><span class="lang-en">1 skill</span><span class="lang-zh">1 个技能</span></span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          <span class="lang-en">Best for: bounded experiment sessions, metric review, short probes, and next-step iteration.</span>
          <span class="lang-zh">适合：有边界的实验会话、指标审查、短探测和下一步迭代。</span>
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Auto-Research">AI4Math-Auto-Research</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Auto-Research"><span class="lang-en">Open Repo</span><span class="lang-zh">打开仓库</span></a>
        </div>
        <p>
          <span class="lang-en">Agentic workflows for mathematical problem discovery, research-loop orchestration, and proof-blueprint review.</span>
          <span class="lang-zh">面向数学问题发现、研究循环编排和证明蓝图审查的智能体工作流。</span>
        </p>
        <div class="vm-meta">
          <span class="vm-pill"><span class="lang-en">Auto Research</span><span class="lang-zh">自动研究</span></span>
          <span class="vm-pill"><span class="lang-en">3 skills</span><span class="lang-zh">3 个技能</span></span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          <span class="lang-en">Best for: turning broad mathematical intent into structured problems, bounded research runs, and reviewed proof plans.</span>
          <span class="lang-zh">适合：将宽泛的数学意图转化为结构化问题、有边界的研究运行和经过审查的证明计划。</span>
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Paper-Writing">AI4Math-Paper-Writing</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Paper-Writing"><span class="lang-en">Open Repo</span><span class="lang-zh">打开仓库</span></a>
        </div>
        <p>
          <span class="lang-en">Source-grounded workflows for mathematical paper drafting, proof-obligation review, and submission-ready LaTeX checks.</span>
          <span class="lang-zh">基于来源证据的数学论文写作、证明义务审查和投稿级 LaTeX 检查流程。</span>
        </p>
        <div class="vm-meta">
          <span class="vm-pill"><span class="lang-en">Paper Writing</span><span class="lang-zh">论文写作</span></span>
          <span class="vm-pill"><span class="lang-en">1 skill</span><span class="lang-zh">1 个技能</span></span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          <span class="lang-en">Best for: converting verified materials into paper text and review artifacts without losing source evidence.</span>
          <span class="lang-zh">适合：在不丢失来源证据的前提下，将已验证材料转化为论文文本和审查材料。</span>
        </p>
      </div>

      <div class="vm-card vm-project">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/AI4Math-Sagemath-skill">AI4Math-Sagemath-skill</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/AI4Math-Sagemath-skill"><span class="lang-en">Open Repo</span><span class="lang-zh">打开仓库</span></a>
        </div>
        <p>
          <span class="lang-en">A SageMath skill that helps agents search SageMath documentation, write runnable SageMath Python code, execute checks, and report verified mathematical conclusions.</span>
          <span class="lang-zh">帮助智能体检索 SageMath 文档、编写可运行 SageMath Python 代码、执行检查并汇报已验证数学结论的技能。</span>
        </p>
        <div class="vm-meta">
          <span class="vm-pill">SageMath</span>
          <span class="vm-pill"><span class="lang-en">Computation</span><span class="lang-zh">计算</span></span>
          <span class="vm-pill">GPL</span>
        </div>
        <p>
          <span class="lang-en">Best for: algebra, number theory, combinatorics, symbolic computation, and SageMath-backed verification.</span>
          <span class="lang-zh">适合：代数、数论、组合数学、符号计算，以及基于 SageMath 的验证。</span>
        </p>
      </div>

      <div class="vm-card vm-project vm-project-wide">
        <div class="vm-repo-head">
          <h3 class="vm-repo-title"><a href="https://github.com/VeryMath/co-mathematician">co-mathematician</a></h3>
          <a class="vm-button" href="https://github.com/VeryMath/co-mathematician"><span class="lang-en">Open Repo</span><span class="lang-zh">打开仓库</span></a>
        </div>
        <p>
          <span class="lang-en">A repository-backed mathematical research workspace for coding agents, designed to make goals, messages, workstreams, reports, reviews, and final papers durable.</span>
          <span class="lang-zh">一个由仓库承载的数学研究工作区，面向编码代理，让目标、消息、工作流、报告、审查和最终论文都可以持久保存。</span>
        </p>
        <div class="vm-meta">
          <span class="vm-pill"><span class="lang-en">Research Workspace</span><span class="lang-zh">研究工作区</span></span>
          <span class="vm-pill">Python</span>
          <span class="vm-pill">MIT License</span>
        </div>
        <p>
          <span class="lang-en">Best for: starting a long-running AI-assisted math project and coordinating the other AI4Math skill repositories inside a reviewed workflow.</span>
          <span class="lang-zh">适合：启动长期 AI 辅助数学研究项目，并在经过审查的流程中协调其他 AI4Math 技能仓库。</span>
        </p>
      </div>
    </div>
  </section>

  <section class="vm-section">
    <h2><span class="lang-en">Choose a Starting Point</span><span class="lang-zh">选择入口</span></h2>
    <div class="vm-route-grid">
      <div class="vm-card vm-route">
        <h3><span class="lang-en">Read, Compute, Formalize</span><span class="lang-zh">阅读、计算、形式化</span></h3>
        <p><span class="lang-en">Start with the AI4Math skill repository closest to the immediate task: paper reading, optimization, computational mathematics, Lean, SageMath, or paper writing.</span><span class="lang-zh">从最接近当前任务的 AI4Math 技能仓库开始：论文阅读、优化、计算数学、Lean、SageMath 或论文写作。</span></p>
      </div>
      <div class="vm-card vm-route">
        <h3><span class="lang-en">Run a Research Project</span><span class="lang-zh">运行研究项目</span></h3>
        <p><span class="lang-en">Use <a href="https://github.com/VeryMath/co-mathematician">co-mathematician</a> when the work needs tracked goals, multiple workstreams, reviewer gates, and a final working paper.</span><span class="lang-zh">当研究需要可追踪目标、多条工作流、评审门控和最终工作论文时，使用 <a href="https://github.com/VeryMath/co-mathematician">co-mathematician</a>。</span></p>
      </div>
      <div class="vm-card vm-route">
        <h3><span class="lang-en">Browse Everything</span><span class="lang-zh">浏览全部仓库</span></h3>
        <p><span class="lang-en">Use the <a href="https://github.com/orgs/VeryMath/repositories">VeryMath repository list</a> to see the full set of public repositories and future additions.</span><span class="lang-zh">访问 <a href="https://github.com/orgs/VeryMath/repositories">VeryMath 仓库列表</a> 查看全部公开仓库和未来新增项目。</span></p>
      </div>
    </div>
  </section>

  <section class="vm-section">
    <h2><span class="lang-en">Research Workflow</span><span class="lang-zh">研究流程</span></h2>
    <p class="vm-lead">
      <span class="lang-en">The current VeryMath stack is designed around a human mathematician working with repository-aware agents. The repository keeps the process inspectable and lets research output grow from reviewed intermediate artifacts rather than transient conversation.</span>
      <span class="lang-zh">当前 VeryMath 技术栈围绕“人类数学家 + 仓库感知智能体”设计。仓库让过程可检查，也让研究成果从经过审查的中间材料中逐步生成，而不是停留在一次性对话里。</span>
    </p>
    <div class="vm-timeline">
      <div class="vm-step">
        <strong><span class="lang-en">1. Frame</span><span class="lang-zh">1. 定义问题</span></strong>
        <span><span class="lang-en">Record the research question, notation, constraints, language policy, and approved goals.</span><span class="lang-zh">记录研究问题、记号、约束、语言策略和已批准目标。</span></span>
      </div>
      <div class="vm-step">
        <strong><span class="lang-en">2. Work</span><span class="lang-zh">2. 推进工作</span></strong>
        <span><span class="lang-en">Create proof, computation, literature, and review workstreams with durable reports.</span><span class="lang-zh">创建证明、计算、文献和审查工作流，并生成可持久保存的报告。</span></span>
      </div>
      <div class="vm-step">
        <strong><span class="lang-en">3. Verify</span><span class="lang-zh">3. 验证产出</span></strong>
        <span><span class="lang-en">Use reviewer loops and completion gates before rendering a final working paper.</span><span class="lang-zh">在生成最终工作论文前，使用评审循环和完成门控进行验证。</span></span>
      </div>
    </div>
  </section>

  <section class="vm-section">
    <h2><span class="lang-en">Join the Ecosystem</span><span class="lang-zh">加入生态</span></h2>
    <p class="vm-lead">
      <span class="lang-en">VeryMath welcomes collaborators interested in AI for mathematics, formal methods, optimization, computational research, academic workflows, and open-source research tools.</span>
      <span class="lang-zh">VeryMath 欢迎关注数学 AI、形式化方法、优化、计算研究、学术工作流和开源研究工具的合作者参与。</span>
    </p>
    <div class="vm-actions">
      <a class="vm-button vm-button-primary" href="https://github.com/orgs/VeryMath/repositories"><span class="lang-en">View Repositories</span><span class="lang-zh">查看仓库</span></a>
      <a class="vm-button" href="https://github.com/VeryMath/co-mathematician/issues"><span class="lang-en">Open Issues</span><span class="lang-zh">查看议题</span></a>
    </div>
  </section>
</div>

<script>
  (function () {
    var root = document.documentElement;
    var buttons = document.querySelectorAll("[data-set-lang]");
    var title = document.getElementById("project_title");
    var tagline = document.getElementById("project_tagline");
    var saved = localStorage.getItem("vm-lang");
    var initial = saved || ((navigator.language || "").toLowerCase().indexOf("zh") === 0 ? "zh" : "en");

    function setLanguage(lang) {
      var isZh = lang === "zh";
      root.setAttribute("data-vm-lang", isZh ? "zh" : "en");
      root.setAttribute("lang", isZh ? "zh-CN" : "en");
      localStorage.setItem("vm-lang", isZh ? "zh" : "en");

      if (title) {
        title.textContent = "VeryMath";
      }
      if (tagline) {
        tagline.textContent = isZh
          ? "面向数学研究的 AI 开源生态"
          : "AI for mathematical research. Reusable, verifiable, and collaborative workflows for open mathematics.";
      }

      buttons.forEach(function (button) {
        var active = button.getAttribute("data-set-lang") === (isZh ? "zh" : "en");
        button.setAttribute("aria-pressed", active ? "true" : "false");
      });
    }

    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        setLanguage(button.getAttribute("data-set-lang"));
      });
    });

    setLanguage(initial);
  })();
</script>
