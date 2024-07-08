from django.shortcuts import render
from .models import soilMoistureReading

# Create your views here.
def moisuture_list(request):
    readings=soilMoistureReading.objects.all().order_by('-timestamp')
    return render(request,'myprojectapp/moisture_list.html',{'readings'})