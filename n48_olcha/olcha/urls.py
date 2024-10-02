from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import category,group,product
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)


urlpatterns = [
    path('categories/', category.CategoryListApiView.as_view(), name='categories'),
    path('groups/', group.GroupListApiView.as_view(), name='groups'),
    path('category/<slug:slug>/',category.CategoryDetailApiView.as_view(), name='category'),
    path('all-products/', product.ProductListApiView.as_view(),name='all-products'),
    path('all-images/', product.ImageListApiView.as_view(),name='all-products'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
