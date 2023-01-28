from django.shortcuts import render



def page_not_found_404(request, exception):
    return render(request, 'errorpages/404.html', status=404)



def gone_notexits_410(request, exception):
    return render(request, 'errorpages/410.html', status=410)


def internal_error_500(request, exception):
    return render(request, 'errorpages/500.html', status=500)



def service_unavailable_503(request, exception):
    return render(request, 'errorpages/503.html', status=503)

