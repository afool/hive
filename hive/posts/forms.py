from django.forms import ModelForm
from models import Post
from models import Attachment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("contents", )

class AttachmentForm(ModelForm):
    class Meta:
        model = Attachment
