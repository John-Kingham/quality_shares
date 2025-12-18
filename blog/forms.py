from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)

    def __init__(self, *args, **kwargs):
        """Blank out the comment label and add a placeholder"""
        super().__init__(*args, **kwargs)
        content = self.fields["content"]
        content.label = ""
        content.widget.attrs["placeholder"] = "Enter your comment here..."
