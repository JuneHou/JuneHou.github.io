---
title: "BTW: A Non-Parametric Variance Stabilization Framework for Multimodal Model Integration"
authors: "<strong>Jun Hou</strong>, Le Wang, Xuan Wang"
venue: "EMNLP 2025 Findings"
date: 2025-08-20
image: "assets/images/papers/BTW.png"
pdf: "https://openreview.net/forum?id=EXp1qDqhCk"
code: "https://github.com/JuneHou/Multimodal-Infomax-moe.git"
abstract: "Mixture-of-Experts (MoE) models have become increasingly powerful in multimodal learning by enabling modular specialization across modalities. However, their effectiveness remains unclear when additional modalities introduce more noise than complementary information. Existing approaches, such as the Partial Information Decomposition, struggle to scale beyond two modalities and lack the resolution needed for instance-level control. We propose Beyond Two-modality Weighting (BTW), a bi-level, non-parametric weighting framework that combines instance-level Kullback-Leibler (KL) divergence and modality-level mutual information (MI) to dynamically adjust modality importance during training. Our method does not require additional parameters and can be applied to an arbitrary number of modalities. Specifically, BTW computes per‐example KL weights by measuring the divergence between each unimodal and the current multimodal prediction, and modality‐wide MI weights by estimating global alignment between unimodal and multimodal outputs. Extensive experiments on sentiment regression and clinical classification demonstrate that our method significantly improves regression performance and multiclass classification accuracy."
---