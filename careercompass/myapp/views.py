from django.shortcuts import render, redirect

def Home(request):
    return render(request, 'Home.html')
def field(request):
    value = request.POST.get('choice')
    return render(request, 'field.html', {'value':value})

def college(request, string):
    return render(request, "college_list.html", {'value':string})
