from django.urls import path 
from . import views

urlpatterns = [
	path('pesanan/', views.pesanan, name="pesanan"),
	path('bayar/<int:id_pesanan>', views.bayar, name="bayar"),
	path('pesan/<int:id_novel>', views.pesan_novel, name="pesan"),
	path('batalkan_pesanan/<int:id_pesanan>', views.batalkan_pesanan, name="batalkan_pesanan"),
	path('pesanan_selesai/<int:id_pesanan>', views.pesanan_selesai, name="pesanan_selesai"),
]