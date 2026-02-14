from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    # ========================
    # TEMPLATE VIEWS
    # ========================
    path('', views.list_produk, name='list_produk'),
    path('bisa-dijual/', views.produk_bisa_dijual, name='produk_bisa_dijual'),
    path('tambah/', views.tambah_produk, name='tambah_produk'),
    path('edit/<int:pk>/', views.edit_produk, name='edit_produk'),
    path('hapus/<int:pk>/', views.hapus_produk, name='hapus_produk'),
    path('import/', views.import_api, name='import_api'),

    # ========================
    # API ENDPOINTS (DRF)
    # ========================
    path('api/produk/', api_views.api_produk_list),
    path('api/produk/bisa-dijual/', api_views.api_produk_bisa_dijual),
    path('api/produk/<int:pk>/', api_views.api_produk_detail),
    path('api/produk/create/', api_views.api_produk_create),
    path('api/produk/update/<int:pk>/', api_views.api_produk_update),
    path('api/produk/delete/<int:pk>/', api_views.api_produk_delete),
]
