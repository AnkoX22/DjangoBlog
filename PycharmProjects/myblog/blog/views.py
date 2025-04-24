from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Post, Status, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm
from django.views.generic import FormView
from django.core.mail import send_mail

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(status=Status.PUBLISHED).order_by('-publish')

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post, publish__year=year,
                             publish__month=month, publish__day=day)

    return render(request, 'blog/post/detail.html', {'post': post})


def post_share(request):
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            to = form.cleaned_data['to']
            name = form.cleaned_data['name']
            comments = form.cleaned_data['comments']

        message = f"""
        Received message from {name}, email: {email}
        {comments}
        """

        send_mail(subject="Post Share", message=message, from_email="noreply@me.com",
                  recipient_list=[to])
        return render(request, "blog/list.html")


def post_comment(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post, publish__year=year,
                             publish__month=month, publish__day=day)

    comments = post.comments.filter(active=True)

    comment = None

    if request.method == 'POST':
       form = CommentForm(data=request.POST)
       comment = Comment()
       if form.is_valid():
           comment = form.save(commit=False)
           comment.post = post
           comment.active = True
           comment.save()
           return render(request, 'blog/post/detail.html', {'post': post})

    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {
        'form':form,
        'post':post,
        'comment': comment,
        'comments': comments.all()
    })