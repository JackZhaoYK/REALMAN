try:
    from malmo import MalmoPython
except:
    import MalmoPython

import os
import sys
import time
import json
import random
from tqdm import tqdm
from collections import deque
import matplotlib.pyplot as plt 
import numpy as np
from numpy.random import randint

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

cur_reward = 0
# prev_position = 
# Hyperparameters
SIZE = 50
REWARD_DENSITY = .1
PENALTY_DENSITY = .02
OBS_SIZE = 20
MAX_EPISODE_STEPS = 200
MAX_GLOBAL_STEPS = 20000
REPLAY_BUFFER_SIZE = 10000
EPSILON_DECAY = .999
MIN_EPSILON = .1
BATCH_SIZE = 128
GAMMA = .9
TARGET_UPDATE = 100
LEARNING_RATE = 1e-4
START_TRAINING = 500
LEARN_FREQUENCY = 1
ACTION_DICT = {
    0: 'move 1',  # Move one block forward
    1: 'turn 1',  # Turn 90 degrees to the right
    2: 'turn -1',  # Turn 90 degrees to the left
}


# Q-Value Network
class QNetwork(nn.Module):
    #------------------------------------
    #
    #   TODO: Modify network architecture
    #
    #-------------------------------------

    def __init__(self, obs_size, action_size, hidden_size=100):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(np.prod(obs_size), hidden_size),
                                 nn.ReLU(),
                                 nn.Linear(hidden_size, action_size)) 
        
    def forward(self, obs):
        """
        Estimate q-values given obs

        Args:
            obs (tensor): current obs, size (batch x obs_size)

        Returns:
            q-values (tensor): estimated q-values, size (batch x action_size)
        """
        batch_size = obs.shape[0]
        obs_flat = obs.view(batch_size, -1)
        return self.net(obs_flat)


def GetMissionXML():
    #------------------------------------
    #
    #   TODO: Spawn diamonds
    #   TODO: Spawn lava
    #   TODO: Add diamond reward
    #   TODO: Add lava negative reward
    #
    #-------------------------------------
    glass_xml = ""
    for y in range(2,202):
        for x in range(0,20):
            glass_xml+="<DrawBlock x='%d' y='%d' z='1' type='glass' />" % (x,y)
            glass_xml+="<DrawBlock x='%d' y='%d' z='3' type='glass' />" % (x,y)
            glass_xml+="<DrawBlock x='0' y='%d' z='2' type='glass' />" % (y)
            glass_xml+="<DrawBlock x='19' y='%d' z='2' type='glass' />" % (y)
    object_xml = ""
     # first block
    object_xml+="<DrawBlock x='%d' y='%d' z='2' type='diamond_ore' />" %(1,200)
    object_xml+="<DrawBlock x='%d' y='%d' z='2' type='diamond_ore' />" %(2,200)
    object_xml+="<DrawBlock x='%d' y='%d' z='2' type='diamond_ore' />" %(3,200)
    for y in range(197,4,-3):
        # for _ in range(1,19):
        x = randint(1,17)
        object_xml+="<DrawBlock x='%d' y='%d' z='2' type='diamond_ore' />" %(x,y)
        object_xml+="<DrawBlock x='%d' y='%d' z='2' type='diamond_ore' />" %(x+1,y)
        object_xml+="<DrawBlock x='%d' y='%d' z='2' type='diamond_ore' />" %(x+2,y)
    
    return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

                <About>
                    <Summary>Diamond Collector</Summary>
                </About>

                <ServerSection>
                    <ServerInitialConditions>
                        <Time>
                            <StartTime>1000</StartTime>
                            <AllowPassageOfTime>false</AllowPassageOfTime>
                        </Time>
                        <Weather>clear</Weather>
                    </ServerInitialConditions>
                    <ServerHandlers>
                        <FlatWorldGenerator generatorString="3;7,2;1;"/>
                        <DrawingDecorator>''' + \
                            "<DrawCuboid x1='0' x2='19' y1='2' y2='202' z1='1' z2='3' type='air'/>" + \
                            "<DrawCuboid x1='{}' x2='{}' y1='1' y2='1' z1='{}' z2='{}' type='lava'/>".format(-SIZE, SIZE, -SIZE, SIZE) + \
                            glass_xml + \
                            object_xml + \
                            '''<DrawBlock x='0'  y='2' z='0' type='air' />
                            <DrawBlock x='0'  y='1' z='0' type='stone' />
                        </DrawingDecorator>
                        <ServerQuitWhenAnyAgentFinishes/>
                    </ServerHandlers>
                </ServerSection>

                <AgentSection mode="Creative">
                    <Name>J</Name>
                    <AgentStart>
                        <Placement x="2.5" y="201" z="2.5" pitch="0" yaw="90"/>
                        <Inventory>
                            <InventoryItem slot="0" type="diamond_pickaxe"/>
                        </Inventory>
                    </AgentStart>
                    <AgentHandlers>
                        <ChatCommands />
                        <RewardForCollectingItem>
                            <Item reward="1" type="diamond"/>
                        </RewardForCollectingItem>
                        <RewardForTouchingBlockType>
                            <Block type="lava" reward="100"/>
                            <Block type="glass" reward="-100"/>
                        </RewardForTouchingBlockType>
                        <RewardForMissionEnd>
                            <Reward description="found_goal" reward="1000" />
                        </RewardForMissionEnd>
                        <DiscreteMovementCommands/>
                        <ObservationFromFullStats/>
                        <ObservationFromGrid>
                            <Grid name="floorAll">
                                <min x="-'''+str(OBS_SIZE)+'''" y="-14" z="-'''+str(OBS_SIZE)+'''"/>
                                <max x="'''+str(OBS_SIZE)+'''" y="0" z="'''+str(OBS_SIZE)+'''"/>
                            </Grid>
                        </ObservationFromGrid>
                        <AgentQuitFromReachingCommandQuota total="'''+str(MAX_EPISODE_STEPS)+'''" />
                        <AgentQuitFromTouchingBlockType>
                            <Block type="lava" description="found_goal"/>
                        </AgentQuitFromTouchingBlockType>
                    </AgentHandlers>
                </AgentSection>
            </Mission>'''


def falling_reward(CUR_POS, PREV_POS):
    falldown= PREV_POS[1] - CUR_POS[1] 
    return -1000 if falldown >= 15 else falldown/3

def get_action(obs, q_network, epsilon, allow_break_action):
    """
    Select action according to e-greedy policy

    Args:
        obs (np-array): current observation, size (obs_size)
        q_network (QNetwork): Q-Network
        epsilon (float): probability of choosing a random action

    Returns:
        action (int): chosen action [0, action_size)
    """
    #------------------------------------
    #
    #   TODO: Implement e-greedy policy
    #
    #-------------------------------------
    if np.random.ranf() <= epsilon:

        return np.random.choice([0,1,2])

    # Prevent computation graph from being calculated
    with torch.no_grad():
        # Calculate Q-values fot each action
        obs_torch = torch.tensor(obs.copy(), dtype=torch.float).unsqueeze(0)
        action_values = q_network(obs_torch)

        # Remove attack/mine from possible actions if not facing a diamond
        # if not allow_break_action:
        #     action_values[0, 2] = -float('inf')  

            # Select action with highest Q-value
        action_idx = torch.argmax(action_values).item()
        
    return action_idx


def init_malmo(agent_host):
    """
    Initialize new malmo mission.
    """
    my_mission = MalmoPython.MissionSpec(GetMissionXML(), True)
    my_mission_record = MalmoPython.MissionRecordSpec()
    my_mission.requestVideo(512,512)
    my_mission.setViewpoint(1)
    # my_mission.startAt(2,201,3)

    max_retries = 3
    my_clients = MalmoPython.ClientPool()
    my_clients.add(MalmoPython.ClientInfo('127.0.0.1', 10000)) # add Minecraft machines here as available

    for retry in range(max_retries):
        try:
            agent_host.startMission( my_mission, my_clients, my_mission_record, 0, "DiamondCollector" )
            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print("Error starting mission:", e)
                exit(1)
            else:
                time.sleep(2)

    return agent_host


def get_observation(world_state):
    """
    Use the agent observation API to get a 2 x 5 x 5 grid around the agent. 
    The agent is in the center square facing up.

    Args
        world_state: <object> current agent world state

    Returns
        observation: <np.array>
    """
    obs = np.zeros((15, OBS_SIZE*2+1, OBS_SIZE*2+1))
    CUR_POS = (0,0,0)
    while world_state.is_mission_running:
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors) > 0:
            raise AssertionError('Could not load grid.')

        if world_state.number_of_observations_since_last_state > 0:
            # First we get the json from the observation API
            msg = world_state.observations[-1].text
            # print(len(world_state.observations))
            observations = json.loads(msg)
            # print("%d:%d:%d" % (int(observations[u'XPos']),int(observations[u'YPos']),int(observations[u'ZPos'])))
            # print("%d:%d:%d" % (int(observations[u'XPos']),int(observations[u'YPos']),int(observations[u'ZPos'])))
            CUR_POS = (int(observations[u'XPos']),int(observations[u'YPos']),int(observations[u'ZPos']))
            
            # Get observation
            # print(observations)
            grid = observations['floorAll']
            grid_binary = [1 if x == 'diamond_ore' else 0 for x in grid]
            # print(grid_binary)
            obs = np.reshape(grid_binary, (15, OBS_SIZE*2+1, OBS_SIZE*2+1))
            # print(obs)
            # Rotate observation with orientation of agent
            yaw = observations['Yaw']
            if yaw == 270:
                obs = np.rot90(obs, k=1, axes=(1, 2))
            elif yaw == 0:
                obs = np.rot90(obs, k=2, axes=(1, 2))
            elif yaw == 90:
                obs = np.rot90(obs, k=3, axes=(1, 2))
            
            break

    return obs, CUR_POS


def prepare_batch(replay_buffer):
    """
    Randomly sample batch from replay buffer and prepare tensors

    Args:
        replay_buffer (list): obs, action, next_obs, reward, done tuples

    Returns:
        obs (tensor): float tensor of size (BATCH_SIZE x obs_size
        action (tensor): long tensor of size (BATCH_SIZE)
        next_obs (tensor): float tensor of size (BATCH_SIZE x obs_size)
        reward (tensor): float tensor of size (BATCH_SIZE)
        done (tensor): float tensor of size (BATCH_SIZE)
    """
    batch_data = random.sample(replay_buffer, BATCH_SIZE)
    obs = torch.tensor([x[0] for x in batch_data], dtype=torch.float)
    action = torch.tensor([x[1] for x in batch_data], dtype=torch.long)
    next_obs = torch.tensor([x[2] for x in batch_data], dtype=torch.float)
    reward = torch.tensor([x[3] for x in batch_data], dtype=torch.float)
    done = torch.tensor([x[4] for x in batch_data], dtype=torch.float)
    
    return obs, action, next_obs, reward, done
  

def learn(batch, optim, q_network, target_network):
    """
    Update Q-Network according to DQN Loss function

    Args:
        batch (tuple): tuple of obs, action, next_obs, reward, and done tensors
        optim (Adam): Q-Network optimizer
        q_network (QNetwork): Q-Network
        target_network (QNetwork): Target Q-Network
    """
    obs, action, next_obs, reward, done = batch

    optim.zero_grad()
    values = q_network(obs).gather(1, action.unsqueeze(-1)).squeeze(-1)
    target = torch.max(target_network(next_obs), 1)[0]
    target = reward + GAMMA * target * (1 - done)
    loss = torch.mean((target - values) ** 2)
    loss.backward()
    optim.step()

    return loss.item()


def log_returns(steps, returns):
    """
    Log the current returns as a graph and text file

    Args:
        steps (list): list of global steps after each episode
        returns (list): list of total return of each episode
    """
    box = np.ones(10) / 10
    returns_smooth = np.convolve(returns, box, mode='same')
    plt.clf()
    plt.plot(steps, returns_smooth)
    plt.title('Diamond Collector')
    plt.ylabel('Return')
    plt.xlabel('Steps')
    plt.savefig('returnsq5.png')

    with open('returnsq5.txt', 'w') as f:
        for value in returns:
            f.write("{}\n".format(value)) 


def train(agent_host):
    """
    Main loop for the DQN learning algorithm

    Args:
        agent_host (MalmoPython.AgentHost)
    """
    # Init networks
    q_network = QNetwork((15, OBS_SIZE*2+1, OBS_SIZE*2+1), len(ACTION_DICT))
    target_network = QNetwork((15, OBS_SIZE*2+1, OBS_SIZE*2+1), len(ACTION_DICT))
    target_network.load_state_dict(q_network.state_dict())

    # Init optimizer
    optim = torch.optim.Adam(q_network.parameters(), lr=LEARNING_RATE)

    # Init replay buffer
    replay_buffer = deque(maxlen=REPLAY_BUFFER_SIZE)

    # Init vars
    global_step = 0
    num_episode = 0
    epsilon = 1
    start_time = time.time()
    returns = []
    steps = []
    global PREV_POS 
    global TEMP_POS 

    # Begin main loop
    loop = tqdm(total=MAX_GLOBAL_STEPS, position=0, leave=False)
    while global_step < MAX_GLOBAL_STEPS:
        episode_step = 0
        episode_return = 0
        episode_loss = 0
        done = False

        # Setup Malmo
        agent_host = init_malmo(agent_host)
        world_state = agent_host.getWorldState()
        while not world_state.has_mission_begun:
            time.sleep(0.1)
            world_state = agent_host.getWorldState()
            for error in world_state.errors:
                print("\nError:",error.text)
        obs, CUR_POS = get_observation(world_state)
        PREV_POS = CUR_POS
        TEMP_POS = CUR_POS
        # Run episode
        while world_state.is_mission_running:
            # Take step
            if CUR_POS == TEMP_POS:
                # Get action
                allow_break_action = obs[1, int(OBS_SIZE/2)-1, int(OBS_SIZE/2)] == 1
                action_idx = get_action(obs, q_network, epsilon, allow_break_action)
                command = ACTION_DICT[action_idx]
                agent_host.sendCommand("chat Next: "+command)
                time.sleep(.1)
                agent_host.sendCommand(command)
                episode_step += 1
                global_step += 1
            # print("==", command)
                # time.sleep(2)
            # time.sleep(5)


            # Take step
            # agent_host.sendCommand(command)

            # If your agent isn't registering reward you may need to increase this
            time.sleep(.1)

            # We have to manually calculate terminal state to give malmo time to register the end of the mission
            # If you see "commands connection is not open. Is the mission running?" you may need to increase this
            # episode_step += 1
            if episode_step >= MAX_EPISODE_STEPS:
                done = True
                time.sleep(2)  

            # Get next observation
            world_state = agent_host.getWorldState()
            for error in world_state.errors:
                print("Error:", error.text)
            next_obs, CUR_POS = get_observation(world_state) 
            time.sleep(.1)
            next_obs, TEMP_POS = get_observation(world_state) 

            # Get reward
            reward = 0
            for r in world_state.rewards:
                reward += r.getValue()
            
            # Get falling reward
            # if (PREV_POS[1] - CUR_POS[1]) % 3 == 0:
            if CUR_POS == TEMP_POS:
                # print(PREV_POS, CUR_POS)
                reward += falling_reward(CUR_POS, PREV_POS)
                PREV_POS = CUR_POS
                # print("+++++", reward)
            episode_return += reward

            # Store step in replay buffer
            replay_buffer.append((obs, action_idx, next_obs, reward, done))
            obs = next_obs

            # Learn
            # global_step += 1
            if global_step > START_TRAINING and global_step % LEARN_FREQUENCY == 0:
                batch = prepare_batch(replay_buffer)
                loss = learn(batch, optim, q_network, target_network)
                episode_loss += loss

                if epsilon > MIN_EPSILON:
                    epsilon *= EPSILON_DECAY

                if global_step % TARGET_UPDATE == 0:
                    target_network.load_state_dict(q_network.state_dict())

        num_episode += 1
        returns.append(episode_return)
        steps.append(global_step)
        avg_return = sum(returns[-min(len(returns), 10):]) / min(len(returns), 10)
        loop.update(episode_step)
        loop.set_description('Episode: {} Steps: {} Time: {:.2f} Loss: {:.2f} Last Return: {:.2f} Avg Return: {:.2f}'.format(
            num_episode, global_step, (time.time() - start_time) / 60, episode_loss, episode_return, avg_return))

        if num_episode > 0 and num_episode % 10 == 0:
            log_returns(steps, returns)
            print()


if __name__ == '__main__':
    # Create default Malmo objects:
    agent_host = MalmoPython.AgentHost()
    try:
        agent_host.parse( sys.argv )
    except RuntimeError as e:
        print('ERROR:', e)
        print(agent_host.getUsage())
        exit(1)
    if agent_host.receivedArgument("help"):
        print(agent_host.getUsage())
        exit(0)

    train(agent_host)
