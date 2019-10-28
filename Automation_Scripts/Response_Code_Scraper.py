import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from collections import Counter
import http.client
import random as rand
​
statusCodes = {}
statusCodeCounts = []
labels = []
colors = []
chartColors = []
# The with statement handles opening and closing the file, including if an exception is raised in the inner block. 
# The 'for line in f' treats the file object f as an iterable, which automatically uses buffered I/O and memory management,
# so you don’t have to worry about large files. This implementation has no problem with TeraByte and larger files.
with open('access.log','r') as f:
    for line in f:
        statusCode = line.split(' ')[8]
        if statusCode in statusCodes:
            statusCodes[statusCode] += 1
        else:
            statusCodes[statusCode] = 1
    count = Counter(statusCodes)    # A performant construct that counts the occurences of each element in the list and creates a mapping
​
# Mapping codes to the appropriate messages
for ele in count:
    labels.append(ele + ' ' + http.client.responses[int(ele)])
    statusCodeCounts.append(count[ele])
​
# Load up all of the color pallette to select from randomly
for color in mcolors.CSS4_COLORS:
    colors.append(color)
numColors = len(colors)
​
# Randomly generate colors for the pie chart from the 148 possibilities
# There are 58 supported, IANA-registered status codes available so we are covered
for i in range(len(labels)):
    newColor = colors[rand.randint(0, numColors-1)]
    chartColors.append(newColor)
    colors.remove(newColor)
    numColors -= 1
​
# Dynamically create the right tuple to make the first pie slice 'pop'
explode = [0.1]
for i in range(1, len(labels)):
    explode.append(0)    
explode = tuple(explode) 
​
# Plot
plt.pie(statusCodeCounts, explode=explode, labels=labels, colors=chartColors, autopct='%1.1f%%', shadow=True, startangle=160)
plt.axis('equal')
plt.show()