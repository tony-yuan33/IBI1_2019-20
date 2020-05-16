# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

total_population = 10000
infected = [1]
recovered = [0]
susceptible = [total_population - infected[0] - recovered[0]]

beta = 0.3   # probability of infection by contact
gamma = 0.05 # probability of recovery

for time_step in range(1000):
    pr_contact = infected[time_step] / total_population
    pr_infection = pr_contact * beta

    new_infected = np.sum(np.random.choice([0, 1], susceptible[time_step], p=[1-pr_infection, pr_infection]))
    new_recovered = np.sum(np.random.choice([0, 1], infected[time_step], p=[1-gamma, gamma]))
    
    infected.append(infected[time_step] + new_infected - new_recovered)
    recovered.append(recovered[time_step] + new_recovered)
    susceptible.append(susceptible[time_step] - new_infected)

plt.plot(susceptible)
plt.plot(infected)
plt.plot(recovered)
plt.legend(('susceptible', 'infected', 'recovered'), loc='upper right')
plt.title('SIR model')
plt.xlabel('time course')
plt.ylabel('number of people')