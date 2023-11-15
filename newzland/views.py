from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wilimson(request):
    return HttpResponse('<marquee><h1>Newzland lost the match with 70 runs so they went home without winning WORLDCUP</h1></marquee>')
def phlips(request):
    return render(request,'philips.html')