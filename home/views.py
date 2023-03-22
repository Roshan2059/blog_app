from django.shortcuts import render,redirect,get_object_or_404
from home.models import Content

# Create your views here.
def home(request):
    content = Content.objects.all()
    return render(request, 'home.html', {'content': content})

def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    else:
        title = request.POST['topic']
        desc = request.POST['description']

        Content.objects.create(topic=title, description=desc, user_id = 1 )
        return redirect('home')

def delete_all(request):
    content = Content.objects.all()
    content.delete()

    return redirect('home')

def delete_individual(request, id):
    try:
        blog = Content.objects.get(id=id)
        blog.delete()
    except Content.DoesNotExist:
        return render(request, '404.html')
    return redirect('home')

def edit(request, id):
    # blog = Content.objects.get(id=id)
    blog = get_object_or_404(Content, id=id)
    
    if request.method == 'GET':
        return render(request, 'edit.html', {'blog' : blog})
    else:
        new_topic = request.POST['topic']
        new_description = request.POST['description']

        blog.topic = new_topic
        blog.description = new_description
        blog.save()

        return redirect('home')
