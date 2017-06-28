import matplotlib.pyplot as plt
import csv


def plot_graph(filename):
    x = []
    y = []
    with open('./data/'+filename, 'r') as csvfile:
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

