from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fantasy.html', views.fantasy_view, name='fantasy'),
    path('home.html', views.home, name='home'),
    path('fiction.html', views.fiction_view, name='fiction'),
    path('action_adventure.html', views.action_adventure_view, name='action_adventure'),
    path('mistery.html', views.mistery_view, name='mistery'),
    path('horror.html', views.horror_view, name='horror'),
    path('thriller_suspense.html', views.thriller_suspense_view, name='thriller_suspense'),
    path('romance.html', views.romance_view, name='romance')
]