from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-published_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
