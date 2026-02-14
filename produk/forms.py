from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'
        widgets = {
            'nama_produk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama produk'
            }),
            'harga': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'step': '1',
                'placeholder': 'Masukkan harga'
            }),
            'kategori': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        
    def clean_nama_produk(self):
        nama = self.cleaned_data.get('nama_produk')
        if not nama:
            raise forms.ValidationError("Nama produk wajib diisi.")
        return nama

    def clean_harga(self):
        harga = self.cleaned_data.get('harga')
        if harga is None or harga <= 0:
            raise forms.ValidationError("Harga harus lebih dari 0.")
        return harga