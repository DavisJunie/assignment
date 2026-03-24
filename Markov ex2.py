import random

states = ["A", "B"]
actions = ["left", "right"]

# Rewards
def reward(state, action):
    if state == "A" and action == "right":
        return 1
    return 0

# Random policy evaluation
for _ in range(5):
    state = random.choice(states)
    action = random.choice(actions)
    r = reward(state, action)
    print(f"State: {state}, Action: {action}, Reward: {r}")