from django.urls import path
from user.views import SignupView, SiginView

app_name = 'user'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SiginView.as_view(), name='signin'),
]