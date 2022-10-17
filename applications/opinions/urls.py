from django.urls import path
from .views import OpinionsUserAPIView, ListOpinion, getAverage

urlpatterns = [
    path('api/opinions/', OpinionsUserAPIView.as_view()),
    path('api/listOpinions/', ListOpinion.as_view()),
    path('api/getAverage/', getAverage),
]