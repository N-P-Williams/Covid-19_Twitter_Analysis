import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from collections import OrderedDict
import pandas as pd

date_occur = OrderedDict()
dates = list()
nums = list()
with open('Clean_Data/virus_data.csv', mode='r') as f:
    for line in f:
        if line == '\n':  #skips empty lines
            continue
        else:
            line.strip('\n')
            date, num = line.split(',')
            date_occur[date] = num
            dates.append(pd.to_datetime(date))  # conver to datetime type for matplotlib
            nums.append(int(num))


fig, ax = plt.subplots()
plt.scatter(dates, nums, s=10)  # plot set size of dots to 10
ax.xaxis.set_minor_locator(AutoMinorLocator())  # set minor ticks for x axis
ax.yaxis.set_minor_locator(AutoMinorLocator())  # set minor ticks for y axis
plt.title(label='Keyword: Virus')
plt.xlabel(xlabel='Date')
plt.ylabel(ylabel='Number of occurrences')
plt.show()
