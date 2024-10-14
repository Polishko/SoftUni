from datetime import datetime
from idlelib.debugobj import dispatch
from lib2to3.fixes.fix_input import context

from django.forms import modelform_factory
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.templatetags.i18n import language
from django.urls import reverse_lazy
from django.utils.decorators import classonlymethod
from django.views.generic import View, TemplateView, RedirectView, ListView, FormView, CreateView, UpdateView, \
    DeleteView

from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet, PostBaseForm
from forumApp.posts.models import Post, Comment

# The most basic CBV to render a get form:
# Index(View). Then less basic Index(BaseView)

# class BaseView:
#     @classonlymethod
#     def as_view(cls):
#
#         def view(request, *args, **kwargs):
#             view_instance = cls()
#             return view_instance.dispatch(request, *args, **kwargs)
#
#         return view
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponseNotAllowed(['POST'])
#
#     def post(self, request, *args, **kwargs):
#         return HttpResponseNotAllowed(['GET'])
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.method == 'GET':
#             return self.get(request, *args, **kwargs)
#         elif request.method == 'POST':
#             return self.post(request, *args, **kwargs)
#
#
# class Index(BaseView):
#     def get(self, request, *args, **kwargs):
#         post_form = modelform_factory(
#             Post,
#             fields=('title', 'content', 'author', 'language',),
#
#         )
#
#         context = {
#             'my_form': post_form,
#         }
#
#         return render(request, 'posts/common/index.html', context)

class IndexView(TemplateView):
    # template_name = 'posts/common/index.html'
    extra_context = {
        'static_time': datetime.now()
    } # this context is static and shows context at time of view initialization

    def get_context_data(self, **kwargs): # dynamic context passed on each request
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        return context


    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['posts/common/index-logged-in.html']
        else:
            return ['posts/common/index.html']


class Index(View):
    def get(self, request, *args, **kwargs):
        context = {
            'dynamic_time': datetime.now(),
        }

        return render(request, 'posts/common/index.html', context)


class RedirectHomeView(RedirectView):
    url = reverse_lazy('index') # static way

    def get_redirect_url(self, *args, **kwargs): # used for dynamic redirection logic
        pass

# Longer version that doesn't make use of FormView (mostly used for POST) and also has validation
class DashboardView(ListView):
    model = Post
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    # pass form to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] =  SearchForm(self.request.GET)
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('dashboard')


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('dashboard')
    template_name = 'posts/delete-post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostDeleteForm(instance=self.object)

        return context


class EditPostView(UpdateView):
    model = Post
    # form_class = PostEditForm
    success_url = reverse_lazy('dashboard')
    template_name = 'posts/edit-post.html'
    context_object_name = 'post'

    def get_form_class(self):
        if self.request.user.is_authenticated:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'language'))
        else:
            return modelform_factory(Post, fields=('content',))


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)

    # Pass the queryset to allow for editing of associated comments
    comment_formset = CommentFormSet(request.POST or None, queryset=Comment.objects.filter(post=post))

    if request.method == 'POST':
        if comment_formset.is_valid():
            for comment_form in comment_formset:
                if comment_form.cleaned_data.get('author') and comment_form.cleaned_data.get('content'):
                    comment = comment_form.save(commit=False)
                    comment.post = post
                    comment.save()
        else:
            print(comment_formset.errors)


        return redirect('details-post', pk=post.id)

    context = {
        'post': post,
        'comment_formset': comment_formset
    }

    return render(request, 'posts/details-post.html', context)
