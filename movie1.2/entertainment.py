# Import media.py contains class "movie" for the instances.
import media
# Import "fresh_tomatoes" is a Web page module to run the website
import fresh_tomatoes



# Instances of Class "Movie"
star_wars = media.Movie("Star Wars",
                        "Good vs Evil in a galaxy far far way",
                        "http://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=93aQr6UkvGI")


A_Knights_Tale = media.Movie("A Knights Tale",
                     "A fishermans son becomes a knight",
                     "http://upload.wikimedia.org/wikipedia/en/a/a6/AKnightsTale.jpg",
                     "https://www.youtube.com/watch?v=zH6U5y086hw")


Dune = media.Movie("Dune",
                     "a savior arrives on a dessert Planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Duneposter.jpg",
                     "https://www.youtube.com/watch?v=aD0Vd-HRpN8")


Tron_Legacy = media.Movie("Tron Legacy",
                     "A sons search for his father in a dgitial universe",
                     "http://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
                     "https://www.youtube.com/watch?v=L9szn1QQfas")

Marvels_the_Avengers = media.Movie("Marvels the Avengers",
                     "the Avengers unite to save the world",
                     "http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                     "https://www.youtube.com/watch?v=eOrNdBpGMv8")


Limitless = media.Movie("Limitless",
                     "A drug makes a man powerful but at what price",
                     "http://upload.wikimedia.org/wikipedia/en/1/17/Limitless_Poster.jpg",
                     "https://www.youtube.com/watch?v=jOLqNOfzus4")


movies = [star_wars, A_Knights_Tale, Dune, Tron_Legacy, Marvels_the_Avengers, Limitless]

#opens website using content lay out from "fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
