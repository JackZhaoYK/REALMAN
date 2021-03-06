---
layout: default
title: Final
---

## Video

<div style="text-align:center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/VGK9qBBzCSE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>



## Project Summary

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In the modern world, people use autonomous robots to do some work. Autonomous vacuum robots today commonly exist in many homes, it uses sensors for obstacle detection, a new feature of cliff detection has been used as an additional sensing technology for safety. Under the development of technology, we believe that auto vacuum robots should have the ability to detect cliff and down the stairs safely. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Our project is a downhill survival game in Minecraft, which asks the agent to go down the map as many valid levels (1-5 floors) as possible and maximize the reward. The agent is able to look down five floors in order to determine the next step. Once the player reaches the bottom of the map, the map will be regenerated. Rewards are given for each level the player goes down, and penalties are applied for touching the map boundary and dropping more than five levels at a time. The agent is expected to have higher rewards for optimization (considered to be a combination of less falling damages and fewer steps). Once the player reaches the bottom of the map, the map will be regenerated. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Since the agent needs to maximize the reward which is also means to minimize the damage from falling down, and the observation for the agent is limited to five floors downward. we implemented machine learning algorithms to train the agent to find the best way to reach the bottom while take minimum damage. The picture below is a illustration of one possible outcome in our map, and we wish our agent can choose the one on the left every time to maximum reward.

<div style="text-align:center;">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="751px" viewBox="-0.5 -0.5 751 701" style="max-width:100%;max-height:701px;"><defs/><g><rect x="160" y="60" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="330" y="140" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="200" y="220" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="40" y="300" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="120" y="380" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="265" y="460" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><path d="M 200 60 Q 300 -10 330 50 Q 360 110 367.99 133.96" fill="none" stroke="#30d158" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 369.65 138.94 L 364.11 133.41 L 367.99 133.96 L 370.75 131.19 Z" fill="#30d158" stroke="#30d158" stroke-miterlimit="10" pointer-events="all"/><path d="M 200 60 Q 300 10 261.19 213.74" fill="none" stroke="#30d158" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 260.21 218.9 L 258.08 211.37 L 261.19 213.74 L 264.96 212.68 Z" fill="#30d158" stroke="#30d158" stroke-miterlimit="10" pointer-events="all"/><path d="M 200 60 Q 80 10 75 120 Q 70 230 79.1 293.7" fill="none" stroke="#30d158" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 79.84 298.89 L 75.39 292.46 L 79.1 293.7 L 82.32 291.47 Z" fill="#30d158" stroke="#30d158" stroke-miterlimit="10" pointer-events="all"/><path d="M 200 60 Q 180 20 155 30 Q 130 40 135 115 Q 140 190 159.33 373.67" fill="none" stroke="#30d158" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 159.88 378.89 L 155.67 372.29 L 159.33 373.67 L 162.63 371.56 Z" fill="#30d158" stroke="#30d158" stroke-miterlimit="10" pointer-events="all"/><path d="M 200 60 Q 280 20 305 110 Q 330 200 325.12 453.63" fill="none" stroke="#30d158" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 325.02 458.88 L 321.66 451.82 L 325.12 453.63 L 328.66 451.95 Z" fill="#30d158" stroke="#30d158" stroke-miterlimit="10" pointer-events="all"/><ellipse cx="205" cy="7.5" rx="7.5" ry="7.5" fill="#5e5ce6" stroke="#000000" pointer-events="all"/><path d="M 205 15 L 205 40 M 205 20 L 190 20 M 205 20 L 220 20 M 205 40 L 190 60 M 205 40 L 220 60" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/><rect x="390" y="110" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 120px; margin-left: 391px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#30d158">Level 1</font></div></div></div></foreignObject><text x="415" y="124" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 1</text></switch></g><rect x="190" y="190" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 200px; margin-left: 191px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#30d158">Level 2</font></div></div></div></foreignObject><text x="215" y="204" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 2</text></switch></g><rect x="0" y="260" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 270px; margin-left: 1px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#30d158">Level 3</font></div></div></div></foreignObject><text x="25" y="274" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 3</text></switch></g><rect x="170" y="350" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 360px; margin-left: 171px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#30d158">Level 4</font></div></div></div></foreignObject><text x="195" y="364" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 4</text></switch></g><rect x="340" y="420" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 430px; margin-left: 341px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#30d158">Level 5</font></div></div></div></foreignObject><text x="365" y="434" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 5</text></switch></g><rect x="520" y="60" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="620" y="140" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="620" y="220" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="650" y="380" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="625" y="460" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><ellipse cx="565" cy="7.5" rx="7.5" ry="7.5" fill="#5e5ce6" stroke="#000000" pointer-events="all"/><path d="M 565 15 L 565 40 M 565 20 L 550 20 M 565 20 L 580 20 M 565 40 L 550 60 M 565 40 L 580 60" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/><rect x="700" y="110" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 120px; margin-left: 701px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#30d158">Level 1</font></div></div></div></foreignObject><text x="725" y="124" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 1</text></switch></g><rect x="700" y="190" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 200px; margin-left: 701px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#30d158">Level 2</font></div></div></div></foreignObject><text x="725" y="204" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 2</text></switch></g><rect x="700" y="270" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 280px; margin-left: 701px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#30d158">Level 3</font></div></div></div></foreignObject><text x="725" y="284" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 3</text></switch></g><rect x="700" y="350" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 360px; margin-left: 701px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#30d158">Level 4</font></div></div></div></foreignObject><text x="725" y="364" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 4</text></switch></g><rect x="700" y="430" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 440px; margin-left: 701px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#30d158">Level 5</font></div></div></div></foreignObject><text x="725" y="444" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 5</text></switch></g><rect x="590" y="300" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="470" y="540" width="80" height="20" fill="#5e5ce6" stroke="#5e5ce6" pointer-events="all"/><rect x="570" y="540" width="50" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 48px; height: 1px; padding-top: 550px; margin-left: 571px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; "><font color="#ff453a">Level 6</font></div></div></div></foreignObject><text x="595" y="554" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Level 6</text></switch></g><path d="M 560 60 Q 480 10 470 140 Q 460 270 489.3 533.67" fill="none" stroke="#ff453a" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 489.88 538.89 L 485.62 532.32 L 489.3 533.67 L 492.58 531.55 Z" fill="#ff453a" stroke="#ff453a" stroke-miterlimit="10" pointer-events="all"/><path d="M 155.36 668.37 C 156.27 664.99 158.54 662.17 161.62 660.6 C 164.69 659.04 168.28 658.88 171.48 660.17 C 176.13 662.47 179.74 666.51 181.55 671.45 C 189.86 647.41 202.49 625.16 218.81 605.83 C 223.44 601.55 229.91 600 235.93 601.73 C 237.47 601.98 238.77 603.01 239.39 604.47 C 240 605.93 239.84 607.6 238.95 608.91 C 216.77 634.4 200.28 664.48 190.61 697.08 C 184.91 700 178.18 700 172.48 697.08 C 168.18 687.34 162.4 678.35 155.36 670.42 C 155 669.79 155 669.01 155.36 668.37 Z" fill="#30d158" stroke="#30d158" stroke-miterlimit="10" pointer-events="all"/><path d="M 520 600 L 549.17 600 L 570 629.59 L 590.83 600 L 620 600 L 584.58 650 L 620 700 L 590.83 700 L 570 670.41 L 549.17 700 L 520 700 L 553.33 650 Z" fill="#ff453a" stroke="#ff453a" stroke-miterlimit="10" pointer-events="all"/></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://desk.draw.io/support/solutions/articles/16000042487" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Viewer does not support full SVG 1.1</text></a></switch></svg>
<br>
<em>Fig.1: Expected agent's behavior</em></div>



## Approaches

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Throughout the project process, we iterated a variety of algorithms and reward models, and the results obtained were also completely different.

### 0. DQN
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The first approach we tried was using Deep Q-network(DQN) and a completely randomized map as our environment, different rewards are given when the agent getting down the hill, reaching the bottom, or touching the map boundry. 
<br>
<p style="text-align:center;">
    <img src="./img/DQNF1.png" height="75%" width="75%"/>
    <br>
    <em>Fig. 2: Falling Rward Function</em>
</p>
<br>
<p style="text-align:center;">
    <img src="./img/DQNF2.png"  height="75%" width="75%"/>
    <br>
    <em>Fig.3: Rward Functions in DQN Model</em>
</p>
<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DQN gives a very clear result that the agent was learning to go down the hill gradually. However, DQN runs quite unstably so we have to make the agent wait for a second or two to wait for the result to come, otherwise, the agent will choose a step randomly. It took us a lot of time experimenting with different weights for rewards, and the result was not significantly improved. With DQN as our baseline, we want the agent to do better.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After brainstorming about the situation, we decided to go with PPO(Proximal Policy Optimization) with rllib and ray to make a multi-agent environmeant. Running multiple agents parallel can significantly increase our training speed because there are more episodes being trained at the same time, and we don’t have to wait for seconds each step since PPO uses sampling to determine the weight of the following steps.


### 1. PPO
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PPO provides a more stable result compare to the Deep Q-network but at a cost of more training steps required. Initially, we used continuous movement in our environment, but the agent will still moving when they are supposed to stop the movement for one second in some cases. So we decided to use discrete movement instead. After adjusting all kinds of parameters like "sample_batch_size", "lr" and "evaluation_num_episodes", we wish our learning speed can be accelerated a bit more. 
<br>
```python
trainer = ppo.PPOTrainer(env=DiamondCollector, config={
    'env_config': {},           # No environment parameters to configure
    'framework': 'torch',       # Use pyotrch instead of tensorflow
    'num_gpus': 0.03,              # We aren't using GPUs now
    'num_workers': 0,              # We aren't using parallelism now
    "train_batch_size": 500,       # shrink bacth size for more learnings
    "lr":0.001
})
```
<em>Code. 1: Parameter tuning for PPO trainer</em>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After discussing with our TA, we shrink our observation space from a vector that contains 4000 elements to a vector that only contains 735 elements, and we removed the reward when the agent reaching the bottom since there is no limit on steps the agent can use and it makes the agent less sensitive to the falling reward. At the meantime, we increased the reward for each level the agent manages to get down, which would stimulate the agent to jump more floors as it can. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bugs are being fixed like miscalculating rewards while the agent is in the air by using the algorithm below. In specific, we obtained the agent position twice in a single step to calculate the difference. If the agent is falling, the position difference will be passed to our falling functin for next reward calculation.

```python
time.sleep(0.1)
self.obs, self.temp_pos = self.get_observation(world_state)
while self.temp_pos!=self.cur_pos:
    time.sleep(0.2)
    self.obs, self.cur_pos = self.get_observation(world_state)
    time.sleep(0.1)
    self.obs, self.temp_pos = self.get_observation(world_state)

reward = 0
if self.cur_pos[1] < 3:
    self.reached = True

reward += self.falling_reward(self.cur_pos, self.prev_pos)
self.prev_pos = self.cur_pos
```

*Code. 2: Locating the agent in the air*

<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The log frequency was adjusted a few times to show the trend of improvement, and that part is displayed in the video.

### 2. PPO Extension
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We found that using PPO with parallelism could save us a lot of time for training because it merge contribution of each worker for each time of learning. However, due to ability of our PCs, the performance of multiple workers was worse than that of a single worker.

### 3. Map setup
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In out first version of the game, we used 2D map as our environment for efficient implementation. However, since we want to let the agent learn a universial strategy against all kinds of map, we upgraded to a 3D map. Each stair is a 2x2 square, and we made sure each level has three stairs which allows the agent won't encounter a situation where all possible ways lead to a negative reward. Agent are free to move in four directions.
<br>
<p style="text-align:center;">
    <img src="./img/possibility.png"  height="75%" width="75%"/>
    <br>
    <em>Fig. 4: Chance of meeting cliffs</em>
</p>
<br>



## Evaluation

### Quantitative Method
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Evaluating the performance for our project is fairly simple, just calculate the reward the agent successfully goes down minus the damage it takes in the process. Based on the need of our model, we have adjusted the weight several times. The quantitative measure would be the final score the agent gets. In that case, rewards are given for each level the player goes down and a dynamic reward is given based on the number of levels the agent gets down. Below is our reward function and the reward is increased for each additional level it falls. Once the agent goes beyond five floors, a negative reward is given.

<br>

```python
def falling_reward(self, cur, prev):
    falldown = prev[1] - cur[1]

    return -15 if falldown >= 15 else math.ceil(falldown*falldown/10)
```
*Code. 3: Reward function*
<br>
<p style="text-align:center;">
    <img src="./img/rewardFunction.png"  height="75%" width="75%"/>
    <br>
    <em>Fig. 5: Current reward function for PPO Model</em>
</p>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Other than the penalty of dropping more than five floors, repeatedly touching the map boundary will result in a negative reward as the following XML code. Since the agent has its height, every time it touches the boundary will result in touching two glass blocks, so we change the negative reward to -1 in our reward function.
<br>
<br>

```python
...
<Block type="glass" reward="-0.3"/>
...

...
if r.getValue() < 0:
                reward += -1
...
```
*Code. 4: Penalty of touching boundary*

### Qualitative Method

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Another qualitative measure is that the agent is expected to have higher rewards as more training are performed, and higher reward means less falling damage and more valid floor drops. After thousands of episodes, we can see our agent stopped repeatedly touching the boundry and started to choose a path that gives higher rewards. Here is the reward graph we get that can show our agent is getting smarter as training goes on.
<br>

<div style="text-align:center;"><img src="./img/final_trend.jpg" alt="image"></div>



<div style="text-align:center;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="107px" viewBox="-0.5 -0.5 107 111"  style="max-width:100%;max-height:111px;"><defs/><g><path d="M 11 0 L 21 0 L 21 90.5 L 31.5 90.5 L 16 109.5 L 0.5 90.5 L 11 90.5 Z" fill="#30d158" stroke="#000000" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/><rect x="26" y="30" width="80" height="20" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 40px; margin-left: 27px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">Change data frequency</div></div></div></foreignObject><text x="66" y="44" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Change data f...</text></switch></g></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://desk.draw.io/support/solutions/articles/16000042487" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Viewer does not support full SVG 1.1</text></a></switch></svg>
</div>

<div style="text-align:center;"><img src="./img/freq50Trend.png" alt="image"><br>
<em>Fig. 6: Graph of qualitative result</em></div>
<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In addition to the reward graph, we also graph the loss function as following. It shows that there are always a decreased trend when getting high loss function. We think the problem happens because of the ability of our PCs. We find that PPO needs more time for each step than DQN for better result. If there are enough learning times and enough steps, the return value will be better.

<p style="text-align:center;">
    <img src="./img/2total_loss.png"  height="60%" width="60%"/>
    <br>
    <em>Fig. 7: Graph of loss function result</em>
</p>
<br>



## References

#### [XML Schema Documentation](http://microsoft.github.io/malmo/0.14.0/Schemas/MissionHandlers.html)

#### [Project Malmo](https://github.com/microsoft/malmo)

#### [TA Kolby Nottingham's Code for Assignment 2 with RLlib](https://campuspro-uploads.s3.us-west-2.amazonaws.com/ad12d7f8-a456-4244-bd96-18be6a728aca/662f51cc-2587-4f7f-b5af-a59aff45727c/assignment2_rllib_cont.py)

#### [Proximal Policy Optimization (PPO) in RLlib in Ray](https://docs.ray.io/en/latest/rllib-algorithms.html#ppo)

