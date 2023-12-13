from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'categoryType', 'text', 'postCategory']
        labels = {'author': 'Автор',
                  'title': 'Заголовок',
                  'text': 'Текст',
                  'postCategory': 'Категория',
                  'categoryType': 'Тип'}

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")
        if title == text:
            raise ValidationError(
                "Заголовок не должен быть идентичным тексту."
            )

        return cleaned_data
