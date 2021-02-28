from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('api', views.ReportSerialize.as_view(), name='api'),
    # Category
    path('category', views.CategoryView.as_view(), name='category'),
    path('add_category', views.CategoryFormView.as_view(), name='add_category'),
    path('<int:pk>/category_update', views.CategoryUpdateView.as_view(), name='category_update'),
    # Products
    path('product', views.ProductView.as_view(), name='product'),
    path('add_product', views.ProductFormView.as_view(), name='add_product'),
    path('<int:pk>/product_update', views.ProductUpdateView.as_view(), name='product_update'),
]
