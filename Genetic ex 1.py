import random

# Fitness function
def fitness(x):
    return x**2

# Generate initial population
population = [random.randint(0, 31) for _ in range(6)]

for generation in range(10):
    population = sorted(population, key=fitness, reverse=True)
    print(f"Gen {generation}: {population}")

    # Select top 2
    parents = population[:2]

    # Crossover + mutation
    new_population = parents.copy()
    while len(new_population) < 6:
        child = (parents[0] + parents[1]) // 2  # simple crossover
        if random.random() < 0.1:
            child += random.randint(-2, 2)  # mutation
        new_population.append(child)

    population = new_population

print("Best solution:", population[0])