from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

from blog.models import BlogPost
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from website.forms import SignupForm, BlogPostForm



# Create your views here.

# @login_required
# def blog_posts(request):
#     blog_post = get_object_or_404(BlogPost, pk=3)
#
#     return HttpResponse(blog_post.content)

def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, "blog/index.html", context={"posts": posts})

def blog_post(request, slug):

    post = BlogPost.objects.get(slug=slug)

    return render(request, "blog/post.html", context={"post": post})


def blogpost(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.published = True
            blogpost.save()
        return HttpResponseRedirect(request.path)
    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values["author"] = request.user
        init_values["date"] = datetime.today()
        form = BlogPostForm(initial=init_values)

    return render(request, "blog/create_article.html", {"form": form})