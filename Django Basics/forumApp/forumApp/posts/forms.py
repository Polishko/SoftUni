from django import forms

from forumApp.posts.choices import LanguageChoices
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # or
        # fields = ['language']

        # widgets = {
        #     'title': forms.NumberInput,
        # }
        #
        # help_texts = {
        #     'title': 'Please add title.',
        # }
        #
        # labels = {
        #     'title': 'This is the post title.'
        # }


# class Post(forms.Form):
#     TITLE_MAX_LENGTH = 100
#     AUTHOR_MAX_LENGTH = 30
#     LANGUAGE_MAX_LENGTH = 20
#
#     title = forms.CharField(
#         max_length=TITLE_MAX_LENGTH,
#     )
#
#     content = forms.CharField(
#         widget=forms.Textarea,
#     )
#
#     author = forms.CharField(
#         max_length=AUTHOR_MAX_LENGTH,
#     )
#
#     created_at = forms.DateTimeField(
#         auto_now_add=True,
#     )
#
#     language = forms.CharField(
#         max_length=LANGUAGE_MAX_LENGTH,
#         choices=LanguageChoices.choices,
#         initial=LanguageChoices.OTHER,
#     )
