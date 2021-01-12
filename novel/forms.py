from django import forms
from .models import Pesanan

class FormPesan(forms.ModelForm):
	class Meta:
		model = Pesanan
		fields = ['jumlah_pesan', 'alamat_pembeli']

class FormBuktiBayar(forms.ModelForm):
	class Meta:
		model = Pesanan
		fields = ['bukti_tf']