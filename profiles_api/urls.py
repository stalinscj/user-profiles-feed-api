from django.urls import path

from profiles_api import views

# Create your urls here.

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
