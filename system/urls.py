from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"), 
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('profile', views.profile, name="profile"),
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('crime', views.crime, name="crime"),
    path('complain', views.complain, name="complain"),
    path('records', views.records, name="records"),
    path('about', views.about, name="about"),
    path('details/crime/<int:id>', views.crimedetails, name="crimedetails"),
    path('details/complain/<int:id>', views.compdetails, name="compdetails"),
    path('what-report', views.what_report, name="what-report"),
    path('contact', views.contact, name="contact"),
]
