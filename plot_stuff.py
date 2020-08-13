import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.ticker import AutoMinorLocator
from collections import OrderedDict
import pandas as pd


def plot_twitter_data():
    date_occur = OrderedDict()
    dates = list()
    nums = list()
    with open('Clean_Data/Utah_virus_data.csv', mode='r') as f:
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
    plt.title(label='Confirmed cases per day')
    plt.xlabel(xlabel='Date')
    plt.ylabel(ylabel='Number of cases')
    plt.show()


def plot_twitter_vs_cases():
    twitter_data = OrderedDict()
    cases_data = OrderedDict()
    with open('Matching_data/covid_data_matching.csv', mode='r') as f:
        for line in f:
            if line == '\n':
                continue
            else:
                line.strip('\n')
                date, num = line.split(',')
                twitter_data[date] = float(num)

    with open('Matching_data/cases_data_matching.csv', mode='r') as f:
        for line in f:
            if line == '\n':
                continue
            else:
                line.strip('\n')
                date, num = line.split(',')
                cases_data[date] = float(num)

    style.use('ggplot')
    fig, ax = plt.subplots()
    plt.scatter(cases_data.values(), twitter_data.values(), s=10)  # plot set size of dots to 10
    ax.xaxis.set_minor_locator(AutoMinorLocator())  # set minor ticks for x axis
    ax.yaxis.set_minor_locator(AutoMinorLocator())  # set minor ticks for y axis
    plt.title(label='Cases vs tweets mentioning "Covid"')
    plt.xlabel(xlabel='number of cases')
    plt.ylabel(ylabel='Number of tweets mentioning covid')
    plt.show()


if __name__ == '__main__':
    plot_twitter_vs_cases()
