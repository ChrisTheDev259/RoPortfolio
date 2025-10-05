from django.urls import path
from . import api 

urlpatterns = [
    path('market/product-grid', api.product_grid, name='product-grid'),
    path('market/create-portfolio', api.create_portfolio, name='create-portfolio'),
]