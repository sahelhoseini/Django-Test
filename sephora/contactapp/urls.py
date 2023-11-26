from django.urls import path
from . import views


urlpatterns=[
    path('login/',views.login_view, name='login'),
    path('sign-in/',views.sign_in_view, name='sign_in'),
]