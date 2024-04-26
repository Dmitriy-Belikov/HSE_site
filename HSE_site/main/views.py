from django.shortcuts import render

def index(request):

    return render(request, 'main/index.html')

'''def surveillance_map(request):
    return render(request, 'forms/forms.html')'''


def about(request):
    return render(request, 'main/about.html')



