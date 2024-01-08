from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>', ProductsCategoryListView.as_view(), name='category_product'),
    path('products', ProductListView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/updatemoderator/', ProductModeratorUpdateView.as_view(), name='product_update_moderator'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('blogs', BlogListView.as_view(), name='list'),
    path('blogs/view/<int:pk>', BlogDetailView.as_view(), name='view'),
    path('blogs/create', BlogCreateView.as_view(), name='create'),
    path('blogs/update/<int:pk>', BlogUpdateView.as_view(), name='update'),
    path('blogs/delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('contact', ContactsView.as_view(), name='contacts'),
]
