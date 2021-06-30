from django.urls import path
from app.views import index, index_tree, index_two


urlpatterns = [
    path('', index, name="index"),
    path('index_two/', index_two, name="index_two"),
    path('index_tree/', index_tree, name="index_tree")
]
