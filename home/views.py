from django.http import HttpResponse 

 

def index(request): 

    return HttpResponse("<h1>Welcome to My Django Website!</h1><p>This is a simple page.</p>") 