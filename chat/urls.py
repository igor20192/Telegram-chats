from django.urls import path
from .views import bot_pars


urlpatterns = [path("chat/", bot_pars, name="chat")]
