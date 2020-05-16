# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# status markers
susceptible = 0
infected = 1
recovered = 2
marked_infected = -1 # will update to non-marked at the end of each time step
marked_recovered = -2

population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = infected # patient zero

# draw first figure
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.savefig('Step0.png', type='png')

beta = 0.3 # probability of infection by contact
gamma = 0.02 # probability of recovery

for time_step in range(1, 101):
    for x in range(100):
        for y in range(100):
            if population[x, y] == infected:
                for neibour_x in range(max(0, x-1), min(100, x+2)): # considering boundary problems
                    for neibour_y in range(max(0, y-1), min(100, y+2)):
                        # don't infect self; infect susceptible neibours
                        if (neibour_x, neibour_y) != (x, y) and population[neibour_x, neibour_y] == susceptible:
                            population[neibour_x, neibour_y] = np.random.choice([susceptible, marked_infected], p=[1-beta, beta])
                # recover
                population[x, y] = np.random.choice([infected, marked_recovered], p=[1-gamma, gamma])
    
    for x in range(100):
        for y in range(100):
            population[x, y] = abs(population[x, y]) # unmark
    
    if time_step in [10, 50, 100]:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.savefig('Step{0}.png'.format(time_step), type='png')