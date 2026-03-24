import random

def fitness(chromosome):
    return sum(chromosome)

def create_individual():
    return [random.randint(0, 1) for _ in range(8)]

population = [create_individual() for _ in range(6)]

for _ in range(10):
    population = sorted(population, key=fitness, reverse=True)

    parents = population[:2]
    new_population = parents.copy()

    while len(new_population) < 6:
        # Crossover
        point = random.randint(1, 7)
        child = parents[0][:point] + parents[1][point:]

        # Mutation
        if random.random() < 0.1:
            idx = random.randint(0, 7)
            child[idx] ^= 1

        new_population.append(child)

    population = new_population

print("Best chromosome:", population[0])