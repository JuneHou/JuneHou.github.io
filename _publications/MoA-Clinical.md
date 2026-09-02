---
title: "Role-Specialized Mixture-of-Agents with Open-Weight LLMs for Clinical Prediction"
authors: "<strong>Jun Hou</strong>, Yi Fang, Xuan Wang"
venue: "COLM 2026 DAIH Workshop"
date: 2026-07-24
image: "assets/images/papers/MoA-Clinical.png"
pdf: "https://arxiv.org/abs/2608.22176"
code: "https://github.com/JuneHou/moa-clinical-rag"
abstract: "Large Language Models (LLMs) are increasingly applied to clinical prediction tasks such as in-hospital mortality and readmission from electronic health records (EHRs). Privacy and compliance constraints motivate systems that can be deployed locally, which has increased interest in open-weight multi-agent designs. However, most medical multi-agent systems are evaluated as a single block, leaving unclear which agent role contributes to prediction and whether retrieval drives observed gains. We study a role-specialized Mixture-of-Agents (MoA) that combines medical knowledge retrieval with contrastive similar-patient reasoning. By varying the role design while holding the retrieval setup fixed, we localize the main effect to the final integrator. Pairing large open-weight analysts with a small open-weight integrator matches closed-model prompting on F1 for mortality prediction while flagging substantially more true high-risk patients. Mechanism analysis shows the role assignment directly yields a high-recall operating point without threshold tuning. The effect is task-dependent, with smaller gains for readmission because the available records correlate weakly with this longer-horizon outcome. These results position role design as a key factor in privacy-constrained, training-free clinical LLM prediction."
---
