import random

import numpy as np


class Movie:
    title = ""
    year = 0
    runTime = 0

    def __init__(self, title = "", year = 0, runTime = 0):
        self.title = title
        self.year = year
        if runTime >= 0:
            self.runTime = runTime

    def __repr__(self):
        return f"{self.title} ({self.year}) - {self.runTime} mins"

    def get_duration(self):
        hours = self.runTime // 60
        minutes = self.runTime % 60

        return hours, minutes


def create_movie_list():
    movie_list = [Movie("Jurassic World", 2015, 124),
                  Movie("Something", 2018, 130),
                  Movie("Whatever", 2017, 162),
                  Movie("Coca Cola", 2019, 155)]

    for i in movie_list:
        print(i)

    return movie_list


def get_movie_data():
    """
    Generate a numpy array of movie data
    :return:
    """
    num_movies = 10
    array = np.zeros([num_movies, 3], dtype=np.float)

    for i in range(num_movies):
        # There is nothing magic about 100 here, just didn't want ids
        # to match the row numbers
        movie_id = i + 100

        # Lets have the views range from 100-10000
        views = random.randint(100, 10000)
        stars = random.uniform(0, 5)

        array[i][0] = movie_id
        array[i][1] = views
        array[i][2] = stars

    return array


my_list = create_movie_list()

print("-------------------------")

movie = Movie("Jurassic World", 2015, 124)
print(movie)
print(movie.get_duration())

movie1 = Movie("", 0, -1)
print(movie1)

print("-------------------------")

new_list = [i for i in my_list if i.runTime > 150]
print(new_list)

print("-------------------------")

my_dict = {i.title: random.randrange(0, 6) for i in my_list}
print(my_dict)

print("-------------------------")

movie_data = get_movie_data()
# print(movie_data)
# print(movie_data.shape[0])
# print(movie_data.shape[1])
# print(movie_data[0, 1])
print(movie_data)

the_two_rows = movie_data[:2]

# print(movie_data[0:, -2:])
print(movie_data[:, 1])


