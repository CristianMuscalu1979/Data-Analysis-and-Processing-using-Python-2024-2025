from django.urls import path
from .views import *

numele_aplicatiei = 'joc' 
fisierul = 'urls'

urlpatterns = [
    path('clasic', rock_paper_view),
    path('frumos', rock_paper_scissors_lizard_spock_view),
    
]