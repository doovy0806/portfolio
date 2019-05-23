import gym
from gym.envs.registration import register
import random

register(
	id='FrozenLake8x8-v3',
	entry_point='gym.envs.toy_text:FrozenLakeEnv',
	kwargs={'map_name': '8x8',
			'is_slippery':False}
)

env = gym.make('FrozenLake8x8-v3')
done = False
discount = 0.99
success = 0
state = env.reset()
q_table = {s : [0,0,0,0] for s in range(0,64)}
noise = 0
t=0
for i_episode in range(1000):
	t+=1
	noise = 1/(t**2)
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
		if reward ==1 and done:
			# needs to be comentized
			success+=1

		elif reward==0 and done:
			reward = -0.01
		# env.render()

		actions[action] = (reward+discount*newqvalue)

state = env.reset()
done = False
naction = 0
while not done:
	naction += 1
	actions = q_table.get(state)
	action = actions.index(max(actions))
	state, reward, done, info = env.step(action)
	newactions = q_table.get(state)
	newaction = newactions.index(max(newactions))
	newqvalue = newactions[newaction]
	print("####", naction, "action")
	env.render()
# print(success/i_episode)

	# print(i_episode, "episode")


# Your code start here...
