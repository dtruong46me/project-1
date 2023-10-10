
import random

def fitness(x):
    print("fitness", abs(x**2 + 6*x - 19))
    return abs(x**2 + 6*x - 19)

def initialize_population(population_size: int, min_value, max_value) -> list:
    print("initial_population: ", [random.uniform(min_value, max_value) for _ in range(population_size)])

    return [random.uniform(min_value, max_value) for _ in range(population_size)]

def crossover(parent1: list, parent2: list):
    # print(parent1, type(parent1))

    alpha = random.uniform(0, 1)

    child1 = alpha * parent1 + (1-alpha) * parent2
    child2 = (1-alpha) * parent1 + alpha * parent2

    return child1, child2

def mutation(individual, mutation_rate, min_value, max_value):

    if random.random() < mutation_rate:
        individual += random.uniform(-1, 1)
        individual = max(min_value, min(individual, max_value))

    return individual

def genetic_algorithm(population_size, min_value, max_value, mutation_rate, generations: int):

    population = initialize_population(population_size, min_value, max_value)

    for generation in range(generations):

        fitness_value = [fitness(x) for x in population]

        # best_individual = population[fitness_value.index(min(fitness_value))]
        best_individual_index = fitness_value.index(min(fitness_value))
        best_individual = population[best_individual_index]

        print(f"Generation {generation}: Best Individuals = {fitness(best_individual)}")


        print(population)
        selected_parents = random.sample(population, population_size // 2)
        print("selected_parents", selected_parents, "len(selected_parents)", len(selected_parents))

        new_population = []

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(selected_parents, 2)

            child1, child2 = crossover(parent1, parent2)

            child1 = mutation(child1, mutation_rate, min_value, max_value)
            child2 = mutation(child2, mutation_rate, min_value, max_value)

            new_population.extend([child1, child2])

        population = new_population

    return best_individual

def main():
    best_solution = genetic_algorithm(population_size=50, min_value=-10, max_value=10, mutation_rate=0.2, generations=100)

    print("best_solution", best_solution)
    print(fitness(best_solution))

if __name__ == '__main__':
    main()
    