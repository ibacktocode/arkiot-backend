from django.conf.urls import url
# from .views import MovieListAPIView, MovieDetailAPIView, MovieCreateAPIView, MovieUpdateAPIView, MovieDeleteAPIView, MovieList, MovieDetail

# urlpatterns = [
#     # url(r'^$', MovieListAPIView.as_view()),
#     url(r'^$', MovieList.as_view(),name='movie-list'),
#     url(r'^(?P<pk>\d+)/$', MovieDetail.as_view(), name='movie-detail'),
#     url(r'^create/$', MovieCreateAPIView.as_view()),
#     url(r'^(?P<pk>\d+)/edit/$', MovieUpdateAPIView.as_view()),
#     url(r'^(?P<pk>\d+)/delete/$', MovieDeleteAPIView.as_view()),
# ]