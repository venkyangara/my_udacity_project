import webbrowser


class Movie():

    """ This class helps define the attributes of a movie """
    # A constructor that take movie title, storyline , poster url
    # and youtube url as parameters
    def __init__(self, movie_title, movie_storyline, poster_url, youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url

    # show_trailer() fun when called opens the webbrowser to play the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


# A check to see if this module is called directly.
if __name__ == "__main__":
    print("Meant to be imported not executed")
