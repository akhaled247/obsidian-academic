---
aliases:
author: "[[Matteo De Petrillo]]"
hasTopic:
  - "[[Environment]]"
  - "[[Simulation]]"
  - "[[UGV]]"
  - "[[UAV]]"
project: "[[_BU RISE SpecRLBench]]"
publishedIn: "[[arXiv]]"
year: "[[2021]]"
Created:
  - "[[02-07-2026]]"
URL: https://arxiv.org/pdf/2102.06069
---
![[Gazebo simulation environment that reflects a highway tunnel with some obstacles.png|384]]
Simulation environment was more realistic (using Gazebo simulator)
- Included irregular models, but was essentially a cylinder cut in half and hollowed out
- Sensors included LIDAR and two cameras -- one facing upwards, and one facing forwards. This was done to map out the entire environment since it was a 3D space (by contrast, the [[SpecRLBench.. A Benchmark for Generalization in Specification-Guided Reinforcement Learning|SpecRLBench]] workspace is effectively 2.5D)
<% tp.file.cursor() %>

--- 
#source/paper 
