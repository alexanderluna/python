import webbrowser

class Movie():
    def __init__(self, title, storyline, image, trailer):
        self.title = title
        self.storyline = storyline
        self.image = image
        self.trailer = trailer

    def show_trailer(self):
        print(self.trailer)
        webbrowser.open("https://www.youtube.com/watch?v=KYz2wyBy3kc")



toy_story = Movie(  "Toy Story",
                    "a movie about toys",
                    "toy.jpg",
                    "https://www.youtube.com/watch?v=KYz2wyBy3kc")


webbrowser.open("https://www.youtube.com/watch?v=KYz2wyBy3kc")
