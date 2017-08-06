import media
#import fresh_tomatoes

harry = media.Movie("jab harry met sejal","a romantic comedy movie","https://en.wikipedia.org/wiki/File:JHMS2017.jpg","https://www.youtube.com/watch?v=W5MZevEH5Ns")

print(harry.storyline)
#harry.show_trailer()
movies = [harry]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.valid_ratings)
print(media.Movie.__doc__)