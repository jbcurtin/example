from django.urls import path

from webservice import views as webservice_views

urlpatterns = [
    path('signup-username-check.json', webservice_views.signup_username_check, name='check_username'),
    path('signup.json', webservice_views.signup, name='signup'),
    path('signup-password.json', webservice_views.signup_password, name='signup_password'),
    path('onboard.json', webservice_views.onboard, name='onboard'),
    path('login.json', webservice_views.login, name='login'),
]
