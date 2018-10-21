from django.contrib import admin
from django.urls import path
from news import views
urlpatterns = [
    
    path(r'hometemplate/', views.HomeView.as_view(),name='hometemplate'),
    path(r'migratedata/',views.MigrateData.as_view(),name='migrate_data'),
    path(r'news_apiview/',views.ListNewsView.as_view(),name = 'api_view'),
]