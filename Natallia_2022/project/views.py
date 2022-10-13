from django.http import HttpResponse
from django.shortcuts import render
from .models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get (pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)





def hello_world_2(request):
    return render(request, 'hello_world_2.html')

# def reverse(request):
#     user_text = request.GET["usertext"]
#     reversed_text=user_text[::-1]
#     num_words=len(reversed_text.split())
#     return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'numwords':num_words})
