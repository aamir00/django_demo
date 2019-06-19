from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Comments
from .forms import CommentForm
# Create your views here.

#Onredirect from the urls these can be configured

def index(request):
    comments_var = Comments.objects.order_by('-date_added');
    context= {'comments' : comments_var };
    return render(request, 'guestbook/index.html', context)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comments(name=request.POST['name'], comment = request.POST['comment'])
            new_comment.save()
            return redirect('guestbook_index')
    else:
        form = CommentForm()
    context = {'form': form }
    return render(request, 'guestbook/sign.html', context)
