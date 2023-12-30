from django.urls import path
from . import views

app_name = 'contact_us'
urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact_us_page'),
    path('create-profile/', views.CreateProfileView.as_view(), name='create_profile_page'),
    path('profiles/', views.ProfilesView.as_view(), name='profiles_page'),
]
