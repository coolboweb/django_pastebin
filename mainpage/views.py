from django.shortcuts import render


def main_view(request):
    return render(request, 'mainpage/mainpage.html', {
        'info': 'Hello World',
    })
