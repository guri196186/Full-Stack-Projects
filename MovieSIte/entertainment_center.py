#!/usr/bin/env python
import fresh_tomatoes
import media

# create an instance of Toy Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy that come to life",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

# create an instance of Avatar Movie
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# create an instance of Hindi Medium Movie
hindi_medium = media.Movie("Hindi Medium",
                           "A couple want to give their daughter the best\
                           education so she will be accepted by the elite.",
                           "http://t3.gstatic.com/images?q=tbn:ANd9GcRERz4zBiMWPhnbk-xB-q7-s4Qfc6DiiEbY2DeUEjtwx-VtxKA3",
                           "https://youtu.be/GjkFr48jk68")

# create an instance of Lion Movie
lion = media.Movie("Lion",
                   "Story and journey of a lost boy.",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcTVuFTo4qf9v0c91rhTcSn25dsQygPhIRdivLe8Z1HdZNiPCj2F",
                   "https://www.youtube.com/watch?v=-RNI9o06vqo")

# create an instance of The other side of the door Movie
other_side = media.Movie("The other side of the door",
                         "The story of a women and his dead child",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcSp36dV7BbOnQztUsrXwt-6yFnel8sXzu23k7fwzxyZ3KO93Nsk",
                         "https://www.youtube.com/watch?v=C1HjOEubv2Y")

# create an instance of Bahubali Movie
bahubali = media.Movie("Bahubali-The conclusion",
                       "The son of Bahubali, begins to search for answers after he learns about his heritage",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                       "https://www.youtube.com/watch?v=G62HrubdD6o")

# create a list of movie instance
movies_list = [toy_story, avatar, hindi_medium, lion, other_side, bahubali]
# call the function to open movie page
fresh_tomatoes.open_movies_page(movies_list)

