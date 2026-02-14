from django.urls import path, include

urlpatterns = [
    path('', include(('produk.urls', 'produk'), namespace='produk')),
]
