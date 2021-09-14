from django.urls import path
from front import views

urlpatterns = [
path('index/', views.index, name='index'),
path('signup/', views.signup, name='signup'),
path('', views.signin, name='signin'),
] 


