---
layout: default
title: Proposal 
---

## Summary of the Project

Our project will be a downhill survival game in the Minecraft, which will simulate a one-hundred-floor building with obstacles. Our scenario will begin with the agent on the 100th floor and the agent is not allowed to move down over five floors once. The goal will be to keep alive and navigate down to the first floor. The agent would choose the best way to navigate down with minimum damage and the minimum time based on the observation. The potential application would be the danger alert system for robots, any type of cars, etc.



## AI/ML Algorithms
- Deep Q-Learning (Reinforcement Learning)
- Greedy Algorithm
- A* Search Algorithm

In our project, the agent will be borned at the top of the building. The agent may not use greedy search or A* search to analysis next movement but using them to  percieve the surrounding environments. For different actions the agent taken, deep Q learnig will record its rewards for enhancing next prediction. 


## Evaluation Plan
### 1.Quantitative Metrics

A successful learning AI will reach the bottom of the building with maximum HP. Two ways to drop agent's HP. 
- Minimum fall down damage. The agent is not allowed to descend over five floors once, and it is expected to descend within a safe height for higher HP. 
- Minimum time punishment. It avoids the agent not staying at a same floor with too much time.
We will mainly concern the quantitative metrics that try to convert all potential delays or accitdents into numerical deduction from agent's health points.

### 2. Qualitative
We could observe impressive increment of downhill depths, decrement of travel time, and increment of rest HP according to increment of generation times. We expect to see a perfect training with no fall injury and time punishment.


## Appointment with the Instructor
3:15pm - 3:30pm, Thursday, October 22, 2020