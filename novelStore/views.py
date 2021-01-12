from django.shortcuts import render
from novel.models import Novel

def index(request):
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