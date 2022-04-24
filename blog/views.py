from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

from .forms import PostForm
from .models import BlogPost


# def post_list_view(request):
#     # posts_list = BlogPost.objects.all()
#     posts_list = BlogPost.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/post_list.html', {'posts_list': posts_list})

class PostListView(generic.ListView):
    # model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return BlogPost.objects.filter(status='pub').order_by('-datetime_modified')


# def post_detail_view(request, pk):
#     # try:
#     #     post = BlogPost.objects.get(pk=pk)
#     # except BlogPost.DoesNotExist:
#     #     post = None
#     #     print('Excepted')
#
#     # try:
#     #     post = BlogPost.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     post = None
#     #     print('Excepted')
#
#     post = get_object_or_404(BlogPost, pk=pk)
#
#     return render(request, 'blog/post_detail.html', {'post': post})

class PostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# def post_create_view(request):
#     # print(request.method)
#     # print('this is the create post view')
#
#     # print(request.POST)
#     # print(request.POST.get('title'))
#     # print(request.POST.get('text'))
#
#     # if request.method == 'POST':
#     #     print('post request')
#     # else:
#     #     print('get request')
#
#     # if request.method == 'POST':
#     #     post_title = request.POST.get('title')
#     #     post_text = request.POST.get('text')
#     #
#     #     user = User.objects.all()[0]
#     #     BlogPost.objects.create(title=post_title, text=post_text, author=user, status='pub')
#     # else:
#     #     print('get request')
#
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form = PostForm()
#             # return redirect(reverse('post_list'))
#             return redirect('post_list')
#     else:  # get request
#         form = PostForm()
#
#     return render(request, 'blog/post_create.html', {'form': form})

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'


# def post_update_view(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_detail', post.id)
#     return render(request, 'blog/post_create.html', {'form': form})

class PostUpdateView(generic.UpdateView):
    model = BlogPost
    # form_class = PostForm
    fields = ['title', 'text']
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


# def post_delete_view(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request, 'blog/post_delete.html', {'post': post})

class PostDeleteView(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

    # def get_success_url(self):
    #     return reverse('post_list')
