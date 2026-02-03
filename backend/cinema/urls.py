from django.contrib import admin
from django.urls import path
from movies.views import movie_list, movie_detail
from showtimes.views import session_seats

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", movie_list, name="home"),
    path("movies/<int:movie_id>/", movie_detail, name="movie-detail"),
    path("showtime/<int:id>/seats/", session_seats, name="session_seats"),
    path("<int:movie_id>/", movie_detail),

]
