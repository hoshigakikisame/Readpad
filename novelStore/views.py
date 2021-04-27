from django.shortcuts import render, redirect
from novel.models import Novel, Pesanan
from django.contrib.auth.decorators import login_required

def index(request):
	if request.user.is_superuser:
		return redirect('staffPage')
	novel = Novel.objects.all().order_by('-upload')
	return render(request, 'index.html', {'semua_novel':novel})

def search(request):

	if 'query' in request.GET:
		query = request.GET['query']
		query = query.strip()
		novel_search = Novel.objects.filter(judul__icontains=query).order_by('-upload')
	
		context = {
			'q':query,
			'novel_search':novel_search,
		}

		return render(request, 'search.html', context)

	return redirect(index)

@login_required(login_url="/userAuth/login/")
def staffPage(request):
	if request.user.is_superuser:
		pesanan = Pesanan.objects.filter(aktif=True).order_by('-tgl_pesan')
		pesanan_selesai = Pesanan.objects.filter(aktif=False).order_by('-tgl_pesan')
		context = {
			'pesanan':pesanan,
			'pesanan_selesai':pesanan_selesai
		}
		return render(request, 'staffPage.html', context)
	return redirect('index')

@login_required(login_url="/userAuth/login/")
def konfirmasi(request, id_pesanan):
	pesanan = Pesanan.objects.get(id=id_pesanan)
	if pesanan.konfirmasi == False:
		pesanan.konfirmasi = True
		pesanan.save()
	else:
		pesanan.konfirmasi = False
		pesanan.save()
	return redirect('staffPage')