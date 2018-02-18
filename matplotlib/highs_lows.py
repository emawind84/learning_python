#!/usr/bin/env python

from __future__ import print_function
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # for index, col_header in enumerate(header_row):
    #     print(index, col_header)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        highs.append(int(row[1]))
    # print(highs)

# plot data
fig = plt.figure(dpi=64, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# format plot
plt.title('Daily high temperatures, xxxx', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

fig.autofmt_xdate()

plt.locator_params(axis='x', nticks=10)
plt.show()