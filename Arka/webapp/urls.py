
  
from django.urls import path
from .views import * 
urlpatterns = [
   path('',IndexView.as_view(),name='home'),
   path('blogs',BlogsList.as_view(), name='blogs'),
   path('members',MembersList.as_view(), name='team'),
   path('blog/<int:pk>',BlogDetail.as_view(), name='blog'),
  
   path('gallery/',GalleryList.as_view(), name = 'gallery'),
   path('admin-dashboard/',dashboard)
 
]