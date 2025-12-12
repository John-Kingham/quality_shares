from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    """
    Renders the blog post archive page.

    Models:
        :model:`blog.Post`

    Template:
        :template:`blog/post_list.html`

    Context:
        posts (QuerySet): All published posts.
    """

    model = Post
    queryset = Post.objects.filter(published=True)
    context_object_name = "posts"
