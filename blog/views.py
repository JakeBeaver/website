from django.shortcuts import render_to_response
from django.http import HttpResponse
from blog.models import posts

# Create your views here.

def home(request):
	return render_to_response('blog.html', {'posts':posts.objects.all()})
