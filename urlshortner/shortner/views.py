from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':       # if they sending POST request
        link = request.POST['link']     # take the url store in url variable
        uid = str(uuid.uuid4())[:5]    # it shorten the url until 5 strings
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
# 'https://'+url_details.link