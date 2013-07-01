from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from blogs.models import Blog, Post, Comment
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext

def index(request, blog_name):
  blog = get_object_or_404(Blog, name=blog_name)
  posts = blog.post_set.all()
  return render_to_response('blogs/index.html', {'blog_name':blog_name, 'blog_description':blog.description, 'posts':posts})

def view(request, blog_name, post_id):
  post = get_object_or_404(Post, pk=post_id)
  comments = post.comment_set.all()
  isauth = request.user.is_authenticated()
  return render_to_response('blogs/post.html', {'post_id':post_id, 'isauth':isauth, 'blog_name':blog_name,
   'post_title':post.title, 'post_content':post.content, 'comments':comments}, context_instance=RequestContext(request))

def comment(request, blog_name):
  usr = request.user
  contnt = request.POST['content']
  pst = Post.objects.get(id=request.POST['post_id'])
  c = Comment(user=usr, post=pst, content=contnt)
  c.save()
  return redirect('/' + blog_name + '/' + request.POST['post_id'] + '/')

def home(request):
  if request.user.is_authenticated():
    blog = Blog.objects.get(user=request.user)
    if blog is not None:
      return redirect('/' + blog.name + '/')
    else:
      return render_to_response('blogs/noblog.html')
  else:
    return render_to_response('blogs/homepage.html', context_instance=RequestContext(request))

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('/index')
    else:
      messages.error(request, 'Username and/or password invalid')
      return redirect('/index')

def logout_view(request):
    auth.logout(request)
    return redirect('/index')
