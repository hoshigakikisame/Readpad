from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Novel(models.Model):
	judul = models.CharField(max_length=255, blank=True)
	thumbnail = models.ImageField(upload_to='documents/', default="/default-img.png")
	upload = models.DateTimeField(auto_now_add=True)
	pengarang = models.CharField(max_length=255, blank=True)
	penerbit = models.CharField(max_length=255, blank=True)
	harga = models.BigIntegerField()
	stok = models.PositiveIntegerField()
	deskripsi = models.TextField(default="Beautiful masterpiece")
	slug = models.SlugField(blank=True, editable=False)

	def save(self, *args, **kwargs):
		super(Novel, self).save(*args, **kwargs)
		self.slug = slugify(str(self.id) + self.judul)
		super().save()

	def __str__(self):
		return '{}'.format(self.judul)

class Pesanan(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	id_novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
	bukti_tf = models.ImageField(upload_to='documents/', blank=True)
	konfirmasi = models.BooleanField(default=False)
	aktif = models.BooleanField(default=True)
	total_bayar = models.PositiveIntegerField(blank=True)
	jumlah_pesan = models.PositiveIntegerField(blank=False)
	tgl_pesan = models.DateTimeField(auto_now_add=True)
	alamat_pembeli = models.TextField(blank=False, default="jl. mawar")

	def save(self, *args, **kwargs):
		super(Pesanan, self).save(*args, **kwargs)
		super().save()

	def __str__(self):
		return '{} | {}'.format(self.id_novel, self.user)