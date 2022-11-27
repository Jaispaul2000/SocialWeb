"""socialappweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from socialgram import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginView.as_view(),name='signin'),
    path('accounts/signup/',views.SignUpView.as_view(),name="signup"),
    path('home',views.HomeView.as_view(),name="home"),
    path('home/account/',views.UserDashboardView.as_view(),name='userdashboard'),
    path('home/<int:id>/add_like',views.add_like,name="add-like"),
    path('home/account/addpost/',views.PostAddView.as_view(),name='add-post'),
    path('home/account/logout/',views.signout,name='signout'),
    path('home/account/post/<int:id>/',views.PostDetailView.as_view(),name='post-detail'),
    path('home/account/post/<int:id>/add_comment',views.add_comment,name="addcomment"),
    path('home/<int:id>/add_comment',views.add_comment,name="add_comment"),
    path('home/account/post/<int:id>/remove_comment',views.remove_comment,name="removecomment"),
    path('home/<int:id>/save_post',views.save_post,name="savepost"),
    path('home/account/saved',views.SavedPosts.as_view(),name="saved-posts"),
    path('home/account/saved/<int:id>',views.SavedPostDetailView.as_view(),name="saved-post-details"),
    path('home/<int:id>',views.UserAccountView.as_view(),name="user-account"),
    path('home/account/post/<int:id>/delete_post',views.post_delete_view,name="remove-post"),
    path("account/editprofile/<int:id>",views.EditProfileView.as_view(),name="editprofile")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
