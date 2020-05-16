# -*- coding: utf-8 -*-
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data:
covid_data = pd.read_csv('full_data.csv')

# Show all columns:
print(covid_data.iloc[:,:])

# Every third row between (and including) 0 and 15:
print(covid_data.iloc[0:16:3,:])

# Total cases in Afghanistan:
print(covid_data.loc[covid_data.loc[:,'location'] == 'Afghanistan', 'total_cases'])

world_dates = covid_data.loc[covid_data.loc[:,'location'] == 'World', 'date']
world_new_cases = covid_data.loc[covid_data.loc[:,'location'] == 'World', 'new_cases']
world_new_deaths = covid_data.loc[covid_data.loc[:,'location'] == 'World', 'new_deaths']

# World mean:
print(np.mean(world_new_cases))

# World median:
print(np.median(world_new_cases))

# Box plot of new world cases:
plt.figure(figsize=(2,4),dpi=100)
plt.boxplot(world_new_cases)
plt.title('New world cases')
plt.ylabel("Number of people")

# Plot new cases
plt.figure(figsize=(6,4),dpi=100)
plt.plot(world_dates, world_new_cases, 'ro')
plt.plot(world_dates, world_new_deaths, 'ko')
plt.legend(('New cases', 'New deaths'), loc='upper left')
plt.title('COVID-19 world pandemic trend')
plt.xlabel('Date')
plt.ylabel('Number of people')
plt.xticks(world_dates.iloc[::5], rotation=-90)

# Question: how has COVID-19 death rate worldwide changed over time?
world_cumulative_cases, world_cumulative_deaths= 0, 0
world_death_rates = [0]
for i in range(len(world_new_cases) - 1):
    world_cumulative_cases += world_new_cases.iloc[i]
    world_cumulative_deaths += world_new_deaths.iloc[i]
    world_death_rates.append(world_cumulative_deaths/world_cumulative_cases)

plt.figure(figsize=(6,4),dpi=100)
plt.plot(world_dates, world_death_rates, 'ro')
plt.title('COVID-19 world death rate trend')
plt.xlabel('Date')
plt.ylabel('Death rate')
plt.xticks(world_dates.iloc[::5], rotation=-90)