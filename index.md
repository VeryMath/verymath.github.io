---
layout: default
title: VeryMath
---

<div class="vm-page">
  <header class="vm-site-header">
    <nav class="vm-topnav" aria-label="VeryMath site navigation">
      <a class="vm-nav-brand" href="#top" aria-label="VeryMath home">
        <img class="vm-nav-logo" src="/assets/img/VeryMathlogo.jpeg" alt="">
        <span>VeryMath</span>
      </a>
      <div class="vm-nav-links" aria-label="Primary navigation">
        <a href="#workflows"><span class="lang-en">Workflows</span><span class="lang-zh">工作流</span></a>
        <a href="#repositories"><span class="lang-en">Repositories</span><span class="lang-zh">仓库</span></a>
        <a href="#use-cases"><span class="lang-en">Use Cases</span><span class="lang-zh">使用场景</span></a>
        <a href="#ecosystem"><span class="lang-en">Ecosystem / Contribute</span><span class="lang-zh">生态 / 参与</span></a>
        <a href="https://github.com/VeryMath">GitHub</a>
      </div>
      <div class="vm-language-toggle" aria-label="Language switcher">
        <button class="vm-lang-button" type="button" data-set-lang="en" aria-pressed="true">EN</button>
        <button class="vm-lang-button" type="button" data-set-lang="zh" aria-pressed="false">中文</button>
      </div>
    </nav>
  </header>

  <div id="top" class="vm-main">
    <section class="vm-hero" aria-labelledby="vm-hero-title">
      <div class="vm-hero-copy">
        <div class="vm-institution-strip" aria-label="Institution logos">
          <a class="vm-institution-link" href="https://math.ecnu.edu.cn/">
            <img class="vm-institution-logo" src="/assets/img/ecnu-math-school-logo.gif" alt="East China Normal University School of Mathematical Sciences logo">
          </a>
          <a class="vm-institution-link" href="https://klmea.ecnu.edu.cn/">
            <img class="vm-institution-logo" src="/assets/img/klmea-logo.png" alt="Key Laboratory of Mathematics and Engineering Applications, Ministry of Education logo">
          </a>
        </div>

        <p class="vm-kicker">
          <span class="lang-en">AI for Mathematical Research</span>
          <span class="lang-zh">AI 辅助数学研究</span>
        </p>
        <h1 id="vm-hero-title" class="vm-title">VeryMath</h1>
        <p class="vm-subtitle">
          <span class="lang-en">Repository-backed AI workflows for mathematical research.</span>
          <span class="lang-zh">面向数学研究的仓库式 AI 工作流。</span>
        </p>
        <p class="vm-hero-body">
          <span class="lang-en">Read papers, compute evidence, formalize proofs, and preserve research progress as verifiable artifacts.</span>
          <span class="lang-zh">让论文阅读、数学计算、形式化验证与研究写作都成为可复用、可审查、可验证的成果。</span>
        </p>
        <div class="vm-actions">
          <a class="vm-button vm-button-primary" href="https://github.com/VeryMath/co-mathematician">
            <span class="lang-en">Start a Research Project</span>
            <span class="lang-zh">启动研究项目</span>
          </a>
          <a class="vm-button" href="#repositories">
            <span class="lang-en">Explore Repositories</span>
            <span class="lang-zh">浏览仓库</span>
          </a>
        </div>
      </div>

      <div class="vm-hero-visual" aria-label="VeryMath workflow overview">
        <img src="/assets/img/VeryMath.jpg" alt="VeryMath AI for Mathematical Research overview">
        <div class="vm-dashboard-strip" aria-label="Workflow anchors">
          <span><span class="lang-en">Papers</span><span class="lang-zh">论文</span></span>
          <span><span class="lang-en">Computation</span><span class="lang-zh">计算</span></span>
          <span><span class="lang-en">Lean</span><span class="lang-zh">Lean</span></span>
          <span><span class="lang-en">Artifacts</span><span class="lang-zh">成果</span></span>
        </div>
      </div>
    </section>

    <section class="vm-trust-strip" aria-label="VeryMath principles">
      <span><span class="lang-en">Open-source</span><span class="lang-zh">开源</span></span>
      <span><span class="lang-en">Repository-backed</span><span class="lang-zh">仓库驱动</span></span>
      <span><span class="lang-en">Verifiable</span><span class="lang-zh">可验证</span></span>
      <span><span class="lang-en">Collaborative</span><span class="lang-zh">协作式</span></span>
      <span><span class="lang-en">Human-in-the-loop</span><span class="lang-zh">人机协同</span></span>
    </section>

    <section id="workflows" class="vm-section vm-workflows" aria-labelledby="vm-workflows-title">
      <div class="vm-section-head">
        <p class="vm-kicker">
          <span class="lang-en">Research Infrastructure</span>
          <span class="lang-zh">研究基础设施</span>
        </p>
        <h2 id="vm-workflows-title">
          <span class="lang-en">Workflows that leave evidence behind</span>
          <span class="lang-zh">让研究过程留下证据的工作流</span>
        </h2>
        <p class="vm-lead">
          <span class="lang-en">VeryMath is organized around durable research artifacts: notes, computations, proof obligations, reviews, and repository state that other people can inspect.</span>
          <span class="lang-zh">VeryMath 围绕可持久保存的研究成果组织工作：笔记、计算、证明义务、审查记录和可被他人检查的仓库状态。</span>
        </p>
      </div>

      <div class="vm-capability-grid">
        <article class="vm-card vm-capability">
          <span class="vm-card-index">01</span>
          <h3><span class="lang-en">Paper Reading</span><span class="lang-zh">论文阅读</span></h3>
          <p><span class="lang-en">Extract definitions, assumptions, proof structure, citation trails, and open problems from research papers.</span><span class="lang-zh">从数学论文中抽取定义、假设、证明结构、引用脉络和开放问题。</span></p>
        </article>
        <article class="vm-card vm-capability">
          <span class="vm-card-index">02</span>
          <h3><span class="lang-en">Computational Evidence</span><span class="lang-zh">计算证据</span></h3>
          <p><span class="lang-en">Turn numerical experiments, optimization routines, symbolic checks, and SageMath runs into reproducible files.</span><span class="lang-zh">将数值实验、优化流程、符号检验和 SageMath 运行整理为可复现文件。</span></p>
        </article>
        <article class="vm-card vm-capability">
          <span class="vm-card-index">03</span>
          <h3><span class="lang-en">Lean Formalization</span><span class="lang-zh">Lean 形式化</span></h3>
          <p><span class="lang-en">Connect informal arguments with formal proof workflows, theorem statements, proof repair, and verification-oriented review.</span><span class="lang-zh">连接非形式化论证、定理陈述、证明修复和面向验证的审查。</span></p>
        </article>
        <article class="vm-card vm-capability">
          <span class="vm-card-index">04</span>
          <h3><span class="lang-en">Research Automation</span><span class="lang-zh">研究自动化</span></h3>
          <p><span class="lang-en">Support long-running research through workstreams, reviewer loops, skill libraries, and final-paper gates.</span><span class="lang-zh">通过工作流、评审循环、技能库和最终论文门控支持长期研究项目。</span></p>
        </article>
      </div>
    </section>

    <section id="use-cases" class="vm-section" aria-labelledby="vm-use-cases-title">
      <div class="vm-section-head vm-section-head-row">
        <div>
          <p class="vm-kicker">
            <span class="lang-en">Task-first entry points</span>
            <span class="lang-zh">按任务进入</span>
          </p>
          <h2 id="vm-use-cases-title">
            <span class="lang-en">What do you want to do?</span>
            <span class="lang-zh">你想从哪里开始？</span>
          </h2>
        </div>
        <p class="vm-lead">
          <span class="lang-en">Start from the research task, then move into the repository that carries the workflow.</span>
          <span class="lang-zh">先从研究任务出发，再进入承载该流程的仓库。</span>
        </p>
      </div>

      <div class="vm-use-case-grid">
        <a class="vm-card vm-use-case" href="https://github.com/VeryMath/AI4Math-Paper-Reading">
          <span class="vm-use-case-label"><span class="lang-en">Read papers</span><span class="lang-zh">阅读论文</span></span>
          <span><span class="lang-en">Definitions, proof dependencies, and source-grounded notes.</span><span class="lang-zh">定义、证明依赖和基于原文的笔记。</span></span>
        </a>
        <a class="vm-card vm-use-case" href="https://github.com/VeryMath/AI4Math-Computational-Mathematics">
          <span class="vm-use-case-label"><span class="lang-en">Run computations</span><span class="lang-zh">运行计算</span></span>
          <span><span class="lang-en">Numerical, symbolic, optimization, and SageMath-backed evidence.</span><span class="lang-zh">数值、符号、优化和 SageMath 支持的证据。</span></span>
        </a>
        <a class="vm-card vm-use-case" href="https://github.com/VeryMath/AI4Math-Lean-Agents">
          <span class="vm-use-case-label"><span class="lang-en">Formalize proofs</span><span class="lang-zh">形式化证明</span></span>
          <span><span class="lang-en">Lean setup, theorem statements, proof repair, and verification.</span><span class="lang-zh">Lean 环境、定理陈述、证明修复和验证。</span></span>
        </a>
        <a class="vm-card vm-use-case" href="https://github.com/VeryMath/AI4Math-Paper-Writing">
          <span class="vm-use-case-label"><span class="lang-en">Write papers</span><span class="lang-zh">撰写论文</span></span>
          <span><span class="lang-en">Source-grounded drafting, proof obligations, and LaTeX checks.</span><span class="lang-zh">基于来源证据的写作、证明义务和 LaTeX 检查。</span></span>
        </a>
        <a class="vm-card vm-use-case vm-use-case-wide" href="https://github.com/VeryMath/co-mathematician">
          <span class="vm-use-case-label"><span class="lang-en">Start a long-running research project</span><span class="lang-zh">启动长期研究项目</span></span>
          <span><span class="lang-en">Coordinate goals, workstreams, reviews, reports, and final artifacts in one repository-aware workspace.</span><span class="lang-zh">在一个仓库感知工作区中协调目标、工作流、审查、报告和最终成果。</span></span>
        </a>
      </div>
    </section>

    <section class="vm-section vm-workflow-panel" aria-labelledby="vm-workflow-visual-title">
      <div class="vm-section-head">
        <p class="vm-kicker">
          <span class="lang-en">Workflow Map</span>
          <span class="lang-zh">流程图</span>
        </p>
        <h2 id="vm-workflow-visual-title">
          <span class="lang-en">From research question to verified artifact</span>
          <span class="lang-zh">从研究问题到可验证成果</span>
        </h2>
      </div>

      <div class="vm-flow" aria-label="Research workflow">
        <div class="vm-flow-node vm-flow-start">
          <span class="lang-en">Research Question</span>
          <span class="lang-zh">研究问题</span>
        </div>
        <div class="vm-flow-branch" aria-label="Core research tracks">
          <div class="vm-flow-node">
            <span class="lang-en">Paper Reading</span>
            <span class="lang-zh">论文阅读</span>
          </div>
          <div class="vm-flow-node">
            <span class="lang-en">Computation</span>
            <span class="lang-zh">计算实验</span>
          </div>
          <div class="vm-flow-node">
            <span class="lang-en">Lean Formalization</span>
            <span class="lang-zh">Lean 形式化</span>
          </div>
        </div>
        <div class="vm-flow-node vm-flow-wide">
          <span class="lang-en">Evidence / Reports / Proof Obligations</span>
          <span class="lang-zh">证据 / 报告 / 证明义务</span>
        </div>
        <div class="vm-flow-node">
          <span class="lang-en">Review Loop</span>
          <span class="lang-zh">审查循环</span>
        </div>
        <div class="vm-flow-node vm-flow-finish">
          <span class="lang-en">Paper / Verified Artifact / Repository</span>
          <span class="lang-zh">论文 / 可验证成果 / 仓库</span>
        </div>
      </div>
    </section>

    <section class="vm-section vm-feature" aria-labelledby="vm-feature-title">
      <div class="vm-feature-copy">
        <p class="vm-kicker">
          <span class="lang-en">Recommended entry point</span>
          <span class="lang-zh">推荐入口</span>
        </p>
        <h2 id="vm-feature-title">co-mathematician</h2>
        <p class="vm-feature-lead">
          <span class="lang-en">A repository-aware workspace for long-running mathematical research projects.</span>
          <span class="lang-zh">面向长期数学研究项目的仓库感知工作区。</span>
        </p>
        <p>
          <span class="lang-en">Use it when a project needs tracked goals, multiple workstreams, reviewer gates, durable reports, and a path toward a working paper or verified artifact.</span>
          <span class="lang-zh">当项目需要可追踪目标、多条工作流、评审门控、持久报告，并逐步形成工作论文或可验证成果时，从这里开始。</span>
        </p>
      </div>
      <div class="vm-feature-actions">
        <a class="vm-button vm-button-primary" href="https://github.com/VeryMath/co-mathematician">
          <span class="lang-en">Open co-mathematician</span>
          <span class="lang-zh">打开 co-mathematician</span>
        </a>
        <a class="vm-button" href="https://github.com/VeryMath/co-mathematician/issues">
          <span class="lang-en">View issues</span>
          <span class="lang-zh">查看议题</span>
        </a>
      </div>
    </section>

    <section id="repositories" class="vm-section" aria-labelledby="vm-repositories-title">
      <div class="vm-section-head">
        <p class="vm-kicker">
          <span class="lang-en">Repository Directory</span>
          <span class="lang-zh">仓库导览</span>
        </p>
        <h2 id="vm-repositories-title">
          <span class="lang-en">Repositories grouped by research task</span>
          <span class="lang-zh">按研究任务组织的仓库</span>
        </h2>
        <p class="vm-lead">
          <span class="lang-en">Every repository below is part of the current VeryMath public ecosystem. The groups make the entry point easier to choose without hiding the underlying GitHub projects.</span>
          <span class="lang-zh">下面每个仓库都属于当前 VeryMath 公开生态。分组只是让入口更清晰，不隐藏底层 GitHub 项目。</span>
        </p>
      </div>

      <div class="vm-repo-groups">
        <section class="vm-repo-group" aria-labelledby="repo-paper-reading">
          <h3 id="repo-paper-reading"><span class="lang-en">Paper Reading</span><span class="lang-zh">论文阅读</span></h3>
          <div class="vm-repo-list">
            <article class="vm-card vm-repo-card">
              <div class="vm-repo-head">
                <h4><a href="https://github.com/VeryMath/AI4Math-Paper-Reading">AI4Math-Paper-Reading</a></h4>
                <a class="vm-repo-link" href="https://github.com/VeryMath/AI4Math-Paper-Reading">GitHub</a>
              </div>
              <p><span class="lang-en">Structured workflows for reading mathematical papers, extracting proof dependencies, and turning papers into reusable AI4Math skills.</span><span class="lang-zh">用于阅读数学论文、抽取证明依赖，并将论文内容转化为可复用 AI4Math 技能的结构化流程。</span></p>
              <div class="vm-meta">
                <span class="vm-pill"><span class="lang-en">Paper Reading</span><span class="lang-zh">论文阅读</span></span>
                <span class="vm-pill"><span class="lang-en">2 skills</span><span class="lang-zh">2 个技能</span></span>
                <span class="vm-pill">MIT License</span>
              </div>
              <p class="vm-best-for"><span class="lang-en">Best for: theorem dependency analysis, source-grounded reading notes, and paper-to-skill extraction.</span><span class="lang-zh">适合：定理依赖分析、基于原文证据的阅读笔记，以及从论文抽取技能。</span></p>
            </article>
          </div>
        </section>

        <section class="vm-repo-group" aria-labelledby="repo-computation">
          <h3 id="repo-computation"><span class="lang-en">Computation &amp; Optimization</span><span class="lang-zh">计算与优化</span></h3>
          <div class="vm-repo-list">
            <article class="vm-card vm-repo-card">
              <div class="vm-repo-head">
                <h4><a href="https://github.com/VeryMath/AI4Math-Optimization">AI4Math-Optimization</a></h4>
                <a class="vm-repo-link" href="https://github.com/VeryMath/AI4Math-Optimization">GitHub</a>
              </div>
              <p><span class="lang-en">Skill packages for mathematical optimization modeling, solver setup, LP/MIP/SOCP workflows, and manifold-constrained optimization.</span><span class="lang-zh">面向数学优化建模、求解器配置、LP/MIP/SOCP 工作流和流形约束优化的技能包。</span></p>
              <div class="vm-meta">
                <span class="vm-pill"><span class="lang-en">Optimization</span><span class="lang-zh">优化</span></span>
                <span class="vm-pill"><span class="lang-en">6 skills</span><span class="lang-zh">6 个技能</span></span>
                <span class="vm-pill">MIT License</span>
              </div>
              <p class="vm-best-for"><span class="lang-en">Best for: modeling mathematical programs, selecting solvers, adapting examples, and reporting evidence from optimization runs.</span><span class="lang-zh">适合：建立数学规划模型、选择求解器、改写示例，以及汇报优化运行证据。</span></p>
            </article>

            <article class="vm-card vm-repo-card">
              <div class="vm-repo-head">
                <h4><a href="https://github.com/VeryMath/AI4Math-Computational-Mathematics">AI4Math-Computational-Mathematics</a></h4>
                <a class="vm-repo-link" href="https://github.com/VeryMath/AI4Math-Computational-Mathematics">GitHub</a>
              </div>
              <p><span class="lang-en">Computational workflows for numerical evidence, symbolic structure, finite element reasoning, and mathematical invariant computation.</span><span class="lang-zh">面向数值证据、符号结构、有限元推理和数学不变量计算的计算工作流。</span></p>
              <div class="vm-meta">
                <span class="vm-pill"><span class="lang-en">Computational Math</span><span class="lang-zh">计算数学</span></span>
                <span class="vm-pill"><span class="lang-en">4 skills</span><span class="lang-zh">4 个技能</span></span>
                <span class="vm-pill">MIT License</span>
              </div>
              <p class="vm-best-for"><span class="lang-en">Best for: turning mathematical objects, equations, data, or paper excerpts into reproducible computational evidence.</span><span class="lang-zh">适合：将数学对象、方程、数据或论文片段转化为可复现的计算证据。</span></p>
            </article>

            <article class="vm-card vm-repo-card">
              <div class="vm-repo-head">
                <h4><a href="https://github.com/VeryMath/AI4Math-Sagemath-skill">AI4Math-Sagemath-skill</a></h4>
                <a class="vm-repo-link" href="https://github.com/VeryMath/AI4Math-Sagemath-skill">GitHub</a>
              </div>
              <p><span class="lang-en">A SageMath skill that helps agents search SageMath documentation, write runnable SageMath Python code, execute checks, and report verified mathematical conclusions.</span><span class="lang-zh">帮助智能体检索 SageMath 文档、编写可运行 SageMath Python 代码、执行检查并汇报已验证数学结论的技能。</span></p>
              <div class="vm-meta">
                <span class="vm-pill">SageMath</span>
                <span class="vm-pill"><span class="lang-en">Computation</span><span class="lang-zh">计算</span></span>
                <span class="vm-pill">GPL</span>
              </div>
              <p class="vm-best-for"><span class="lang-en">Best for: algebra, number theory, combinatorics, symbolic computation, and SageMath-backed verification.</span><span class="lang-zh">适合：代数、数论、组合数学、符号计算，以及基于 SageMath 的验证。</span></p>
            </article>
          </div>
        </section>

        <section class="vm-repo-group" aria-labelledby="repo-formalization">
          <h3 id="repo-formalization"><span class="lang-en">Formalization &amp; Lean</span><span class="lang-zh">形式化与 Lean</span></h3>
          <div class="vm-repo-list">
            <article class="vm-card vm-repo-card">
              <div class="vm-repo-head">
                <h4><a href="https://github.com/VeryMath/AI4Math-Lean-Agents">AI4Math-Lean-Agents</a></h4>
                <a class="vm-repo-link" href="https://github.com/VeryMath/AI4Math-Lean-Agents">GitHub</a>
              </div>
              <p><span class="lang-en">Lean 4 setup, formalization, proof repair, patch review, and optional Lean-specialist backend workflows for coding agents.</span><span class="lang-zh">面向编码代理的 Lean 4 环境配置、形式化、证明修复、补丁审查和可选 Lean 专家后端流程。</span></p>
              <div class="vm-meta">
                <span class="vm-pill">Lean 4</span>
                <span class="vm-pill"><span class="lang-en">2 skills</span><span class="lang-zh">2 个技能</span></span>
                <span class="vm-pill">MIT License</span>
              </div>
              <p class="vm-best-for"><span class="lang-en">Best for: inspecting Lean projects, preparing mathlib workspaces, repairing proofs, and validating final patches with evidence.</span><span class="lang-zh">适合：检查 Lean 项目、准备 mathlib 工作区、修复证明，并用证据验证最终补丁。</span></p>
            </article>
          </div>
        </section>

        <section class="vm-repo-group" aria-labelledby="repo-automation">
          <h3 id="repo-automation"><span class="lang-en">Research Automation</span><span class="lang-zh">研究自动化</span></h3>
          <div class="vm-repo-list">
            <article class="vm-card vm-repo-card">
              <div class="vm-repo-head">
                <h4><a href="https://github.com/VeryMath/AI4Math-Auto-Research">AI4Math-Auto-Research</a></h4>
                <a class="vm-repo-link" href="https://github.com/VeryMath/AI4Math-Auto-Research">GitHub</a>
              </div>
              <p><span class="lang-en">Agentic workflows for mathematical problem discovery, research-loop orchestration, and proof-blueprint review.</span><span class="lang-zh">面向数学问题发现、研究循环编排和证明蓝图审查的智能体工作流。</span></p>
              <div class="vm-meta">
                <span class="vm-pill"><span class="lang-en">Auto Research</span><span class="lang-zh">自动研究</span></span>
                <span class="vm-pill"><span class="lang-en">3 skills</span><span class="lang-zh">3 个技能</span></span>
                <span class="vm-pill">MIT License</span>
              </div>
              <p class="vm-best-for"><span class="lang-en">Best for: turning broad mathematical intent into structured problems, bounded research runs, and reviewed proof plans.</span><span class="lang-zh">适合：将宽泛的数学意图转化为结构化问题、有边界的研究运行和经过审查的证明计划。</span></p>
            </article>

            <article class="vm-card vm-repo-card">
              <div class="vm-repo-head">
                <h4><a href="https://github.com/VeryMath/AI4Math-Evolving">AI4Math-Evolving</a></h4>
                <a class="vm-repo-link" href="https://github.com/VeryMath/AI4Math-Evolving">GitHub</a>
              </div>
              <p><span class="lang-en">Agent-led workflows for iterative mathematical experiments, OpenEvolve runs, evaluation loops, and skill refinement.</span><span class="lang-zh">由智能体驱动的迭代数学实验、OpenEvolve 运行、评估循环和技能改进流程。</span></p>
              <div class="vm-meta">
                <span class="vm-pill"><span class="lang-en">Evolving Research</span><span class="lang-zh">演化研究</span></span>
                <span class="vm-pill"><span class="lang-en">1 skill</span><span class="lang-zh">1 个技能</span></span>
                <span class="vm-pill">MIT License</span>
              </div>
              <p class="vm-best-for"><span class="lang-en">Best for: bounded experiment sessions, metric review, short probes, and next-step iteration.</span><span class="lang-zh">适合：有边界的实验会话、指标审查、短探测和下一步迭代。</span></p>
            </article>
          </div>
        </section>

        <section class="vm-repo-group" aria-labelledby="repo-writing">
          <h3 id="repo-writing"><span class="lang-en">Writing &amp; Artifacts</span><span class="lang-zh">写作与成果</span></h3>
          <div class="vm-repo-list">
            <article class="vm-card vm-repo-card">
              <div class="vm-repo-head">
                <h4><a href="https://github.com/VeryMath/AI4Math-Paper-Writing">AI4Math-Paper-Writing</a></h4>
                <a class="vm-repo-link" href="https://github.com/VeryMath/AI4Math-Paper-Writing">GitHub</a>
              </div>
              <p><span class="lang-en">Source-grounded workflows for mathematical paper drafting, proof-obligation review, and submission-ready LaTeX checks.</span><span class="lang-zh">基于来源证据的数学论文写作、证明义务审查和投稿级 LaTeX 检查流程。</span></p>
              <div class="vm-meta">
                <span class="vm-pill"><span class="lang-en">Paper Writing</span><span class="lang-zh">论文写作</span></span>
                <span class="vm-pill"><span class="lang-en">1 skill</span><span class="lang-zh">1 个技能</span></span>
                <span class="vm-pill">MIT License</span>
              </div>
              <p class="vm-best-for"><span class="lang-en">Best for: converting verified materials into paper text and review artifacts without losing source evidence.</span><span class="lang-zh">适合：在不丢失来源证据的前提下，将已验证材料转化为论文文本和审查材料。</span></p>
            </article>
          </div>
        </section>

        <section class="vm-repo-group" aria-labelledby="repo-long-running">
          <h3 id="repo-long-running"><span class="lang-en">Long-running Research</span><span class="lang-zh">长期研究</span></h3>
          <div class="vm-repo-list">
            <article class="vm-card vm-repo-card vm-repo-card-featured">
              <div class="vm-repo-head">
                <h4><a href="https://github.com/VeryMath/co-mathematician">co-mathematician</a></h4>
                <a class="vm-repo-link" href="https://github.com/VeryMath/co-mathematician">GitHub</a>
              </div>
              <p><span class="lang-en">A repository-backed mathematical research workspace for coding agents, designed to make goals, messages, workstreams, reports, reviews, and final papers durable.</span><span class="lang-zh">一个由仓库承载的数学研究工作区，面向编码代理，让目标、消息、工作流、报告、审查和最终论文都可以持久保存。</span></p>
              <div class="vm-meta">
                <span class="vm-pill"><span class="lang-en">Research Workspace</span><span class="lang-zh">研究工作区</span></span>
                <span class="vm-pill">Python</span>
                <span class="vm-pill">MIT License</span>
              </div>
              <p class="vm-best-for"><span class="lang-en">Best for: starting a long-running AI-assisted math project and coordinating the other AI4Math skill repositories inside a reviewed workflow.</span><span class="lang-zh">适合：启动长期 AI 辅助数学研究项目，并在经过审查的流程中协调其他 AI4Math 技能仓库。</span></p>
            </article>
          </div>
        </section>
      </div>
    </section>

    <section id="ecosystem" class="vm-section vm-ecosystem" aria-labelledby="vm-ecosystem-title">
      <div class="vm-section-head">
        <p class="vm-kicker">
          <span class="lang-en">Open ecosystem</span>
          <span class="lang-zh">开放生态</span>
        </p>
        <h2 id="vm-ecosystem-title">
          <span class="lang-en">Build with VeryMath</span>
          <span class="lang-zh">参与 VeryMath</span>
        </h2>
        <p class="vm-lead">
          <span class="lang-en">VeryMath welcomes collaborators interested in AI for mathematics, formal methods, optimization, computational research, academic workflows, and open-source research tools.</span>
          <span class="lang-zh">VeryMath 欢迎关注数学 AI、形式化方法、优化、计算研究、学术工作流和开源研究工具的合作者参与。</span>
        </p>
      </div>

      <div class="vm-ecosystem-grid">
        <a class="vm-card vm-ecosystem-link" href="https://github.com/VeryMath">
          <strong><span class="lang-en">GitHub organization</span><span class="lang-zh">GitHub 组织</span></strong>
          <span><span class="lang-en">Browse public repositories and follow new VeryMath projects.</span><span class="lang-zh">浏览公开仓库并关注新的 VeryMath 项目。</span></span>
        </a>
        <a class="vm-card vm-ecosystem-link" href="https://github.com/orgs/VeryMath/repositories">
          <strong><span class="lang-en">Related repositories</span><span class="lang-zh">相关仓库</span></strong>
          <span><span class="lang-en">See the complete repository list on GitHub.</span><span class="lang-zh">在 GitHub 查看完整仓库列表。</span></span>
        </a>
        <a class="vm-card vm-ecosystem-link" href="https://github.com/VeryMath/co-mathematician/issues">
          <strong><span class="lang-en">Contribute</span><span class="lang-zh">参与贡献</span></strong>
          <span><span class="lang-en">Start with open issues and repository-specific discussion in GitHub.</span><span class="lang-zh">从开放议题和 GitHub 仓库讨论开始参与。</span></span>
        </a>
      </div>
    </section>
  </div>
</div>
