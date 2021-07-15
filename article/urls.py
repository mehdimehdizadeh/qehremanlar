from django.contrib import admin
from django.urls import path
from article import views

app_name = "article"

urlpatterns = [
    path('article/<int:id>',views.detail,name="detail"),
    path('category/<int:id>',views.category,name="category"),
]
