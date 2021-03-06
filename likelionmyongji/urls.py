"""likelionmyongji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import page.views
import question.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page.views.home, name='home'),
    path('question/', question.views.question_list, name='question_list'),
    path('question/<int:question_id>/', question.views.question_detail, name='question_detail'),
    path('question/post/', question.views.question_post, name='question_post'),
    path('question/delete/<int:question_id>/', question.views.question_delete, name='question_delete'),
    path('question/edit/<int:question_id>/', question.views.question_edit, name='question_edit'),
    path('question/comment/<int:question_id>/', question.views.comment, name='comment'),
    path('question/comment/<int:question_id>/delete/<int:comment_id>', question.views.comment_delete, name='comment_delete'),
]
