from django.http import HttpResponse


def portfolio_view(request):
    return HttpResponse("The portfolio view is working.")
