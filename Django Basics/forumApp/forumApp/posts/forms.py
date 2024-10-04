from django import forms

from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        error_messages = {
            'title': {
                'required': 'Please enter a title.',
                'max-limit': f'Please follow the {Post.TITLE_MAX_LENGTH} char limit for the title; it`s too long.'
            },
            'author': {
                'required': 'Please add an author for the post.'
            }
        }

class PostEditForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        error_messages = PostCreateForm.Meta.error_messages

class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    disabled_fields = ('title',)


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        error_messages= {
            # 'required': 'Please write something to search.',
            'max_length': 'You can only enter 100 characters!'
        },
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...'
            }
        )
    )