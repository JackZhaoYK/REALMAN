# Rllib docs: https://docs.ray.io/en/latest/rllib.html

try:
    from malmo import MalmoPython
except:
    import MalmoPython

import sys
import time
import json
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

import gym, ray
from gym.spaces import Discrete, Box
from ray.rllib.agents import ppo


class DiamondCollector(gym.Env):

    def __init__(self, env_config):  
        # Static Parameters
        self.size = 50
        self.reward_density = .1
        self.penalty_density = .02
        self.obs_size = 20
        self.max_episode_steps = 600
        self.log_frequency = 10
        self.episode_num = 0
        self.quit = False

        # Rllib Parameters
        self.action_space = Box(-1, 1, shape=(3,), dtype=np.float32)
        self.observation_space = Box(0, 1, shape=(np.prod([15, self.obs_size*2+1, self.obs_size*2+1]), ), dtype=np.int32)
        # Malmo Parameters
        self.agent_host = MalmoPython.AgentHost()
        try:
            self.agent_host.parse( sys.argv )
        except RuntimeError as e:
            print('ERROR:', e)
            print(self.agent_host.getUsage())
            exit(1)

        # DiamondCollector Parameters
        self.obs = None
        self.cur_pos = (0,0,0)
        self.episode_step = 0
        self.episode_return = 0
        self.returns = []
        self.steps = []

        # ADDED
        self.prev_pos = (0,0,0)
        self.temp_pos = (0,0,0)
        self.pos_list =list()


    def reset(self):
        """
        Resets the environment for the next episode.

        Returns
            observation: <np.array> flattened initial obseravtion
        """
        # world_state = self.agent_host.getWorldState()
        # reward = 0
        # for r in world_state.rewards:
        #     if r.getValue() < 0:
        #         reward += -1
        #     if r.getValue()>90:
        #         reward+=100
        # # print("reward: ",cur_reward)
        # self.episode_return += reward

        # Reset Malmo
        world_state = self.init_malmo()

        # Reset Variables
        print("Episode:  ",self.episode_num,"Step:  ",self.episode_step,"Reward:  ",self.episode_return)
        self.returns.append(self.episode_return)
        current_step = self.steps[-1] if len(self.steps) > 0 else 0
        self.steps.append(current_step + self.episode_step)
        self.episode_return = 0
        self.episode_step = 0
        self.episode_num+=1
        self.quit = False

        # Log
        if len(self.returns) > self.log_frequency and \
            len(self.returns) % self.log_frequency == 0:
            print("Now we should have our log!")
            self.log_returns()

        # Get Observation
        self.obs, self.cur_pos = self.get_observation(world_state)
        self.obs, self.temp_pos = self.get_observation(world_state) 
        self.obs, self.prev_pos = self.get_observation(world_state)

        return self.obs.flatten()

    def falling_reward(self, cur, prev):
        falldown= prev[1] - cur[1] 
        return -15 if falldown >= 15 else falldown

    def step(self, action):
        """
        Take an action in the environment and return the results.

        Args
            action: <int> index of the action to take

        Returns
            observation: <np.array> flattened array of obseravtion
            reward: <int> reward from taking action
            done: <bool> indicates terminal state
            info: <dict> dictionary of extra information
        """
        
        # Get Action
        # if action[1] > 0.5:
        #     self.agent_host.sendCommand('turn 1')
        #     self.agent_host.sendCommand('turn 1')
        #     self.agent_host.sendCommand('move {:30.1f}'.format(action[0]))
        #     time.sleep(1)
        # elif action[1] < -0.5:
        #     self.agent_host.sendCommand('turn -1')
        #     self.agent_host.sendCommand('turn -1')
        #     self.agent_host.sendCommand('move {:30.1f}'.format(action[0]))
        #     time.sleep(1)
        # else:
        # print("move:     ",action[0])
        # print("turn:     ",action[1])
        if self.quit:
            self.agent_host.sendCommand('quit')
            return self.obs.flatten(), 0, True, dict()
        self.agent_host.sendCommand('move {:30.1f}'.format(action[0]))
        self.agent_host.sendCommand('turn {:30.1f}'.format(action[1]))
        # self.agent_host.sendCommand('move {:30.1f}'.format(action[0]))
        time.sleep(.2)

        # self.agent_host.sendCommand('turn {:30.1f}'.format(action[1]))
        self.episode_step += 1

        # Get Observation
        world_state = self.agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:", error.text)
        self.obs, self.cur_pos = self.get_observation(world_state) 
        self.pos_list.append(self.cur_pos)
        # print("STEP: ",len(self.pos_list))
        # Get Done
        
        done = not world_state.is_mission_running 

        # Get Reward
        time.sleep(0.1)
        self.obs, self.temp_pos = self.get_observation(world_state) 

        reward = 0
        if self.temp_pos == self.cur_pos:
            reward += self.falling_reward(self.cur_pos, self.prev_pos)
            self.prev_pos = self.cur_pos
        else:
            pass
            # print("Diff: CUR: {}, PREV: {}".format(self.cur_pos, self.temp_pos))
        # cur_reward =[]
        
        for r in world_state.rewards:
            if r.getValue() < 0:
                reward += -1
                # cur_reward.append(-1)
            if r.getValue() >90:
                reward += 100
                self.quit = True


                
        # print("reward: ",cur_reward)
        self.episode_return += reward
        if reward!=0:
            self.agent_host.sendCommand("chat Current Reward: "+str(reward)+"   Total: "+str(self.episode_return))
        return self.obs.flatten(), reward, done, dict()

    def get_mission_xml(self):

        glass_xml = ""
        for y in range(2,202):
            for x in range(0,20):
                glass_xml+="<DrawBlock x='%d' y='%d' z='1' type='glass' />" % (x,y)
                glass_xml+="<DrawBlock x='%d' y='%d' z='6' type='glass' />" % (x,y)
                for glass_z in range(2,6):
                    glass_xml+="<DrawBlock x='0' y='%d' z='%d' type='glass' />" % (y,glass_z)
                    glass_xml+="<DrawBlock x='19' y='%d' z='%d' type='glass' />" % (y,glass_z)
        object_xml = ""
        for init_z in range(2,6):
            object_xml+="<DrawBlock x='%d' y='%d' z='%d' type='diamond_ore' />" %(1,200,init_z)
            object_xml+="<DrawBlock x='%d' y='%d' z='%d' type='diamond_ore' />" %(2,200,init_z)
            object_xml+="<DrawBlock x='%d' y='%d' z='%d' type='diamond_ore' />" %(3,200,init_z)
        for y in range(197,4,-3):
            # for _ in range(1,19):
            first_x = randint(1,17)
            first_z = randint(2,5)
            for z in range(first_z,first_z+2):
                object_xml+="<DrawBlock x='%d' y='%d' z='%d' type='diamond_ore' />" %(first_x,y,z)
                object_xml+="<DrawBlock x='%d' y='%d' z='%d' type='diamond_ore' />" %(first_x+1,y,z)

            while True:
                second_x = randint(1,17)
                if second_x not in range(first_x-3, first_x+3):
                    break

            second_z = randint(2,5)
            for z in range(second_z,second_z+2):
                object_xml+="<DrawBlock x='%d' y='%d' z='%d' type='diamond_ore' />" %(second_x,y,z)
                object_xml+="<DrawBlock x='%d' y='%d' z='%d' type='diamond_ore' />" %(second_x+1,y,z)

        end_xml = ""
        for i in range(-self.size,self.size+1):
            end_xml+="<Marker reward='100' x='%d' y='2' z='%d' tolerance='2' />" %(i,i)

        return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
                <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

                    <About>
                        <Summary>REALMAN</Summary>
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
                                "<DrawCuboid x1='0' x2='19' y1='1' y2='202' z1='1' z2='6' type='air'/>" + \
                                "<DrawCuboid x1='{}' x2='{}' y1='0' y2='1' z1='{}' z2='{}' type='stone'/>".format(-self.size, self.size, -self.size, self.size) + \
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
                            <ContinuousMovementCommands/>
                            <MissionQuitCommands/>
                            <RewardForTouchingBlockType>
                                <Block type="glass" reward="-0.3"/>
                            </RewardForTouchingBlockType>
                            <RewardForReachingPosition>''' +\
                                end_xml +\
                            '''</RewardForReachingPosition>
                            <ObservationFromFullStats/>
                            <ObservationFromRay/>
                            <ObservationFromChat/>
                            

                            <ObservationFromGrid>
                                <Grid name="floorAll">
                                    <min x="-'''+str(self.obs_size)+'''" y="-14" z="-'''+str(self.obs_size)+'''"/>
                                    <max x="'''+str(self.obs_size)+'''" y="0" z="'''+str(self.obs_size)+'''"/>
                                </Grid>
                            </ObservationFromGrid>
                            <AgentQuitFromReachingCommandQuota total="'''+str(self.max_episode_steps)+'''" />
                        </AgentHandlers>
                    </AgentSection>
                </Mission>'''


    def init_malmo(self):
        """
        Initialize new malmo mission.
        """
        my_mission = MalmoPython.MissionSpec(self.get_mission_xml(), True)
        my_mission_record = MalmoPython.MissionRecordSpec()
        my_mission.requestVideo(700,700)
        my_mission.setViewpoint(1)

        max_retries = 3
        my_clients = MalmoPython.ClientPool()
        my_clients.add(MalmoPython.ClientInfo('127.0.0.1', 10000)) # add Minecraft machines here as available

        for retry in range(max_retries):
            try:
                self.agent_host.startMission( my_mission, my_clients, my_mission_record, 0, 'DiamondCollector' )
                break
            except RuntimeError as e:
                if retry == max_retries - 1:
                    print("Error starting mission:", e)
                    exit(1)
                else:
                    time.sleep(2)

        world_state = self.agent_host.getWorldState()
        while not world_state.has_mission_begun:
            time.sleep(0.1)
            world_state = self.agent_host.getWorldState()
            for error in world_state.errors:
                print("\nError:", error.text)

        return world_state


    def get_observation(self,world_state):
        """
        Use the agent observation API to get a 2 x 5 x 5 grid around the agent. 
        The agent is in the center square facing up.

        Args
            world_state: <object> current agent world state

        Returns
            observation: <np.array>
        """
        obs = np.zeros((15, self.obs_size*2+1, self.obs_size*2+1))
        CUR_POS = (0,0,0)
        while world_state.is_mission_running:
            time.sleep(0.1)
            world_state = self.agent_host.getWorldState()
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
                obs = np.reshape(grid_binary, (15, self.obs_size*2+1, self.obs_size*2+1))
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



    def log_returns(self):
        """
        Log the current returns as a graph and text file

        Args:
            steps (list): list of global steps after each episode
            returns (list): list of total return of each episode
        """
        box = np.ones(self.log_frequency) / self.log_frequency
        returns_smooth = np.convolve(self.returns, box, mode='same')
        plt.clf()
        plt.plot(self.steps, returns_smooth)
        plt.title('REALMAN')
        plt.ylabel('Return')
        plt.xlabel('Steps')
        plt.savefig('REALMAN_returns4.png')
        print("Log saved!")

        with open('REALMAN_returns4.txt', 'w') as f:
            for step, value in zip(self.steps, self.returns):
                f.write("{}\t{}\n".format(step, value)) 


if __name__ == '__main__':
    ray.init()
    trainer = ppo.PPOTrainer(env=DiamondCollector, config={
        'env_config': {},           # No environment parameters to configure
        'framework': 'torch',       # Use pyotrch instead of tensorflow
        'num_gpus': 2,              # We aren't using GPUs
        'num_workers': 0            # We aren't using parallelism
    })

    while True:
        print(trainer.train())