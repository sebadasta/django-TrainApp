from django.http import HttpResponse
from django.shortcuts import render



def index(request):
   return render(request, "index.html")

def test(request):

   testlist = ['asd','1q','dede']
   return render(request, "test.html", {"testlist": testlist})
