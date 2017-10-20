from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime
def index(request):
  print "Time", datetime.now().strftime("%Y-%m-%d %H:%M %p")
  context = {
  "time": strftime("%Y-%m-%d %I:%M %p", gmtime())
  }
  return render(request,'time_app/index.html', context)