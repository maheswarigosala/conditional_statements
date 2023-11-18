from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':80,'b':50,'c':30}
    return render(request,'conditional.html',d)
