from django.shortcuts import render

# Create your views here.
def csa(request):
    return render(request,'csa.html')
def form(request):
    return render(request,'form.html')