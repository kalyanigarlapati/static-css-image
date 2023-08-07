from django.shortcuts import render

# Create your views here.
def hlo(request):
    return render(request,'hlo.html')