import gym
from gym.envs.registration import register
import random

register(
	id='FrozenLake8x8-v3',
	entry_point='gym.envs.toy_text:FrozenLakeEnv',
	kwargs={'map_name': '8x8',
			'is_slippery':True}
)

env = gym.make('FrozenLake8x8-v3')
done = False
discount = 0.9
alpha = 0.8
state = env.reset()
q_table = {s : [0,0,0,0] for s in range(0,64)}
success =0
noise = 0
t=0
iteration = 1000
for i_episode in range(iteration):
	t+=1
	noise = (2/t)
	state = env.reset()
	done=False
	while not done:
		actions = q_table.get(state)
		if random.random() < noise :
			action = random.randint(0,3)
		elif max(actions)!=0:
			action = actions.index(max(actions))
		else:
			zero_index = random.randint(0,3)
			while actions[zero_index] !=0:
				zero_index = random.randint(0,3)
			action = zero_index
		qvalue = actions[action]
		prev_state = state
		state, reward, done, info = env.step(action)
		newactions = q_table.get(state)
		newaction = newactions.index(max(newactions))
		newqvalue = newactions[newaction]
		if reward==0 and done:
			reward = -0.7
		if reward==1 and done:
			success+=1
		actions[action] = (1-alpha)*qvalue + alpha*(reward+discount*newqvalue)

		t+=1

state = env.reset()
done = False
naction=0

while not done:
	naction+=1
	actions = q_table.get(state)
	action = actions.index(max(actions))
	state, reward, done, info = env.step(action)
	print("####",naction,"action")
	env.render()



