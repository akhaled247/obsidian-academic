---
aliases:
  - Foundational Paper
  - SpecRLBench
  - Main Paper
author: Zijian Guo
hasTopic:
  - "[[SpecRLBench]]"
project: "[[BU RISE SpecRLBench]]"
publishedIn: "[[arXiv]]"
year: "[[2026]]"
Created:
  - <% tp.file.include("[[templates/timestamp note]]") %>
URL: https://arxiv.org/pdf/2604.24729v1
---
> [!Abstract]- 
> Specification-guided reinforcement learning (RL) provides a principled framework for encoding complex, temporally extended tasks using formal specifications such as linear temporal logic (LTL). While recent methods have shown promising results, their ability to generalize across unseen spec- ifications and diverse environments remains insufficiently understood. In this work, we introduce SpecRLBench, a benchmark designed to evaluate the generalization capabilities of LTL-based specification-guided RL methods. The benchmark spans multiple difficulty levels across naviga- tion and manipulation domains, incorporating both static and dynamic environments, diverse robot dynamics, and varied observation modalities. Through extensive empirical evaluation, we charac- terize the strengths and limitations of existing approaches and reveal the challenges that emerge as specification and environment complexity increase. SpecRLBench provides a structured plat- form for systematic comparison and supports the development of more generalizable specification- guided RL methods. Code is available at https://github.com/BU-DEPEND-Lab/SpecRLBench
<%tp.file.cursor()%>
Benchmark for testing different spectulation-guided RL models (hence [[SpecRLBench.. A Benchmark for Generalization in Specification-Guided Reinforcement Learning|SpecRLBench]] name). Currently, there are 19 environments to choose from, split between **navigation** and **manipulation** tasks. I don't understand how the environments are dynamically created, so I will have to look into that.

--- 
#source/paper 
