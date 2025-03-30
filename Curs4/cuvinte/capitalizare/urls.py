###  URL MIC
from django.urls import path
from .views import capitalizare_view,parametrii_view


urlpatterns = [
    path('parametrii',parametrii_view),
    path('<text>',capitalizare_view),
    
]