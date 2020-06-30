import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

with open('utah_confirmed_usafacts.csv') as f:
    confirmed_by_county = {} ## Dict that has the County name as a the key and the numbers of cases in a list
    f_line = f.readline()
    data, date = f_line.split('stateFIPS')
    dates = date.split(',') ##puts all dates into a array that will match up to number of cases in the dict list
    for lines in f:
        temp_line = f.readline()
        temp_head, temp_dates = temp_line.split('UT')
        temp_data = temp_head.split(',')
        county = temp_data[1]
        dates_temp = temp_dates.split(',')
        dates_cleaned = dates_temp[2:] ##remove first empty element and the 49
        confirmed_by_county[county] = dates_cleaned

colors = list("rgbcmyk")

for data_dict in confirmed_by_county:
    num_dates = len(confirmed_by_county[data_dict])
    x = dates[0:num_dates]
    y = confirmed_by_county[data_dict]
    plt.scatter(x, y)

plt.legend(confirmed_by_county.keys())
plt.show()