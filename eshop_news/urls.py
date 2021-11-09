from django.urls import path
from .views import NewsList, news_detail

app_name = "eshop_news"

urlpatterns = [

    path('', NewsList.as_view(), name='home_news'),
    path('<news_id>/<title>', news_detail, name='news-detail'),

]
