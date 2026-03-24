import numpy as np

# States: 3 positions
rewards = [0, 0, 1]  # goal at last state
gamma = 0.9

values = np.zeros(3)

for _ in range(10):
    new_values = values.copy()
    for s in range(3):
        if s == 2:
            continue
        new_values[s] = rewards[s] + gamma * max(values[min(s+1,2)], values[max(s-1,0)])
    values = new_values

print("State values:", values)