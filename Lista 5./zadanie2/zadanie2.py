# Author: Patrycja Paradowska
# 2 maja 2020r. Lista 5. Python, Zadanie 2.
# Napisac program, ktory na podstawie preferencji uzytkownika bedzie
# rekomendowal filmy, ktore najprawdopodobniej mu sie spodobaja.

import csv
import numpy
import pandas

def representation_of_movie(a, b, titles_of_films):
    z = numpy.dot(a, numpy.nan_to_num(b/numpy.linalg.norm(b, axis=None)))
    z = numpy.nan_to_num(z/numpy.linalg.norm(z, axis=None))
    outcome = numpy.dot(a.T, z)
    return [(outcome[i, 0], titles_of_films.loc[titles_of_films['movieId'] == i + 1]['title'].item())
            for i in range(outcome.shape[0]) if titles_of_films['movieId'].isin([i + 1]).any()]

def creating_rating_matrix(a, b, file):
    outcome = numpy.zeros((b, a))
    with open(file, newline='') as csv_file:
        file_csv = csv.DictReader(csv_file)
        for r in file_csv:
            movieid = int(r['movieId']) - 1
            if movieid <= a:
                userid = int(r['userId']) - 1
                outcome[userid, movieid] = float(r['rating'])
    return outcome

if __name__ == '__main__':
    numpy.seterr(divide='ignore', invalid='ignore')
    ratings = '../ml-latest-small/ratings.csv'
    movies = '../ml-latest-small/movies.csv'

    d = creating_rating_matrix(9018, 610, ratings)
    x = pandas.read_csv(movies)
    films = x.loc[x['movieId'] < 10000]
    d = numpy.nan_to_num(d / numpy.linalg.norm(d, axis=0))

    user_ratings = numpy.zeros((9018, 1))
    user_ratings[2570] = 5     # Matrix
    user_ratings[31] = 4       # Twelve Monkeys
    user_ratings[259] = 5      # Star Wars IV
    user_ratings[1096] = 4

    recommendations = sorted(representation_of_movie(d, user_ratings, films), key=lambda x: x[0], reverse=True)
    print("Wynik rekomendacji po posortowaniu (najlepsze 20 wynikow): ")
    print()
    for i in range(20):
        print(recommendations[i])