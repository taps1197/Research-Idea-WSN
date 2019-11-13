import numpy

# def cal_pop_fitness(equation_inputs, pop):
#     # Calculating the fitness value of each solution in the current population.
#     # The fitness function caulcuates the sum of products between each input and its corresponding weight.
#     fitness = numpy.sum(pop*equation_inputs, axis=1)
#     return fitness

def select_mating_pool(pop, fitnes, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitnes == numpy.max(fitnes))
        max_fitness_idx = max_fitness_idx[0][0]
        print("max_fitness_idx:")
        print(max_fitness_idx)
        parents[parent_num, :] = pop[max_fitness_idx, :]
        print(parents)
        print(fitnes[max_fitness_idx])
        fitnes[max_fitness_idx] = 0
    return parents

def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually it is at the center.
    crossover_point = numpy.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        # Index of the first parent to mate.
        parent1_idx = k%parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k+1)%parents.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
    return offspring_crossover


def fitness_test(list1):
    s = len(list1)
    count = 0
    alpha = 0.00000006
    beta  = 0.000000045
    gamma = 0.000000135 
    #to count relay nodes
    for i in list1:
        if i is 1:
            count+= 1
            
    print("c::", count)
    c=count #c= total no. of relay nodes
    t=0
    sum =0
    #count all the nodes
    for i in range(s):
        t= t + i +1
        if list1[i] is 1:
            sum = sum + i + 1  #i+1 is distance from sink to relay node
    print("t::",t)
    print("sum::",sum)
    k=sum/t  #summation part
    print("k::",k)
    fit =  (alpha* abs(s-c)) - (beta*k)
    print("fitness::")
    print(fit)
    return fit