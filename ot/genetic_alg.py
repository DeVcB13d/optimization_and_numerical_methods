# Implementation of a gentic algorithm to find the optimality of a given function

'''
Example function : f(x) = -x^2 + 15x
x in [0,15]

x is represented as a 4 bit binary number

Basic steps:

1. Generate a random population
2. Find fitness of each chromosome f(C)
3. Assign probabilities to each chromosome based on f(C)
4. Roulette wheel selection of the chromosomes
5. Choose a crosover probability to crossover
6. If crossover then choose a random point in the chromosome and exchange 
7. Random bit flip mutation

'''

import random
import numpy as np
import math
import matplotlib.pyplot as plt


# Function to convert a binary list to a single integer
def binary_to_int(binary_list):
    decimal_value = 0
    power = len(binary_list) - 1

    for digit in binary_list:
        decimal_value += digit * (2 ** power)
        power -= 1

    return decimal_value

def plot_fitness(function,discrete_x,discrete_y,lim_range,generation):
    # Create x values for the continuous function
    # Creating 100 values in the lim_range of 0 to 16
    x = np.linspace(0, lim_range+1, 100) 
    # Calculate the y values for the continuous function
    y_continuous = function(x)

    # Create the plot
    plt.plot(x, y_continuous, label='optimizing function at generation {0}'.format(generation))
    sc = plt.scatter(discrete_x, discrete_y, color='red', label='Population Values')

    # Add labels, title, and legend
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Optimizing function and population values')
    plt.legend()

    # Display the plot
    plt.grid(True)
    return sc

def update(sc,discrete_x,discrete_y):
    print("discrete x : ",discrete_x)   
    plt.pause(0.1)
    sc.set_offsets(np.c_[discrete_x,discrete_y])
    plt.draw()

# Randomly initialize a population
def init_population(population_size, bits):
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0,1) for _ in range(bits)]
        population.append(chromosome)
    return population

# Calculate the fitness for the entire population
def get_fitness(population,fitness_fn):
    fitness = []
    int_values = []
    for chr in population:
        # Convert the list into an integer
        int_conv = binary_to_int(chr)
        int_values.append(int_conv)
        fitness.append(fitness_fn(int_conv))

    return fitness,int_values

# Select a randon individual based o roulette wheel selection               
def roulette_wheel_selection(fitness):
    # Determining the probabilities of selection
    fit_sum = sum(fitness)
    fitness_prob_weights = [1 - (fit/fit_sum )for fit in fitness]
    roulette_wheel = []
    roulette_wheel.append(fitness_prob_weights[0])

    # Generating a roulette wheel
    for fwi,fw in enumerate(fitness_prob_weights):
        if fwi != 0:
            roulette_wheel.append(roulette_wheel[fwi-1]+fw)
    print("roulette wheel weights : ",roulette_wheel)

    # Generate a random number
    rand_num = random.random()
    print("random number : ",rand_num)
    print("roulette wheel : ",roulette_wheel)
    for i,weight in enumerate(roulette_wheel):
        if rand_num  < weight:
            print("selected : ",i)
            return i

# Function to perform single point crossover in 2 inds
def single_point_crossover(parent1,parent2):
    # Ensure both parents have the same length
    assert len(parent1) == len(parent2)
    # Choosing a random poin to swap from 
    x = random.randint(0,len(parent1))
    # Randomly select a crossover point
    crossover_point = random.randint(1, len(parent1) - 1)

    # Perform crossover to create two offspring individuals
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

    return offspring1, offspring2

# Defining bitflip mutation
def bitflip_mutation(chromosome,mutation_rate):
    for i,chrome in enumerate(chromosome):
        # Generate a random number
        random_mutation_num = random.random()
        if random_mutation_num < mutation_rate:
            if chrome == 0:
                chromosome[i] = 1
            else:
                chromosome[i] = 0
    return chromosome



def genetic_optimize(fitness_fn,population_size,crossover_rate,mutation_rate,lim_range,total_generations):
    plt.show()
    # Finding the number of bits required to initialize the population
    bits = int(math.log2(lim_range)+1)
    # Generating a random popultation 
    population = init_population(population_size,bits)
    print("Initial population : ",population)
    fitness,int_values = get_fitness(population,fitness_fn)
    # Plotting the fitness function and fitness of the population
    plt_sc = plot_fitness(fitness_fn,int_values,fitness,lim_range,0)

    # Running the genetic algorithm for a set of generations
    for generation_i in range(total_generations):

        new_generation = []

        while len(new_generation) < population_size:
            # selecting 2 random individuals for crossover
            ind1 = roulette_wheel_selection(fitness)
            ind2 = roulette_wheel_selection(fitness)  

            # Setting a random probability for genetic crossover
            crossover_prob = random.random()
            if crossover_prob < crossover_rate:
                offspring1, offspring2 = single_point_crossover(population[ind1], population[ind2])

                # Random mutation
                mutant_1 = bitflip_mutation(offspring1,mutation_rate)
                mutant_2 = bitflip_mutation(offspring2,mutation_rate)

                new_generation.append(mutant_1)
                new_generation.append(mutant_2)
        
        population = new_generation.copy()
        fitness,int_values = get_fitness(population,fitness_fn)

        # Plotting the fitness function and fitness of the population
        update(plt_sc,int_values,fitness)

        for i in fitness:
            print(i, end = " ")

    return max(fitness),population[fitness.index(max(fitness))]
    

def main():
    POPULATION_SIZE = 10
    CROSSOVER_RATE = 0.7
    MUTATION_RATE = 0.01
    FITNESS_FN = lambda x : -1*(x)**2 - 4
    LIM_RANGE = 15

    TOTAL_GENERATIONS = 100

    max_value, x_value = genetic_optimize(FITNESS_FN,POPULATION_SIZE,CROSSOVER_RATE,MUTATION_RATE,LIM_RANGE,TOTAL_GENERATIONS)
    print("Max value by genetic = {0} for x = {1} ".format(max_value,x_value))

main()

