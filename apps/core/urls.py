from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # This calls the index function which now has the student data
    path("", views.index, name="dashboard"),
    path('profile/', views.profile_view, name='profile'),
]