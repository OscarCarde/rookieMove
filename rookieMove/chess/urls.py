from django.urls import path
from . import views

urlpatterns = [
    #placeholder pattern to render the board template, may be replaced by a class based view laterI
    path("", views.board, name = "board")
]