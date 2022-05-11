from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse


class HelloWorld(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        str_ = "Hello, World"
        return HttpResponse(str_)


class IndexView(View):
    def get(self, request):
        return render(request, "common/index.html")
