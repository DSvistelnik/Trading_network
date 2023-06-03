from django.contrib import admin
from django.urls import path, include
from network_links import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('product/', views.ProductView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view()),
    path('factory/', views.NetworkView.as_view()),
    path('factory/<int:pk>/', views.NetworkDetailView.as_view()),
    #path('retail/', views.RetailView.as_view()),
    #path('retail/<int:pk>/', views.RetailDetailView.as_view()),
    #path('individual/', views.IndividualView.as_view()),
    #path('individual/<int:pk>/', views.IndividualDetailView.as_view()),
    path('user/', include('authentication.urls')),

]
