# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import cm

total_population = 10000

beta = 0.3   # probability of infection by contact
gamma = 0.05 # probability of recovery

vaccination_rate = 0
legends = []
while vaccination_rate <= 1:
    infected = [1] # infected population
    immune = [int(vaccination_rate * total_population)] # immune population
    susceptible = [total_population - infected[0] - immune[0]] # susceptible population

    for time_step in range(1000):
        pr_contact = infected[time_step] / total_population
        pr_infection = pr_contact * beta

        new_infected = np.sum(np.random.choice([0, 1], susceptible[time_step], p=[1-pr_infection, pr_infection]))
        new_recovered = np.sum(np.random.choice([0, 1], infected[time_step], p=[1-gamma, gamma]))
        
        infected.append(infected[time_step] + new_infected - new_recovered)
        immune.append(immune[time_step] + new_recovered)
        susceptible.append(susceptible[time_step] - new_infected)

    plt.plot(infected)
    legends.append('{:.0%}'.format(vaccination_rate))
    vaccination_rate += 0.1


plt.legend(legends, loc='upper right')
plt.title('SIR model with different vaccination rates')
plt.xlabel('time course')
plt.ylabel('number of people')