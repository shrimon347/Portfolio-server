from django.urls import path
from . import views

urlpatterns = [
    path("blogs/",views.getbloglist, name="blogs"),
    path("blogs/<str:pk>/",views.getblogpost, name="blog"),
    path('contact/', views.contact_view, name='contact'),
    path('projects/', views.getprojects, name='works'),
]
