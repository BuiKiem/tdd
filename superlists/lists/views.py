from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home_page(request: HttpRequest) -> HttpResponse:
    """Home page view function"""

    return HttpResponse("<html><title>To-Do lists</title></html>")
