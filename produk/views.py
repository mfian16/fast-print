from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProdukSerializer
from .utils import get_fastprint_data
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages



def import_api(request):
    get_fastprint_data()
    return redirect('produk:list_produk')

@api_view(['GET'])
def api_produk(request):
    produk = Produk.objects.all()
    serializer = ProdukSerializer(produk, many=True)
    return Response(serializer.data)

def list_produk(request):
    query = request.GET.get('q', '')

    produk_list = Produk.objects.all().order_by('nama_produk')

    if query:
        produk_list = produk_list.filter(
            Q(nama_produk__icontains=query) |
            Q(kategori__nama_kategori__icontains=query)
        )

    paginator = Paginator(produk_list, 10)
    page_number = request.GET.get('page')
    produk = paginator.get_page(page_number)

    return render(request, 'produk/list.html', {
        'produk': produk,
        'query': query
    })



def produk_bisa_dijual(request):
    query = request.GET.get('q', '')

    produk_list = Produk.objects.filter(
        status__nama_status="bisa dijual"
    ).order_by('nama_produk')

    if query:
        produk_list = produk_list.filter(
            Q(nama_produk__icontains=query) |
            Q(kategori__nama_kategori__icontains=query)
        )

    paginator = Paginator(produk_list, 10)  # 10 data per halaman
    page_number = request.GET.get('page')
    produk = paginator.get_page(page_number)

    return render(request, 'produk/list.html', {
        'produk': produk,
        'query': query
    })

def tambah_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil ditambahkan")
            return redirect('produk:list_produk')

    else:
        form = ProdukForm()

    return render(request, 'produk/form.html', {'form': form})


def edit_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    form = ProdukForm(request.POST or None, instance=produk)

    if form.is_valid():
        form.save()
        messages.success(request, "Produk berhasil diperbarui")
        return redirect('produk:list_produk')

    return render(request, 'produk/form.html', {'form': form})


def hapus_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    produk.delete()
    messages.success(request, "Produk berhasil dihapus")
    return redirect('produk:list_produk')

