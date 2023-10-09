actors = [
    "Brad Pitt",
    "Meryl Streep",
    "Leonardo DiCaprio",
    "Cate Blanchett",
    "Tom Hanks",
    "Jennifer Lawrence",
    "Robert De Niro",
    "Julia Roberts",
    "Johnny Depp",
    "Nicole Kidman",
    "Denzel Washington",
    "Angelina Jolie",
    "George Clooney",
    "Kate Winslet",
    "Daniel Day-Lewis",
    "Charlize Theron",
    "Morgan Freeman",
    "Natalie Portman",
    "Hugh Jackman",
    "Emma Stone"
]

actors_list = []
cnt = 2
for actor in actors:
    actors_list.append({"actor_id":f"actor_{cnt}", "name":actor})
    cnt += 1




# script for director
# directors_list = [
#     "Director 1"
# ]

directors_list = [
    "Quentin Tarantino",
    "Steven Spielberg",
    "Martin Scorsese",
    "Woody Allen",
    "David O. Russell",
    "Tim Burton",
    "Baz Luhrmann",
    "Spike Lee",
    "Clint Eastwood",
    "Paul Thomas Anderson",
    "George Miller",
    "Christopher Nolan",
    "Gore Verbinski",
    "Ron Howard",
    "James Cameron",
    "Darren Aronofsky",
    "Damien Chazelle"
]



# Script for movies
movies_list = [
    {
        "movie_id": "movie_1",
        "name": "Movie 1",
        "actors": [
            {
                "actor_id": "actor_1",
                "role": "hero",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "12.3",
        "release_date": "2020-3-3",
        "director_name": "Director 1"
    }
]


import random

movies_list = []
movie_ids = []

tf = [True, False]

for i in range(2,33):
    movie_id = f"movie_{i+1}"
    movie_ids.append(movie_id)
    movie_name = f"Movie {i+1}"
    director_name = random.choice(directors_list)
    actor1 = {"actor_name": random.choice(actors), "role": "hero", "is_debut_movie": random.choice(tf)}
    actor2 = {"actor_name": random.choice(actors), "role": "heroine", "is_debut_movie": random.choice(tf)}
    actors = [actor1, actor2]
    box_office_collection = round(random.uniform(50, 500), 1)
    release_date = f"20{random.randint(10, 21)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    
    movie = {
        "movie_id": movie_id,
        "name": movie_name,
        "actors": actors,
        "box_office_collection_in_crores": str(box_office_collection),
        "release_date": release_date,
        "director_name": director_name
    }
    
    movies_list.append(movie)

# print(movies_list)




# script for ratings 
movie_rating_list = [
    {
        "movie_id": "movie_1",
        "rating_one_count": 4,
        "rating_two_count": 4,
        "rating_three_count": 4,
        "rating_four_count": 4,
        "rating_five_count": 4,
    }
]

movie_rating_list = []
idx = 0
for i in range(2,33):
    movie_id = movie_ids[idx]
    idx += 1
    rating = {
        "movie_id": movie_id,
        "rating_one_count": random.randint(5,5000),
        "rating_two_count": random.randint(5,5000),
        "rating_three_count": random.randint(5,5000),
        "rating_four_count": random.randint(5,5000),
        "rating_five_count": random.randint(5,5000),
    }
    movie_rating_list.append(rating)

# print(movie_rating_list)
