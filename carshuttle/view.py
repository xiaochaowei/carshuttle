from django.shortcuts import render_to_response
def index(request):
	return render_to_response("index.html")

def price(request):
	return render_to_response("price.html")

def about(request):
	return render_to_response("about.html")