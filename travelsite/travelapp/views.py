from django.shortcuts import render
from django.http import HttpResponse
from .models import place
from .models import Newupdates
def demo(request):
    obj=place.objects.all()
    update_obj = Newupdates.objects.all()
    return render(request,"index.html",{'result':obj,'update_res':update_obj})