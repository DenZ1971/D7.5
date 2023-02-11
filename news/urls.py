from .views import *
from django.urls import path

urlpatterns = [

   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('create/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('create/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('upgrade/', upgrade_user, name='upgrade_user'),
   path('category/<int:pk>/', CategoryList.as_view(), name='category_list'),
   path('category/<int:pk>/subscribe/', subscribe, name='subscribe'),
   path('category/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),


]
