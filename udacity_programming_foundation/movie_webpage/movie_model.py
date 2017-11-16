import fresh_tomatoes
import movie_class

toy_story = movie_class.Movie(  "Toy Story",
                    "a movie about toys",
                    "https://static.rogerebert.com/uploads/movie/movie_poster/toy-story-1995/large_agy8DheVu5zpQFbXfAdvYivF2FU.jpg",
                    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

the_big_short = movie_class.Movie(  "The big short",
                        "In 2008, Wall Street guru Michael Burry realizes that a number of subprime home loans are in danger of defaulting. Burry bets against the housing market by throwing more than $1 billion of his investors' money into credit default swaps. His actions attract the attention of banker Jared Vennett",
                        "https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg",
                        "https://www.youtube.com/watch?v=vgqG3ITMv1Q")

movie_list = [toy_story, the_big_short]

fresh_tomatoes.open_movies_page(movie_list)
