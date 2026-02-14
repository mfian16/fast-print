from rest_framework import serializers
from .models import Produk

class ProdukSerializer(serializers.ModelSerializer):
    kategori_nama = serializers.CharField(source='kategori.nama_kategori', read_only=True)
    status_nama = serializers.CharField(source='status.nama_status', read_only=True)

    class Meta:
        model = Produk
        fields = [
            'id_produk',
            'nama_produk',
            'harga',
            'kategori',
            'kategori_nama',
            'status',
            'status_nama'
        ]
