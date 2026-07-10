---
aliases:
  - PPO
hasTopic:
  - "[[Arxiv Insights - PPO]]"
  - "[[SpecRLBench]]"
  - "[[Algorithm]]"
  - "[[RL]]"
  - "[[PPO]]"
isA: []
Created: "[[02-07-2026]]"
---
*To learn what PPO was, I used the [Arxiv Insights](https://www.youtube.com/watch?v=5P7I-xPq8u8) channel recommended on the Stable Baselines documentation page for PPO as a reference.*
- RL relies on training data that is self-generated using the environment, which in of and itself is based on the policy that is trained by the data
- Distributions of observations and rwards are changing, causing instability
- High sensitivity to hyperparameters
- Balance between simplicity in code, tuning, sampling
- Online learning >> learns directly from environment encounters
*Policy Gradient Loss*
![365](Images/policy_gradient_loss_function.png)
pi_theta - Neural network that takes states as input and outputs actions
A_t - Advantage estimate. Estimate of relative value of selected action in current state. 
- Determine whether action taken was better/worst than expected
-A_t = Discounted Rewards (Return) - Baseline Estimate (Value)
-- Return: Weighted sum of rewards currently found with gamma that changes prioritization of immediate vs. long-term rewards. This is found after the episode is over, so we know all rewards
-- Value Function: Expectation/Estimate discounted sum of rewards from this point. Variance because it's running a neural network
- If positive advantage, increase probability of choosing this action the next time; vice versa
**Trust Region Policy Optimization**
- Make sure new policy isn't too different from old policy
- Similar to normal Policy Gradient, but instead of log() divides by the old policy
- Adds KL constraint to policy objective - Stick close to region where thing works
**Proximal Policy Optimization**
*Objective Function*
- r(theta) denotes ratio of an action being taken in new vs. old policy
-- >1 if more probable, ||<1 if less probable
-- r(theta) x A_t = TRPO
![](Images/ppo_objective_function.png)
1st term = Normal policy gradients
2nd term = Clipped version of 1st term
Minimum of these two terms is expected reward
- Limit policy gradient steepness after a single estimate unless large inverse effect from what was believed before
- E.g. if action thought to be bad but was actually good, then try to reverse previous policy. Vice versa
- But if policy was good and this sample is bad, could just be noise (optimistic)
*Loss Function*
![](Images/ppo_loss_function.png)
1st new term = Updates baseline network. Estimates average amount of discounted reward. Shares parameters with main PPO objective
2nd new term = Entropy term. Makes sure agent does enough exploration. Measures how unpredictable an outcome can be
Hyperparameters to weight the contributions of these two new terms

--- 
#concept 
