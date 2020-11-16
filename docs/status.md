---
layout: default
title: Status
---
## Video
### REALMAN Status Report Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/aYoLBZaDmwU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### REALMAN Machine Learning 150x speed
<iframe width="560" height="315" src="https://www.youtube.com/embed/NWoSBVhXOpY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Project Summary
In the modern world, people use autonomous robots to do some work. Autonomous vacuum robots today commonly exist in many homes, it uses sensors for obstacle detection, a new feature of cliff detection has been used as an additional sensing technology for safety. Under the development of technology, we believe that auto vacuum robots should have the ability to detect cliff and down the stairs safely. Our project is a downhill survival game in Minecraft, which asks the agent to go down the map as many levels as possible within limited steps. The agent is able to look down five floors in order to determine the next step. Once the player reaches the bottom of the map, the map will be regenerated. Rewards are given for each level the player goes down, and penalties are applied for touching the map boundary and dropping more than five levels at a time. The agent is expected to have higher rewards for optimization (considered to be a combination of less falling damages and fewer steps).

## Approach
### Methodology
Different from path searching game and item collecting game, we are trying to build up a universal strategy that can deal with a randomized map. Currently, we are implementing the game based on Q-network with PyTorch, and the map is build based on the most basic needs. Where we need a map that is easy to observe and achievable for AI training. Therefore, instead of making a 3D map, our initial map is a 2D version while the player can either go left or right. Rewards and Penalties are also applied through XML and loss functions. Where the rewards are the reward of doing downhill effectively and the reward of achieving goals, the penalties are the penalty of moving toward the boundary and of falling over five floors. The performance of our fist model is largely dependent on the weight of rewards and penalties, and we have found a reasonable value for those feedbacks. 

### Realization And Problems
The following result is our first ‘successful’ try. However, the graph of the training result still has some problems.
![result_image](https://github.com/JackZhaoYK/REALMAN/blob/main/docs/img/returns.png?raw=true)
- First, it doesn't have a continuously ascending trend, which could be resulted in the setting of difficulties in our game. We may need to create more complicated challenges for our AI agent. 
- Second, it doesn't have a stable reward value range, everything looks a little bit random, we think the problem could be the setting value of rewards and penalties. We gonna try more possible value in the next stage. 
- Third, it doesn't keep a robust status of doing powerful calculations in the last third part. We believe that there must be a great space for optimization and improvement.



## Remaining Goals and Challenges
Even though out model is opreating normally, we think it can do better than that. Sometimes the player will turn around on the first level and stuck there, and we believe there is something wrong with the rating for each possible move. Modifing the training function with more weighted parameters might be helpful in this situation. The rewards and penalities can me further improved but we might need a bit more time on testing different combinations. The loss function is a another potential problem while our model gives huge loss values over five thousand while our rewards was set to five points per level.

One of the frustrating part in our project is we waste a lot of time setting up our linux environment and realized there is barely no improvement on the speed of out model limited bu Malmo, and some functions works really wired in Malmo like you have to add .5 on the player's x and z coordinates in order to make 'move' command funcional.  

## Resources Used
We used Deep Q-network in homework 2 and modified to fit in our game. Pytouch is used and greedy algorithm is added in our network.
