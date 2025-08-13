from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_view),
    path('key_press/', views.key_press, name='key_press'),
    path('backspace/', views.backspace, name='backspace'),
    path('submit/', views.submit, name='submit'),
]
