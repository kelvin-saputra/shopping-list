from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Kelvin Saputra',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)