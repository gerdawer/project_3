from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Film, Comment, Rating
from .forms import CommentForm, RatingForm
from django.contrib.auth import get_user_model
User = get_user_model()


def index(request):
    post_list = Film.objects.all()
    form = CommentForm()
    return render(
        request, 'index.html', {
            'post_list': post_list,
            'form': form,
        }
    )


def add_comment(request, username, film_id):
    """Добавление комментария к записи"""
    film = get_object_or_404(Film, id=film_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(author=request.user, film=film, **form.cleaned_data)
            return redirect('index')
    return redirect('index')


def film_view(request, username, film_id):
    user_profile = get_object_or_404(User, username=username)
    film = get_object_or_404(Film.objects.select_related('title'), author=user_profile, pk=film_id)
    counter_posts = Film.objects.filter(author=user_profile).count(id)
    form = CommentForm()
    items = Comment.objects.filter(film=film).count(author)
    return render(
        request, 'post.html', {
            'username': username,
            'user_profile': user_profile,
            'film': film,
            'counter': counter_posts,
            'form': form,
            'items': items}
    )




