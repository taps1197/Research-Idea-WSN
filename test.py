import numpy
import ga
import random

"""
The y=target is to maximize this equation ASAP:
    y = w1x1+w2x2+w3x3+w4x4+w5x5+6wx6
    where (x1,x2,x3,x4,x5,x6)= ...
    What are the best values for the 6 weights w1 to w6?
    We are going to use the genetic algorithm for the best possible values after a number of generations.
"""


# varun's ideation 
N = 6
chr=[[0 for x in range(0,N)] for x in range(0,N)]

for i in range(0,N):
    s=random.randrange(3,6,1)
    list=[]

    for j in range(s):
        list = random.sample(range(0,N),s)

    for k in range(0,N):
        for l in list:
            if l is k:
                chr[i][k]=1
                break
            
                
print("CHR::  ",chr,"\n")

for k in range(0,N):
    print("\nch[",k,"]:",chr[k])           
    # Inputs of the equation.
    equation_inputs = chr[k]
    # Number of the weights we are looking to optimize.
    num_weights = 6

    """
    Genetic algorithm parameters:
        Mating pool size
        Population size
    """
    sol_per_pop = 8
    num_parents_mating = 4

    # Defining the population size.

    pop_size = (sol_per_pop,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.

    #Creating the initial population.
    new_population = numpy.random.uniform(low=1.0, high=0, size=pop_size)
    print(new_population)

    num_generations = 5
    for generation in range(num_generations):
        print("Generation : ", generation)
        # Measing the fitness of each chromosome in the population.
        # fitness = ga.cal_pop_fitness(equation_inputs, new_population)
        fitness = ga.fitness(equation_inputs)


        # Selecting the best parents in the population for mating.
        parents = ga.select_mating_pool(new_population, fitness, 
                                        num_parents_mating)

        # Generating next generation using crossover.
        offspring_crossover = ga.crossover(parents,
                                        offspring_size=(pop_size[0]-parents.shape[0], num_weights))

        # Adding some variations to the offsrping using mutation.
        offspring_mutation = ga.mutation(offspring_crossover)

        # Creating the new population based on the parents and offspring.
        new_population[0:parents.shape[0], :] = parents
        new_population[parents.shape[0]:, :] = offspring_mutation

        #print 
        # The best result in the current iteration.
        print("Best result : ", numpy.max(numpy.sum(new_population*equation_inputs, axis=1)))

    # Getting the best solution after iterating finishing all generations.
    #At first, the fitness is calculated for each solution in the final generation.
    # fitness = ga.cal_pop_fitness(equation_inputs, new_population)
    fitness = ga.fitness(equation_inputs)    
    #  Then return the index of that solution corresponding to the best fitness.
    best_match_idx = numpy.where(fitness == numpy.max(fitness))

    print("Best solution : ", new_population[best_match_idx, :])
    print("Best solution fitness : ", fitness[best_match_idx])
