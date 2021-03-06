#!/usr/bin/env python
"""class where we will place our movies"""


import media
import fresh_tomatoes


# A list of movies
toy_story = media.Movie("Toy Story",
                        "Toy Story is about the 'secret life of toys'",
                        "https://goo.gl/XqPqLT",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                     "A marine turn into an alien",
                     "https://goo.gl/3WcdY8",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

matrix = media.Movie("The Matrix",
                     "Neo (-- What is the Matrix?",
                     "https://goo.gl/WRZBUz",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")

gladiator = media.Movie("Gladiator",
                        "A man coming back",
                        "https://goo.gl/qPivN8",
                        "https://youtu.be/owK1qxDselE")

taken = media.Movie("Taken",
                    "A Father girl kidnapped",
                    "https://goo.gl/6c1fYs",
                    "https://youtu.be/kZ02_Uzf7So")

brave_heart = media.Movie("BraveHeart",
                          "Epic war heart",
                          "https://goo.gl/93QUfP",
                          "https://youtu.be/nMft5QDOHek")
# an array with the movies listed
listofmovies = [toy_story, avatar, matrix, gladiator, taken, brave_heart]


fresh_tomatoes.open_movies_page(listofmovies)
