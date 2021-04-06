from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'social_user'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post', views.CreatePost.as_view(), name='create_post'),
    path('update_post/<int:pk>', views.UpdatePost.as_view(), name='update_post'),
    path('post_list', views.PostList.as_view(), name='post_list'),
    path('post_details/<int:pk>', views.PostDetails.as_view(), name='post_detail'),
    path('post_delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
