import random

def fitness(x):
    return abs(x**2 + 6*x - 19)

def initialize_population(population_size, min_value, max_value):
    return [random.uniform(min_value, max_value) for _ in range(population_size)]

def crossover(parent1, parent2):
    alpha = random.uniform(0, 1)
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = alpha * parent2 + (1 - alpha) * parent1
    return child1, child2

def mutate(individual, mutation_rate, min_value, max_value):
    if random.random() < mutation_rate:
        individual += random.uniform(-1, 1)
        individual = max(min_value, min(individual, max_value))
    return individual

def genetic_algorithm(population_size, min_value, max_value, mutation_rate, generations, stop_threshold):
    population = initialize_population(population_size, min_value, max_value)
    best_solution = None
    best_fitness = float('inf')

    for generation in range(generations):
        fitness_values = [fitness(x) for x in population]
        best_individual = population[fitness_values.index(min(fitness_values))]
        best_current_fitness = fitness(best_individual)
        
        print(f"Thế hệ {generation}: Giá trị tốt nhất = {best_current_fitness}")

        if best_current_fitness < best_fitness:
            best_solution = best_individual
            best_fitness = best_current_fitness

        if best_fitness < stop_threshold:
            break
        
        selected_parents = random.sample(population, population_size // 2)
        
        new_population = []
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(selected_parents, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate, min_value, max_value)
            child2 = mutate(child2, mutation_rate, min_value, max_value)
            new_population.extend([child1, child2])
        
        population = new_population

    return best_solution, best_fitness

best_solution, best_fitness = genetic_algorithm(population_size=50, min_value=-10, max_value=10, mutation_rate=0.1, generations=1000, stop_threshold=1e-6)
print(f"Kết quả tốt nhất: {best_solution}, Giá trị tốt nhất: {best_fitness}")
