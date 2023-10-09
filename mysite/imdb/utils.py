from .models import Actor, Director, Movie, Rating, Cast
from django.db.models import Q
from datetime import date


def populate_database(
        actors_list, movies_list, directors_list, movie_rating_list):
    for actor in actors_list:
        try:
            Actor.objects.create(
                actor_id=actor["actor_id"], name=actor['name'])
        except:
            pass

    for director in directors_list:
        try:
            Director.objects.create(name=director)
        except:
            pass

    for movie in movies_list:
        date_feilds = list(map(int, movie['release_date'].split('-')))
        release_date_obj = date(*date_feilds)

        movie_director = Director.objects.get(name=movie['director_name'])

        try:
            Movie.objects.create(movie_id=movie['movie_id'], name=movie['name'],
                                 box_office_collection_in_crores=movie[
                'box_office_collection_in_crores'], release_date=release_date_obj,
                director=movie_director,
            )
        except:
            pass

        movie_obj = Movie.objects.get(movie_id=movie['movie_id'])
        for actor in movie['actors']:
            actor_obj = Actor.objects.get(actor_id=actor['actor_id'])
            Cast.objects.create(actor=actor_obj, movie=movie_obj,
                                role=actor['role'], is_debut_movie=actor['is_debut_movie'])

    for rating in movie_rating_list:
        movie_obj = Movie.objects.get(movie_id=rating['movie_id'])
        Rating.objects.create(movie=movie_obj, rating_one_count=rating['rating_one_count'], rating_two_count=rating['rating_two_count'],
                              rating_three_count=rating['rating_three_count'], rating_four_count=rating['rating_four_count'], rating_five_count=rating['rating_five_count'])


# populate_database(actors_list, movies_list, directors_list, movie_rating_list)
a = 10


def get_no_of_distinct_movies_actor_acted(actor_id):
    """
    :param actor_id: 'actor_1'
    :return:
    Number of movies he/she acted
        Sample Output: 4
    """
    movie_count = 0
    cast_query = Cast.objects.filter(actor_id=actor_id)
    for _ in cast_query:
        movie_count += 1
    return movie_count

# Test
# print(get_no_of_distinct_movies_actor_acted("actor_1"))


def get_movies_directed_by_director(director_obj):
    """
    :param director_obj: <Director: Director 1>
    :return:
    List of movie objects
    Sample Output: [<Movie: movie_1_obj>, <Movie: movie_2_obj>]
    """
    movie_count = 0
    movie_query = Movie.objects.filter(director=director_obj)
    for _ in movie_query:
        movie_count += 1
    return movie_count

# Test
# dir_obj = Director.objects.get(name="Quentin Tarantino")
# print(get_movies_directed_by_director(dir_obj))


def get_average_rating_of_movie(movie_obj):
    """
    :param movie_obj: <Movie: movie_1>
    :return:
    Average Rating
    Sample Output: 4.5
    """
    try:
        movie_rating = Rating.objects.get(movie=movie_obj)
    except Rating.DoesNotExist:
        return 0
    # average rating = 5*r5 + 4*r4 .../ r5 + r4 + ..
    r5 = movie_rating.rating_five_count
    r4 = movie_rating.rating_four_count
    r3 = movie_rating.rating_three_count
    r2 = movie_rating.rating_two_count
    r1 = movie_rating.rating_one_count

    total_votes = r5 + r4 + r3 + r2 + r1

    average_rating = (r5*5 + r4*4 + r3*3 + r2*2 + r1)/total_votes
    return round(average_rating, 1)

# Test
# test_movie = Movie.objects.get(movie_id='movie_3')
# print(get_average_rating_of_movie(test_movie))


def delete_movie_rating(movie_obj):
    """
    :param movie_obj: <Movie: movie_1>
    :return:
    """
    try:
        movie_rating = Rating.objects.get(movie=movie_obj)
    except Rating.DoesNotExist:
        return
    movie_rating.delete()

# Test
# test_movie = Movie.objects.get(movie_id='movie_4')
# print(delete_movie_rating(test_movie))


def get_all_actor_objects_acted_in_given_movies(movie_objs):
    """
    :param movie_objs: [<Movie: movie_1>, <Movie: movie_2>, ..]
    :return:
    List of actor objects
    Sample Output: [<Actor: actor_1>, <Actor: actor_2>, ..]
    """
    actors = []
    for movie_obj in movie_objs:
        movie_casts = Cast.objects.filter(movie=movie_obj)
        for movie_cast in movie_casts:
            actors.append(movie_cast.actor)
    return actors

# Test
# test_movie1 = Movie.objects.get(movie_id='movie_4')
# test_movie2 = Movie.objects.get(movie_id='movie_3')
# movie_arr = [test_movie1, test_movie2]
# print(get_all_actor_objects_acted_in_given_movies(movie_arr))


def update_director_for_given_movie(movie_obj, director_obj):
    """
    :param movie_obj: <Movie movie_1>
    :param director_obj: <Director: Director 1>
    :return:
    """
    movie_obj.director = director_obj
    movie_obj.save()

# Test
# movie_obj = Movie.objects.get(movie_id="movie_3")
# director_obj = Director.objects.get(name="Tim Burton")
# print(update_director_for_given_movie(movie_obj, director_obj))


def get_distinct_movies_acted_by_actor_whose_name_contains_john():
    """
    :return:
    movie_objs: [<Movie movie_1>, <Movie movie_2>, ..]
    """
    movies_list = set()
    actors_list = Actor.objects.filter(name__contains='John')
    for actor_obj in actors_list:
        cast_list = Cast.objects.filter(actor=actor_obj)
        for cast in cast_list:
            movies_list.add(cast.movie)
    return list(movies_list)

# Test
# print(get_distinct_movies_acted_by_actor_whose_name_contains_john())


def remove_all_actors_from_given_movie(movie_obj):
    """
    :param movie_obj: <Movie: movie_1>
    :return:
    """


def get_all_rating_objects_for_given_movies(movie_objs):
    """
    :param movie_objs: [<Movie: movie_1>, <Movie: movie_2>, <Movie: movie_3>,..]
    :return:
    rating_objs: [<Rating: rating_1>, <Rating: rating_2>, ..]
    """
    ratings_list = []
    for movie_obj in movie_objs:
        try:
            rating_obj = Rating.objects.get(movie=movie_obj)
            ratings_list.append(rating_obj)
        except:
            pass
    return ratings_list

# Test
# test_movie1 = Movie.objects.get(movie_id='movie_4')
# test_movie2 = Movie.objects.get(movie_id='movie_10')
# test_movie3 = Movie.objects.get(movie_id='movie_15')
# test_movie4 = Movie.objects.get(movie_id='movie_12')
# movie_arr = [test_movie1, test_movie2, test_movie3, test_movie4]
# print(get_all_rating_objects_for_given_movies(movie_arr))


def get_movies_by_given_movie_names(movie_names):
    """
    :return:
    [{
        "movie_id": 1,
        "name": "Titanic",
        "cast": [
            {
                "actor": {
                    "name": "Kate Winslet",
                    "actor_id": 1
                },
                "role": "Lead Actress",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "218.7",
        "release_date": "1997-11-18",
        "director_name": "James Cameron",
        "average_rating": 4.9,
        "total_number_of_ratings": 1000
    }]
    """
    details_objs = []
    for movie_name in movie_names:
        details_obj = {}
        movie_obj = Movie.objects.get(name=movie_name)
        details_obj['movie_id'] = movie_obj.movie_id
        details_obj['name'] = movie_obj.name
        details_obj['release_date'] = str(movie_obj.release_date)
        details_obj['box_office_collection_in_crores'] = movie_obj.box_office_collection_in_crores
        details_obj['director_name'] = movie_obj.director.name
        details_obj['average_rating'] = get_average_rating_of_movie(movie_obj)

        try:
            movie_rating = Rating.objects.get(movie=movie_obj)
        except Rating.DoesNotExist:
            details_obj['total_number_of_ratings'] = 0
        else:
            r5 = movie_rating.rating_five_count
            r4 = movie_rating.rating_four_count
            r3 = movie_rating.rating_three_count
            r2 = movie_rating.rating_two_count
            r1 = movie_rating.rating_one_count

            total_votes = r5 + r4 + r3 + r2 + r1
            details_obj['total_number_of_ratings'] = total_votes

        cast_objs = Cast.objects.filter(movie=movie_obj)
        detail_casts_list = []

        for cast_obj in cast_objs:
            details_cast_obj = {}
            details_cast_obj['role'] = cast_obj.role
            details_cast_obj['is_debut_movie'] = cast_obj.is_debut_movie

            details_cast_actor_obj = {}
            details_cast_actor_obj['actor_id'] = cast_obj.actor.actor_id
            details_cast_actor_obj['name'] = cast_obj.actor.name

            details_cast_obj['actor'] = details_cast_actor_obj
            detail_casts_list.append(details_cast_obj)

        details_obj['cast'] = detail_casts_list
        details_objs.append(details_obj)

    return details_objs

# print(get_movies_by_given_movie_names(["The Avengers"]))


def get_movies_released_in_summer_in_given_years(years):
    """
    :param years_list: [2024,..]
    :return: movie dict as in task 1
    """
    movie_details = []
    movie_objs = Movie.objects.filter(release_date__year__in=years)
    for movie_obj in movie_objs:
        details_list = get_movies_by_given_movie_names([movie_obj.name])
        movie_details.append(details_list[0])
    return movie_details

# Test
# print(get_movies_released_in_summer_in_given_years([2020,2019]))


def get_movie_names_with_actor_name_ending_with_smith():
    """
    :return:
    ["The Pursuit of Happyness", "Aladdin"] 
    """
    actor_list = Actor.objects.filter(name__iendswith='smith')
    movie_names = []
    cast_list = Cast.objects.filter(actor__in=actor_list)
    for cast in cast_list:
        movie_names.append(cast.movie.name)
    return movie_names


def get_movie_names_with_ratings_in_given_range():
    """
    :return:
    ["Avengers, End Game", "The Iron Man, Part 3"]
    """
    # [1000, 3000] 5 star rating
    return [rating.movie.name for rating in Rating.objects.filter(rating_five_count__gte=1000, rating_five_count__lte=3000)]


def get_movie_names_with_ratings_above_given_minimum():
    """
    :return:["Avengers, End Game", "The Iron Man, Part 3"]
    """
    # year > 2000 and 5* >= 500 or 4* >= 1000 or 3* >= 2000 or
    # 2* >= 4000 or 1* >= 8000

    movies2020_list = Movie.objects.filter(release_date__year__gt=2000)
    ratings_list = Rating.objects.filter(Q(movie__release_date__year__gt=2000) & Q(rating_five_count__gte=500) | Q(
        rating_four_count__gte=1000) | Q(rating_three_count__gte=2000) | Q(rating_two_count__gte=4000) | Q(rating_one_count__gte=8000)).values_list('movie__name',flat=True)

    return list(ratings_list)


def get_movie_directors_in_given_year():
    """
    :return:
    ["Trivikram Srinivas"]
    """
    movies2020_list = Movie.objects.filter(release_date__year=2010)
    directors = set()
    for movie in movies2020_list:
        directors.add(movie.director.name)
    return list(directors)


def get_actor_names_debuted_in_21st_century():
    """
    :return:
    ["VD"]
    """
    movies2020_list = Movie.objects.filter(release_date__year__gt=2000)
    cast_list = Cast.objects.filter(Q(movie__in=movies2020_list) & Q(is_debut_movie=True))
    return [ cast.actor.name for cast in cast_list]


def get_director_names_containing_big_as_well_as_movie_in_may():
    """
    :return:
    ["James Cameron"]
    """
    movies_list = Movie.objects.filter(Q(name__icontains='b') | Q(release_date__month=9))
    return [ movie.name for movie in movies_list]


def get_director_names_containing_big_and_movie_in_may():
    """
    :return:
    ["James Cameron"]
    """
    movies_list = Movie.objects.filter(Q(name__icontains='b') & Q(release_date__month=9))
    return [ movie.name for movie in movies_list]



def reset_ratings_for_movies_in_this_year():
    """
    """
    rating_list = Rating.objects.filter(Q(movie__release_date__year=2010))
    for rating in rating_list:
        rating.rating_five_count = 0
        rating.rating_four_count = 0
        rating.rating_three_count = 0
        rating.rating_two_count = 0
        rating.rating_one_count = 0
        rating.save()
    return list(rating_list)

##### Asssigment004 ##########

def get_average_box_office_collections():
    """
    :return: float value
    100.123
    """
    movie_list = Movie.objects.all()
    total_collection_in_crores = 0
    number_of_movies = 0
    for movie in movie_list:
        total_collection_in_crores += movie.box_office_collection_in_crores
        number_of_movies += 1
    
    return round(total_collection_in_crores/number_of_movies, 3)
    
    

def get_movies_with_distinct_actors_count():
    """
    :return: a list of Movie model instances
    """
    

def get_male_and_female_actors_count_for_each_movie():
    """
    :return: a list of Movie model instances
    """

def get_roles_count_for_each_movie():
    """
    :return:
    ["Avengers, End Game", "The Iron Man, Part 3"]
    """

def get_role_frequency():
    """
    :return: {
    "role_1": 3,
    "role_2": 5
    }
    """

def get_role_frequency_in_order():
    """
    :return: [('role_2', 5), ('role_1', 3)]

    """

def get_no_of_movies_and_distinct_roles_for_each_actor():
    """
    :return: a list of Movie model instances
    """

def get_movies_with_atleast_forty_actors():
    """
    :return: a list of Movie model instances
    """

def get_average_no_of_actors_for_all_movies():
    """
    :return: 4.123
    """
