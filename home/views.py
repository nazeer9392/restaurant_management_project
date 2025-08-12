from django.shortcuts import render
from django.conf import settings
# Create your views here.
 def about(request):
    return render(request,'about.html')
def homepage_view(request):
    context={
        'phone_number':settings.RESTAU
    }