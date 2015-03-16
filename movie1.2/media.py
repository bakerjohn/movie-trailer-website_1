import webbrowser
# Imports Modules from other Python Packages
# Our Class name is "Movie". All instances realted to Movie will fall into this Class


class Movie():
# Instance methods __init__ and show_trailer
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# show_trailer method will display the "youtube" trailer for each instance in a webbrowser        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

        
