from models import Attachment, Post

from django.forms import ModelForm


class AttachmentForm(ModelForm):
    class Meta:
        model = Attachment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("contents", )

