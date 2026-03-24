import random

def f(x, y):
    return x**2 + y**2

particles = [[random.uniform(-10,10), random.uniform(-10,10)] for _ in range(5)]
velocities = [[0,0] for _ in range(5)]
pbest = particles[:]
gbest = min(particles, key=lambda p: f(p[0], p[1]))

for _ in range(20):
    for i in range(5):
        for d in range(2):
            velocities[i][d] = (0.5 * velocities[i][d] +
                                1.5 * random.random() * (pbest[i][d] - particles[i][d]) +
                                1.5 * random.random() * (gbest[d] - particles[i][d]))

            particles[i][d] += velocities[i][d]

        if f(*particles[i]) < f(*pbest[i]):
            pbest[i] = particles[i]

    gbest = min(pbest, key=lambda p: f(p[0], p[1]))

print("Best position:", gbest)