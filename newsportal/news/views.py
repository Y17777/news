from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .forms import PostForm
from .models import Post
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class Search(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news_search.html'
    context_object_name = 'news'

    # paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news_det.html'
    context_object_name = 'news_det'


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return HttpResponseRedirect('/news')
    form = PostForm
    return render(request, 'create_page.html', {'form': form})


def news_util(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    template = 'news_utils.html'
    cnt = {
        'post_list': Post.objects.all().order_by('dateCreation'),
        'form': PostForm()
    }

    # form = PostForm
    return render(request, template, cnt)


def edit_page(request, pk):
    get_post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=get_post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/news')
    template = 'edit_page.html'

    cnt = {
        'get_post': get_post,
        'form': PostForm(instance=get_post)
    }
    return render(request, template, cnt)


def delete_page(request, pk):
    get_post = Post.objects.get(pk=pk)
    get_post.delete()
    return HttpResponseRedirect('/news/utils')
