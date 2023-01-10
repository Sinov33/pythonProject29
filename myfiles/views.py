import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def home(malumot):
    if 'baza' in malumot.POST:
        matnim = malumot.POST.get('baza')
        sozim = str(matnim).strip()
        qidirishim = Q(nomi__icontains=sozim) | \
                     Q(malumot__icontains=sozim) | \
                     Q(vaqt__icontains=sozim)
        servic = Servise.objects.filter(qidirishim)
        odamlar = Team.objects.filter()
        ishlarimiz = Portfolio.objects.filter()
        return render(malumot, 'Index.html', {'service': servic,'team': odamlar,'works': ishlarimiz})

    elif 'guruh' in malumot.POST:
        matni = malumot.POST.get('guruh')
        sozi = str(matni).strip()
        qidirishi = Q(ism__icontains=sozi) | \
                   Q(lavozim__icontains=sozi) | \
                   Q(malumot__icontains=sozi) | \
                   Q(vaqt__icontains=sozi)
        servic = Servise.objects.filter(qidirishi)
        odamlar = Team.objects.filter()
        ishlarimiz = Portfolio.objects.filter()
        return render(malumot, 'Index.html', {'service': servic, 'team': odamlar, 'works': ishlarimiz})
    elif 'malumot' in malumot.POST:
        matn = malumot.POST.get('malumot')
        soz = str(matn).strip()
        qidirish = Q(nomi__icontains = soz)| \
                   Q(cleant_nomi__icontains=soz)|\
                   Q(date__icontains = soz)|\
                   Q(link__icontains = soz)|\
                   Q(malumot__icontains = soz)|\
                   Q(tur__id__icontains= soz)
        servic = Servise.objects.filter(qidirish)
        odamlar = Team.objects.filter()
        ishlarimiz = Portfolio.objects.filter()
        return render(malumot, 'Index.html', {'service': servic, 'team': odamlar, 'works': ishlarimiz})
    elif 'emailii' in malumot.POST:
        gmaili = malumot.POST.get('emailii')
        Gmail(gmailii=gmaili).save()
    elif malumot.method == 'POST':
        ismi = malumot.POST.get('name')
        gmaili = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        matn = malumot.POST.get('message')
        vaqti = datetime.datetime.now()
        Murojaat(name=ismi,gmail=gmaili,title=subject,textt=matn,date=vaqti).save()
    else:
        ishlarimiz = Portfolio.objects.filter()
        servic = Servise.objects.filter()
        odamlar = Team.objects.filter()
        return render(malumot,'Index.html',{'works':ishlarimiz,'service':servic,'team':odamlar})
    if malumot.method == 'GET':
        ishlarimiz = Portfolio.objects.all()
        return render(malumot, 'Index.html', {'works': ishlarimiz})

def inner(malumot):
    return render(malumot,'inner_page.html')

def portfolio(malumot,id):
    if malumot.method == 'POST':
        gmailim = malumot.POST.get('emailim')
        Portgmail(gmaili=gmailim).save()

    ishlarimiz = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{'work':ishlarimiz})

