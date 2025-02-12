# from crispy_forms.helper import FormHelper
from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory

from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['approved',]



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

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if author and author[0] != author[0].upper():
            raise ValidationError('Author name should start with uppercase letter.')

        return author

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and title.lower() in content.lower():
            raise ValidationError('Title cannot be included in the post.')

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)
        post.title.capitalize()

        if commit:
            post.save()

        return post


class PostEditForm(PostCreateForm):
    class Meta(PostCreateForm.Meta):
        error_messages = PostCreateForm.Meta.error_messages


class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)


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

    # Using crispy helper example
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper()
    #     self.helper.method = 'post'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')

        labels = {
            'author': '',
            'content': ''
        }

        error_messages = {
            'author': {
                'required': 'You can`t submit without author!'
            },

            'content': {
                'required': 'You can`t leave the content empty!'
            },

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add comment...'
        })

CommentFormSet = modelformset_factory(
    Comment,
    form=CommentForm,
    fields=('author', 'content'),  # Specify the fields you want to include in the formset
    extra=1
)
