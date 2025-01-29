from django.urls import path,include
#from imdb_first.api.views import movie_list,movie_detail
from imdb_first.api.views import (WatchDetailAV,WatchListAV,StreamPlatformAV,StreamPlatformDetailAV,
                                  ReviewList,ReviewDetail)

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='Watch-list'),
    path('<int:pk>',WatchDetailAV.as_view(),name='Watch-detail'),
    path('stream/',StreamPlatformAV.as_view(),name='Watch-detail'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='Watch-detail'),
    path('review',ReviewList.as_view(),name='Reviews-detail'),
    path('review/<int:pk>',ReviewDetail.as_view(),name='Review-detail')
]
