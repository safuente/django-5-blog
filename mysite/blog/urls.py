from django.urls import path
from . import views

app = 'blog'

urlpatterns = [
    # post views
    path("", views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail')
]