---
aliases: []
hasTopic:
  - "[[Algorithm]]"
  - "[[RL]]"
  - "[[PPO]]"
  - "[[IPPO]]"
  - "[[MAPPO]]"
  - "[[HPPO]]"
isA: []
Created: "[[02-07-2026]]"
---
https://marllib.readthedocs.io/en/latest/algorithm/ppo_family.html

#### IPPO
![](Images/ippo_workflow_marllib.png)
*i.e. Independent PPO*
- In IPPO, each agent has their own policy and critic, but that policy/critic model can be shared between all of the agents
- This allows for many different task types with a very similar implementation to standard PPO
- IPPO does not require information sharing, but it can be implemented if you'd like
	- **Information Sharing**: Sharing either data (obs, action, etc.), predicted data (critic value, message, etc.), or knowledge (replay buffer, model parameters, etc.)
- In IPPO, agents do not have access to the global state if they are in a partially observed setting (e.g. SAR)
#### MAPPO
![](Images/mappo_workflow_marllib.png)
*i.e. Multi-Agent PPO*
- MAPPO is built off of IPPO, but they share observations and actions so that they can coordinate tasks
	- Example of CTDE (Centralized Training, Decentralized Execution). The agents will share data, but their actions are independently controlled by their policy.
- Inputs to centralized V function is crucial because it controls the DE of the agents
- MAPPO can be conducted in parallel (since parameters are share across agents), making it similar in speed to off-policy algorithms with enough parallelization
- 
--- 
#concept 
