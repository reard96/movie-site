import webbrowser
# So that we can grab the trailers from YouTube

class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
	# creates the different elements of our Movie class
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
	# need a function to show the trailer for movies
		webbrowser.open(self.trailer_youtube_url)
