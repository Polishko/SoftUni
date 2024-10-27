from django import forms
from django.core.exceptions import ValidationError

from furryfunnies.posts.models import Post
from furryfunnies.mixins import PlaceHolderMixin, ReadOnlyMixin


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated_at', 'author']

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if Post.objects.filter(title=title).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Oops! That title is already taken. How about something fresh and fun?')

        return title


class PostCreateForm(PlaceHolderMixin, PostBaseForm):
    pass


class PostDetailForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].help_text = ''


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    readonly_fields = ['title', 'image_url', 'content', ]

    class Meta(PostBaseForm.Meta):
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].help_text = ''
