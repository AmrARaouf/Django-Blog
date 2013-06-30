from django.contrib.auth.models import User
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
   'post_title':post.title, 'post_content':post.content, 'comments':comments}, context_instance=RequestContext(request) )

def comment(request, blog_name):
  usr = request.user
  contnt = request.POST['content']
  pst = Post.objects.get(id=request.POST['post_id'])
  c = Comment(user=usr, post=pst, content=contnt)
  c.save()
  return redirect('/' + blog_name + '/' + request.POST['post_id'] + '/')
  #url = reverse('view', kwargs={'post_id':request.POST['post_id'], 'blog_name': blog_name})
  #return HttpResponseRedirect(url)
