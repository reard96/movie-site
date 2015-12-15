import fresh_tomatoes
# so that we can put all of this in a nice-looking web page
import media
# need the Movie class that we defined 


basterds = media.Movie("Inglourious Basterds", 
					   "Band of vigilante Americans hunt Nazis.",
				       "http://www.gstatic.com/tv/thumb/movieposters/193875/p193875_p_v7_af.jpg",
				       "https://www.youtube.com/watch?v=6AtLlVNsuAc")

inception = media.Movie("Inception", 
						"Is this all just a dream?",
						"http://resizing.flixster.com/l5I-Yk--UFS2Nrq_GJmKcWzRZ7M=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/16/67/11166725_ori.jpg",
						"https://www.youtube.com/watch?v=8hP9D6kZseM")

jeff = media.Movie("Jeff, Who Lives at Home", 
				   "Should we put our faith in signs from the universe?",
				   "http://www.gstatic.com/tv/thumb/movieposters/8855648/p8855648_p_v7_aa.jpg",
				   "https://www.youtube.com/watch?v=34kCWAsddtA")

italian = media.Movie("The Italian Job", 
					  "Thieves who were crossed get payback.",
					  "http://www.gstatic.com/tv/thumb/movieposters/32134/p32134_p_v7_aa.jpg",
					  "https://www.youtube.com/watch?v=5Eyw-Qiwpj0")

ferriss = media.Movie("Ferris Bueller's Day Off", 
					  "The best sick day ever.",
					  "http://www.gstatic.com/tv/thumb/movieposters/9316/p9316_p_v7_aa.jpg",
					  "https://www.youtube.com/watch?v=ik0y8yWw7jU")

furious = media.Movie("Fast Five", 
					  "Heist in Rio involving some sexy automobiles.",
					  "http://t1.gstatic.com/images?q=tbn:ANd9GcR9Y8JHdp2nSaGCT7RfryzQtCLmJgDDkV77IHKa1hXnQpaDfpDX",
					  "https://www.youtube.com/watch?v=tPZfa7bZzF4")

# My favorite movies and their info that we defined in Movie class 

movies = [basterds, inception, jeff, italian, ferriss, furious]
# create list of the movies to populate web page with

fresh_tomatoes.open_movies_page(movies)
# launches the web page using the function in the fresh_tomatoes file