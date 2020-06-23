from django.shortcuts import render
from testapp.models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def home(request):
    return render (request,'testapp/home.html')

def hybjobs1(request):
    jobs_list=hybjobs.objects.order_by('date')
    paginator=Paginator(jobs_list,10)
    page_number=request.GET.get('page')
    try:
        jobs_list=paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list=paginator.page(1)
    except EmptyPage:
        jobs_list=paginator.page(paginator.num_pages)

    # mydict={'jobs_list':jobs_list}
    return render (request,'testapp/hybjobs.html',{'jobs_list':jobs_list})

def blorejobs1(request):
    jobs_list=blorejobs.objects.order_by('date')
    mydict={'jobs_list':jobs_list}
    return render (request,'testapp/blorejobs.html',context=mydict)

def chennaijobs1(request):
    jobs_list=chennaijobs.objects.order_by('date')
    mydict={'jobs_list':jobs_list}
    return render (request,'testapp/chennaijobs.html',context=mydict)

def punejobs1(request):
    jobs_list=punejobs.objects.order_by('date')
    mydict={'jobs_list':jobs_list}
    return render (request,'testapp/punejobs.html',context=mydict)
