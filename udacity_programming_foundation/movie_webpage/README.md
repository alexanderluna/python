# Movie Website [(View Source)](movie_class.py)

__Task: Build a movie website using a movie class to store: title, storyline, image and trailer and display them with a click__

Planning the program outline

```
import libraries

create class
init class and properties
create movie trailer method
```

In a separate model file:

```
import movie class
create movie list
render HTML
```

create movie class

```
class Movie():
    __init__(self, title, storyline, image, video):
        self.title = title
        self.storyline = storyline
        self.image = image
        self.video_url = video_url
```

create model:

```
import movie_class

toy_story = movie_class.Movie(  "Toy Story",
                    "a movie about toys",
                    "https://static.rogerebert.com/uploads/movie/movie_poster/toy-story-1995/large_agy8DheVu5zpQFbXfAdvYivF2FU.jpg",
                    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

```

Render website:

```
import fresh_tomatoes

fresh_tomatoes.open_movies_page(movie_list)

```
