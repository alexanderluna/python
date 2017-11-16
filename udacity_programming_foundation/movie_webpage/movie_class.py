import webbrowser

class Movie():
    def __init__(self, title, storyline, image, video_url):
        self.title = title
        self.storyline = storyline
        self.image = image
        self.video_url = video_url


    def show_trailer(self):
        webbrowser.open(self.video_url)
