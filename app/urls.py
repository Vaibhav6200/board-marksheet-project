from django.urls import path
from .import views


app_name = 'app'

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('upload/', views.upload, name="upload"),
    path('bulk_upload/', views.bulk_upload, name="bulk_upload"),
    path('individual_upload/', views.individual_upload, name="individual_upload"),

    path('downloadAll/', views.downloadAll, name="downloadAll"),


    path('filter_school/<int:class_id>', views.filter_school, name="filter_school"),
    path('filter_student/<int:class_id>', views.filter_student, name="filter_student"),
]
