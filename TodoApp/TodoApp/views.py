from django.http import HttpResponse


def home():
    return HttpResponse("Bienvenida al home")
