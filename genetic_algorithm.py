import random
import string
import math

MIN_LENGTH = 8
MAX_LENGTH = 36
REQUIRED_CHARS = {
    'uppercase': string.ascii_uppercase,
    'lowercase': string.ascii_letters,
    'digits': string.digits,
    'special': '!@#$%^&*()_+-=[]{}|;:,.<>?'
}

POPULATION_SIZE = 100
GENERATIONS = 3000
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 5


def generate_random_password():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    all_chars = ''.join(REQUIRED_CHARS.values())
    return ''.join(random.choice(all_chars) for _ in range(length))


def calculate_entropy(password):
    char_count = {}
    for char in password:
        char_count[char] = char_count.get(char, 0) + 1
    entropy = 0
    for count in char_count.values():
        probability = count / len(password)
        entropy -= probability * math.log2(probability)
    return entropy


def calculate_fitness(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return 0

    num_requirements_met = 0
    for char_set in REQUIRED_CHARS.values():
        if any(char in password for char in char_set):
            num_requirements_met += 1

    entropy = calculate_entropy(password)
    return entropy * num_requirements_met


def tournament_selection(population, fitnesses):
    tournament = random.sample(list(zip(population, fitnesses)), TOURNAMENT_SIZE)
    return max(tournament, key=lambda x: x[1])[0]


def crossover(parent1, parent2):
    point = random.randint(0, min(len(parent1), len(parent2)))
    return parent1[:point] + parent2[point:]


def calculate_max_fitness():
    max_requirements_met = len(REQUIRED_CHARS)
    max_entropy = math.log2(MAX_LENGTH)
    return max_entropy * max_requirements_met


def mutate(password):
    if random.random() > MUTATION_RATE:
        return password

    chars = list(password)
    pos = random.randint(0, len(chars) - 1)
    all_chars = ''.join(REQUIRED_CHARS.values())
    chars[pos] = random.choice(all_chars)
    return ''.join(chars)


def genetic_algorithm():
    population = [generate_random_password() for _ in range(POPULATION_SIZE)]
    max_possible_fitness = calculate_max_fitness()

    print(f"Max Possible Fitness: {max_possible_fitness}")

    for generation in range(GENERATIONS):
        fitnesses = [calculate_fitness(pwd) for pwd in population]
        best_fitness = max(fitnesses)
        best_password = population[fitnesses.index(best_fitness)]

        if best_fitness >= max_possible_fitness:
            print(f"Maximum fitness reached at generation {generation}")
            return best_password, best_fitness

        new_population = [best_password]
        for _ in range(POPULATION_SIZE - 1):
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    final_fitnesses = [calculate_fitness(pwd) for pwd in population]
    best_fitness = max(final_fitnesses)
    best_password = population[final_fitnesses.index(best_fitness)]
    print(f"Completed {GENERATIONS} generations")

    return best_password, best_fitness


if __name__ == "__main__":
    password, fitness = genetic_algorithm()
    print(f"Best password found: {password}")
    print(f"Fitness score: {fitness}")
