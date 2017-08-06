import webbrowser

class Movie():
    """ this class stores movie related information"""
    valid_ratings = ["G", "PG", "R"]

    def __init__(self,movie_name,movie_storyline,movie_poster,movie_trailer):
        self.title = movie_name
        self.storyline = movie_storyline
        self.poster_url = movie_poster
        self.trailer_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_url)