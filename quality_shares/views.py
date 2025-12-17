from http import HTTPStatus
from django.shortcuts import render


def handler404(request, exception):
    """Render a custom 404 error page."""
    return render(request, "errors/404.html", status=HTTPStatus.NOT_FOUND)


def handler500(request):
    """Render a custom 500 error page."""
    return render(
        request, "errors/500.html", status=HTTPStatus.INTERNAL_SERVER_ERROR
    )


def test_server_error(request):
    """
    Simulate an internal server error.

    To simulate an internal server error, add a path in the project urls.py
    file that sends the request to this function. E.g.

    `path("500/", views.test_error_server),`

    Delete the test path before pushing changes.
    """
    raise Exception("This is a simulated internal server error.")
