---
layout: default
title: Status
---

# Video
[embeded Youtube link here](a minimum resolution of 1200 × 720 (i.e. 720p))

# Project Summary
Our project is a downhill survival game in the Minecraft, which asks the player to go down the map as many levels as possible within limited steps. The agent is able to look down five floors in order to determine the next step. Once the player reaches the bottom of the map, the map will be regenerated. Rewards are given for each level the player goes down, and penalties are applied for touching the map boundary and dropping more than five levels at a time.

# Approach
Different from path searching game and item collecting game, we are trying to build up a universal stratgy that can deal with randomized map. Currently, we are implementing the game based on Q-network with pytouch, and the map is build based on the most basic needs. Instead of making a 3D map, our initial map is a 2D version while the player can either go left or right. Rewards and Penalties are applied through XML and loss functions.
The perfomance our fist model is largely depend on the weight of rewards and penalities, and we have found a reasonable value for those feedbacks. The folllowing result is our first 'successful' try.

![image]()

# Evaluation
The most obvious way to evaluate the performance of our model is the levels the player goes down within limited steps, however, we noticed the player wasted a huge amount of steps on turning around and move toward the boundry of our map. In order to get a more reasonable evaluation, we implemented penalty when player move toward the boundry. While random steps may cause the player goes toward the boundry, our player has learned to avoid stuck on such actions. The folloing plot is a comparesion of results before and after the penalty is implemented.
![image]()
![image]()


# Remaining Goals and Challenges
Even though out model is opreating normally, we think it can do better than that. Sometimes the player will turn around on the first level and stuck there, and we believe there is something wrong with the rating for each possible move. Modifing the training function with more weighted parameters might be helpful in this situation. The rewards and penalities can me further improved but we might need a bit more time on testing different combinations. The loss function is a another potential problem while our model gives huge loss values over five thousand while our rewards was set to five points per level.
One of the frustrating part in our project is we waste a lot of time setting up our linux environment and realized there is barely no improvement on the speed of out model limited bu Malmo, and some functions works really wired in Malmo like you have to add .5 on the player's x and z coordinates in order to make 'move' command funcional.  

# Resources Used
We used Deep Q-network in homework 2 and modified to fit in our game. Pytouch is used and greedy algorithm is added in our network.
