"""hellodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from polls.views import show_subjects, show_all_teachers, praise_or_criticize, login, get_captcha, export_teachers_excel, export_pdf, get_teachers_data, api_show_subjects, show_all_subjects, show_teachers, SubjectView, TeacherView

from hellodjango import settings

urlpatterns = [path("admin/", admin.site.urls), path("", show_all_subjects), path("teachers/", show_all_teachers), path("praise/", praise_or_criticize), path("criticize/", praise_or_criticize), path("login/", login), path("captcha/", get_captcha), path("excel/", export_teachers_excel), path('pdf/', export_pdf), path('teachers_data/', get_teachers_data), path('api/bpm/subjects/', api_show_subjects), path('api/subjects/', show_subjects), path('api/teachers/', TeacherView.as_view())]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns.insert(0, path('__debug__/', include(debug_toolbar.urls)))


# CBV 实现的RESTful api 通过继承 ModelViewSet 类实现多个函数方法，需要创建新的路由并注册添加到 urlspattern
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/cbv/subjects', SubjectView)
urlpatterns += router.urls