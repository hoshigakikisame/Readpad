from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/userAuth/login/")
def pesanan(request):
	pesanan_user = models.Pesanan.objects.filter(user=request.user, aktif=True).order_by('-tgl_pesan')
	return render(request, "pesanan.html", {'semua_pesanan':pesanan_user})

@login_required(login_url="/userAuth/login/")
def bayar(request, id_pesanan):
	update_pesanan = models.Pesanan.objects.get(id=id_pesanan)
	form = forms.FormBuktiBayar(request.POST or None, request.FILES or None, instance=update_pesanan)
	context = {
		'form':form,
	}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		return redirect('novel:pesanan')

	print()
	return render(request, 'bayar.html', context)

@login_required(login_url="/userAuth/login/")
def pesan_novel(request, id_novel):
	form = forms.FormPesan(request.POST or None, request.FILES or None)
	context = {
		'form':form,
	}
	if request.method == 'POST':
		if form.is_valid():
			pesanan_baru = form.save(commit=False)
			pesanan_baru.user = request.user
			if int(request.POST['jumlah_pesan']) == 1:
				pesanan_baru.total_bayar = int(models.Novel.objects.get(id=id_novel).harga)
			else:
				pesanan_baru.total_bayar = int(models.Novel.objects.get(id=id_novel).harga) * int(request.POST['jumlah_pesan'])
			pesanan_baru.id_novel = models.Novel.objects.get(id=id_novel)
			pesanan_baru.save()
			return redirect('novel:pesanan')

		else:
			print("not valid")
			print(form.errors)

	return render(request, 'buat_pesanan.html', context)

@login_required(login_url="/userAuth/login/")
def pesanan_selesai(request, id_pesanan):
	pesanan = models.Pesanan.objects.get(id=id_pesanan)
	pesanan.aktif = False
	pesanan.save()
	return redirect('novel:pesanan')

@login_required(login_url="/userAuth/login/")
def batalkan_pesanan(request, id_pesanan):
	models.Pesanan.objects.filter(id=id_pesanan).delete()
	return redirect('novel:pesanan')