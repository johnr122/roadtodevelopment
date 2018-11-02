import media
import fresh_tomatoes
meet_the_robinsons = media.Movie("Meet the Robinsons", 
                                "Boy with the Big Dream",
                                "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-1c09hzd_35c8ee94.jpeg?region=0%2C0%2C1000%2C1409&quality=8", 
                                "https://www.youtube.com/watch?v=S396-fnLldk" )

UP = media.Movie("UP","Couple wanted to go to Paradise Falls",
                "https://static.rogerebert.com/uploads/review/primary_image/reviews/up-2009/hero_Up-2009.jpg",
                "https://www.youtube.com/watch?v=ORFWdXl_zJ4")

ratatouille = media.Movie("Ratatouille", "A rat that can cook good food.",
                        "http://www.gstatic.com/tv/thumb/v22vodart/165058/p165058_v_v8_ao.jpg",
                        "https://www.youtube.com/watch?v=e8GBfNo3IHY")

inside_out = media.Movie("Inside Out",
                        "Movie about emotions",
                        "https://i.ytimg.com/vi_webp/ttH5-pOLuwE/movieposter.webp",
                        "https://www.youtube.com/watch?v=seMwpP0yeu4")

zootopia = media.Movie("Zootopia",
                        "Animal World",
                        "https://i.ytimg.com/vi_webp/2qJBtiAcvtw/movieposter.webp",
                        "https://www.youtube.com/watch?v=jWM0ct-OLsM")

movies = [meet_the_robinsons, UP, ratatouille, inside_out, zootopia]
fresh_tomatoes.open_movies_page(movies)