



from django.urls import path
from . import views


urlpatterns = [
    
    path('clients/', views.ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', views.ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-detail'),
    path('projects/', views.ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', views.ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
]

