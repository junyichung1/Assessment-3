from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
#     path('', views.add_widget, name='add_widget'),
    path('addwidgets/', views.WidgetCreate.as_view(), name="add_widget"),
    path('deletewidgets/<int:pk>/', views.WidgetDelete.as_view(), name="delete_widget"),
]