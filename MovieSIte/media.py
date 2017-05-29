import webbrowser

""" This docstring explain what the movie() class does """


class Movie():
    """ This docstring explains constructor method,
    it'sinputs and outputs if any """
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    """ This docstring explain what the show trailer function does """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

