from django.urls import path
#from rest_framework.routers import DefaultRouter
from . import views
from .views import ActiveLinkView, RecentLinkView
from rest_framework.views import APIView
#from .views import LinkListApi, LinkCreateApi, LinkUpdateApi, LinkDeleteApi

app_name="links"

#router = DefaultRouter()
#router.register(r'links', LinkCreateApi, basename= 'link'  )

#urlpatterns = [] + router.urls

urlpatterns = [
    path("create/", views.LinkCreateApi.as_view(), name="api_create"),
    path("update/<int:pk>", views.LinkUpdateApi.as_view(), name="api_update"),
    path("delete/<int:pk>", views.LinkDeleteApi.as_view(), name="api_delete"),
    path("", views.LinkListApi.as_view(), name="api_list"),
    path("active/", ActiveLinkView.as_view(), name= 'active_link'),
    path("recent/", RecentLinkView.as_view(), name= 'recent_link'),
]

#http://127.0.0.1:8000/links
