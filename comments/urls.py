from django.contrib import admin
from django.urls import path
from comments import views

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
    path("comment_list/", views.comment_list, name="comment_list"), 
    path("comment_detail/<int:post_id>/", views.comment_detail, name="comment_detail"),
    path("comment_update/<int:id>/", views.comment_update, name="comment_update"),
    path("comment_delete/<int:id>/", views.comment_delete, name="comment_delete"), 
    path('resume/', views.resume_view, name='resume'),
]