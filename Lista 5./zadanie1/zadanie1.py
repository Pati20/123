# Author: Patrycja Paradowska
# 2 maja 2020r. Lista 5. Python, Zadanie 1.

import numpy
import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

read_ratings_from_csv = pandas.read_csv('../ml-latest-small/ratings.csv')[['userId', 'movieId', 'rating']].to_numpy()
toystory = read_ratings_from_csv[numpy.where(read_ratings_from_csv[:, 1] == 1)]

def generating_plot(number):
    X, Y = getting_rat(215, number)
    clf = LinearRegression().fit(X, Y)
    p = plt.scatter([i for i in range(0, 215)],
        [clf.predict([X[i]]) for i in range(0, 215)], alpha=0.5, c= 'yellow')
    real = plt.scatter([i for i in range(0, 215)],
        [Y[i] for i in range(0, 215)], alpha=0.5, c='pink')
    plt.legend((p, real), ('Predicted', 'Real'))
    plt.title(f"Wykres dla m = {number}")
    plt.savefig(f'wykres_dla_m_{number}.png')
    plt.clf()

def getting_rat(usr, films):
    m = numpy.zeros((usr, films))
    ratings = numpy.zeros(usr)
    idx = 0
    for i, rating in enumerate(toystory):
        if i > usr - 1:
            break
        curr_usr = rating[0]
        ratings[i] = rating[2]
        while idx < len(read_ratings_from_csv) and read_ratings_from_csv[idx][0] < curr_usr:
            idx = idx + 1
        while idx < len(read_ratings_from_csv) and read_ratings_from_csv[idx][0] == curr_usr:
            if read_ratings_from_csv[idx][1] - 2 >= 0 and \
                    read_ratings_from_csv[idx][1] - 2 < films:
                m[i][int(read_ratings_from_csv[idx][1] - 2)] = read_ratings_from_csv[idx][2]
            idx = idx + 1
    return m, ratings

if __name__ == '__main__':
    training_size = 200
    size = 215
    m_zad1a = [10, 1000, 10000]
    m_zad1b = [10, 100, 200, 500, 1000, 10000]
    for m in m_zad1a:
        generating_plot(m)
    for m in m_zad1b:
        print(f"REZULTAT PRZEWIDYWANIA DLA m = {m}:")
        X, Y = getting_rat(size, m)
        a = Y[0:training_size]
        b = X[0:training_size]
        clf = LinearRegression().fit(b, a)
        for i in range(training_size, size):
            print(f"{i+1}: predict value: {clf.predict([X[i]])}, correct value: {Y[i]}")
        print()