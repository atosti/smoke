from django.shortcuts import render
from django.http import HttpResponse
from yahoo_finance import Share

def index(request):
    favs = ['KMKGF', 'SLW', 'AAU'] #Hardcoded for now
    output = ""
    for i in range (len(favs)):
        #temp = Share('KMKGF')
        temp = Share(favs[i])
        #output = output.join(temp)
        output = output + "".join(temp.get_price()) + "\n"
        
    return HttpResponse(output)
