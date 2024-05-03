from django.urls import path
from .views import IndexView, ModeloView, SobreView

urlpatterns = [
    # path('endereco/', IndexView.as_view(), name='nome-da-url'),
    path('', IndexView.as_view(), name='inicio'),
    path('modelo/', ModeloView.as_view(), name='modelo'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]
