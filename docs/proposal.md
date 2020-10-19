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

In our project, the agent will be born at the top of the building. The agent may not use Greedy search or A* search to analyze the next movement but using them to perceive the surrounding environments. For different actions the agent taken, deep Q learning will record its rewards for enhancing the next prediction. 


## Evaluation Plan
### 1.Quantitative Metrics

A successful learning AI will reach the bottom of the building with maximum HP. Two ways to drop agent's HP. 
- Minimum fall-down damage. The agent is not allowed to descend over five floors once, and it is expected to descend within a safe height for higher HP. 
- Minimum time punishment. It avoids the agent not staying on the same floor for too much time.
We will mainly concern the quantitative metrics that try to convert all potential delays or accidents into numerical deduction from the agent's health points.

### 2. Qualitative
We could observe an impressive increment of downhill depths, a decrement of travel time, and an increment of rest HP according to an increment of generation times. We expect to see a perfect training with no fall injury and time punishment.


## Appointment with the Instructor
3:15pm - 3:30pm, Thursday, October 22, 2020