from django.contrib import admin
from .models import Actor, Director, Movie, Cast, Rating

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Rating)
admin.site.register(Cast)
admin.site.register(Movie)