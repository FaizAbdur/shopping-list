from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Faiz Abdurrachman',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
