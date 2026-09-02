---
title: "EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems"
authors: "<strong>Jun Hou</strong>, Priya Pitre, Yi Fang, Xuan Wang"
venue: "EMNLP 2026 Findings"
date: 2026-08-30
image: "assets/images/papers/EDGE.png"
pdf: "https://arxiv.org/abs/2609.01360"
code: "https://github.com/JuneHou/EDGE"
abstract: "Large language model (LLM) agent failures often contain multiple related errors rather than a single mistake. Existing attribution methods usually identify a responsible agent, step, or root cause, but do not explicitly model dependency between errors. We introduce EDGE, an Error Dependency Graph-guided multi-Error attribution framework. EDGE constructs an error dependency graph from observed error events and validates a reliable causal subset through counterfactual rollout. The inference graph guides a two-stage LLM-as-judge detector for error attribution, and the intervention-validated subgraph provides a more reliable basis for explanation and repair analysis. Experiments on TRAIL and MAST show that EDGE improves category-level multi-error attribution across most evaluated models and settings. Experiments with adapted Who&When-style prompts show that the graph helps across prompting strategies. These results suggest that dependency structure is a useful diagnostic prior for agent failures beyond isolated root-cause prediction."
---
