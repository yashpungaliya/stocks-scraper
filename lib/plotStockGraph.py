import os

import matplotlib.pyplot as plt
import csv
from datetime import datetime


def plot_graph(filename):
    x = []
    y = []
    p1 = os.path.abspath('..')
    foldername = datetime.now().strftime("%D")
    foldername = foldername.replace("/", "-")
    myPath = p1 + '/data/' + foldername
    with open(myPath+'/'+filename, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=';')
        for row in plots:
            x.append(float(row[1]))
            y.append(float(row[0]))
    #plt.scatter(x, y)
    plt.plot(x, y,linewidth=2.0, label='Stock Graph')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('MyGraph')
    plt.legend()
    plt.show()

