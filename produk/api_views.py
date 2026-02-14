from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produk
from .serializers import ProdukSerializer


# GET ALL
@api_view(['GET'])
def api_produk_list(request):
    produk = Produk.objects.all()
    serializer = ProdukSerializer(produk, many=True)
    return Response(serializer.data)


# GET BISA DIJUAL
@api_view(['GET'])
def api_produk_bisa_dijual(request):
    produk = Produk.objects.filter(status__nama_status="bisa dijual")
    serializer = ProdukSerializer(produk, many=True)
    return Response(serializer.data)


# GET DETAIL
@api_view(['GET'])
def api_produk_detail(request, pk):
    try:
        produk = Produk.objects.get(pk=pk)
    except Produk.DoesNotExist:
        return Response({"error": "Data tidak ditemukan"}, status=404)

    serializer = ProdukSerializer(produk)
    return Response(serializer.data)


# CREATE
@api_view(['POST'])
def api_produk_create(request):
    serializer = ProdukSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


# UPDATE
@api_view(['PUT'])
def api_produk_update(request, pk):
    try:
        produk = Produk.objects.get(pk=pk)
    except Produk.DoesNotExist:
        return Response({"error": "Data tidak ditemukan"}, status=404)

    serializer = ProdukSerializer(produk, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# DELETE
@api_view(['DELETE'])
def api_produk_delete(request, pk):
    try:
        produk = Produk.objects.get(pk=pk)
    except Produk.DoesNotExist:
        return Response({"error": "Data tidak ditemukan"}, status=404)

    produk.delete()
    return Response({"message": "Berhasil dihapus"}, status=204)
