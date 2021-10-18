from django.shortcuts import render

def halaman1(request):
    namamk = ["Perikanan", 'Kelautan', 'Sistem Informasi']
    tentang = "dst"
    judulhalaman = "SeeSEA !"

    konteks = {
        'judul' : judulhalaman,
        'isi' : tentang,
        'namamk' : namamk
    }

    return render(request, 'halaman1.html',konteks)

def halaman2(request):
    return render(request, 'halaman2.html')

# Create your views here.
