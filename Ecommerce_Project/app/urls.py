from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home, name='home'),
    path('category/<str:val>/', views.CategoryView.as_view(), name='category'),
    path('productdetails/<int:pk>/', views.ProductDetails.as_view(), name='product-details')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
