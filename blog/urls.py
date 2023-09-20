from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('page/', views.my_view, name="page"),
    path('select/', views.select_board, name='select_board'),
    path('board/', views.board, name='board'),
    path('board2/', views.board2, name='board2'),
    path('board3/', views.board3, name='board3'),
]