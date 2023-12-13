from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from .models import Post, Category


class PostFilter(FilterSet):
    date = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата позже, чем',
        widget=DateTimeInput(
            attrs={'type': 'date'},
            format='%Y-%m-%dT',
        ),
    )

    class Meta:
        model = Post
        fields = {'title': ['icontains'], 'postCategory': ['exact']}
