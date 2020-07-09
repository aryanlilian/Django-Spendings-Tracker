from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home/index.html')


@login_required
def blog(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Blog',
    }
    return render(request, 'home/blog.html', context)


@login_required
def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        Comment.objects.create(
            user=request.user, post=post, comment_text=request.POST['comment_text'])
        return redirect('post', pk)

    context = {
        'post': post,
        'comments': comments,
        'title': 'Post',
    }
    return render(request, 'home/post.html', context)


def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    post_id = comment.post.id
    if request.method == 'POST':
        comment.delete()
        return redirect('post', post_id)
    context = {
        'comment': comment,
    }
    return render(request, 'home/delete.html', context)


def update_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    post_id = comment.post.id
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post', post_id)
    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, 'home/update_comment.html', context)
