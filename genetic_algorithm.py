import random
import string
import math
import pandas as pd
from zxcvbn import zxcvbn


class GeneticAlgorithm:
    def __init__(self, population_size, generations, mutation_rate, tournament_size, max_length, uppercase, lowercase,
                 digits, special, min_length=8):
        self.MIN_LENGTH = min_length
        self.MAX_LENGTH = max_length

        self.REQUIRED_CHARS = {}
        if uppercase:
            self.REQUIRED_CHARS['uppercase'] = string.ascii_uppercase
        if lowercase:
            self.REQUIRED_CHARS['lowercase'] = string.ascii_letters
        if digits:
            self.REQUIRED_CHARS['digits'] = string.digits
        if special:
            self.REQUIRED_CHARS['special'] = '!@#$%^&*()_+-=[]{}|;:,.<>?'

        self.POPULATION_SIZE = population_size
        self.GENERATIONS = generations
        self.MUTATION_RATE = mutation_rate
        self.TOURNAMENT_SIZE = tournament_size

    def create_initial_population(self):
        common_passwords_csv = pd.read_csv('common_passwords.csv')
        common_passwords = common_passwords_csv['password'].to_list()

        return random.sample(common_passwords, self.POPULATION_SIZE)

    def calculate_entropy(self, password):
        char_count = {}
        for char in password:
            char_count[char] = char_count.get(char, 0) + 1
        entropy = 0
        for count in char_count.values():
            probability = count / len(password)
            entropy -= probability * math.log2(probability)
        return entropy

    def calculate_fitness(self, password):
        if len(password) < self.MIN_LENGTH or len(password) > self.MAX_LENGTH:
            return 0

        # Usamos uma biblioteca externa para calcular a força da senha
        # e usamos o score dela para influenciar a fitness.
        zxcvbn_result = zxcvbn(password)

        num_requirements_met = 0
        for char_set in self.REQUIRED_CHARS.values():
            if any(char in password for char in char_set):
                num_requirements_met += 1

        entropy = self.calculate_entropy(password)
        return entropy * num_requirements_met * zxcvbn_result['score']

    def tournament_selection(self, population, fitnesses):
        tournament = random.sample(list(zip(population, fitnesses)), self.TOURNAMENT_SIZE)
        return max(tournament, key=lambda x: x[1])[0]

    def crossover(self, parent1, parent2):
        point = random.randint(0, min(len(parent1), len(parent2)))
        return parent1[:point] + parent2[point:]

    def mutate(self, password):
        if random.random() > self.MUTATION_RATE:
            return password

        chars = list(password)
        pos = random.randint(0, len(chars) - 1)
        all_chars = ''.join(self.REQUIRED_CHARS.values())

        # Precisamos possibilitar a adição de caracteres para que
        # a senha final possa aumentar.
        action = random.choice(['replace', 'add'])

        if action == 'replace':
            chars[pos] = random.choice(all_chars)
        elif action == 'add':
            chars.append(random.choice(all_chars))

        result = ''.join(chars)
        if len(result) > self.MAX_LENGTH:
            result = result[:self.MAX_LENGTH]
        return result

    def genetic_algorithm(self):
        population = self.create_initial_population()

        for generation in range(self.GENERATIONS):
            fitnesses = [self.calculate_fitness(pwd) for pwd in population]
            best_fitness = max(fitnesses)
            best_password = population[fitnesses.index(best_fitness)]

            new_population = []
            for _ in range(self.POPULATION_SIZE - 1):
                parent1 = self.tournament_selection(population, fitnesses)
                parent2 = self.tournament_selection(population, fitnesses)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)

            population = new_population

            yield best_fitness, best_password, generation + 1

        final_fitnesses = [self.calculate_fitness(pwd) for pwd in population]
        best_fitness = max(final_fitnesses)
        best_password = population[final_fitnesses.index(best_fitness)]

        return best_password, best_fitness
