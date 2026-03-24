import random

# Objective function
def f(x):
    return x**2

# Initialize particles
particles = [random.uniform(-10, 10) for _ in range(5)]
velocities = [0]*5
pbest = particles[:]
gbest = min(particles, key=f)

for _ in range(20):
    for i in range(5):
        velocities[i] = (0.5 * velocities[i] +
                         1.5 * random.random() * (pbest[i] - particles[i]) +
                         1.5 * random.random() * (gbest - particles[i]))

        particles[i] += velocities[i]

        if f(particles[i]) < f(pbest[i]):
            pbest[i] = particles[i]

    gbest = min(pbest, key=f)

print("Best solution:", gbest)