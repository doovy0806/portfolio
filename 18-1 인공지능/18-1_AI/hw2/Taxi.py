import gym
import random

env = gym.make('Taxi-v2')

done = False
state = env.reset()
q_table = {s : [0,0,0,0,0,0] for s in range(0, 500)}
success =0
noise = 0
iteration = 5000
for i in range(iteration):
    state = env.reset()
    noise = 40/(i+1)
    done = False
    # print(i)
    while not done:
        actions = q_table[state]
        maxaction = max(actions)

        if random.random() < noise  :
            action = random.randint(0,5)
        else:
            action = actions.index(maxaction)

        qvalue = actions[action]
        prev_state = state

        state, reward, done, info = env.step(action)
        newactions = q_table.get(state)
        newaction = newactions.index(max(newactions))
        newqvalue = newactions[newaction]
        actions[action] =  (reward + newqvalue)
total = 0
for p in range(1):
    state = env.reset()
    done = False
    # points = 0
    m=0
    while not done:
        m+=1
        actions = q_table.get(state)
        action = actions.index(max(actions))
        state, reward, done, info = env.step(action)
        # points += reward
        print("####",m,"action")
        env.render()
    # total += points
# print(total/100)



