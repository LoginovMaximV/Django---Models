from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput, Select
from .models import Post
import django_filters


class PostFilter(FilterSet):
    category_type = django_filters.ChoiceFilter(
        field_name='category_type',
        choices=Post.CATEGORY_CHOICE,
        widget=Select(attrs={'class': 'form-control'}),
        label='Категория'
    )

    added_after = DateTimeFilter(
        field_name='date_create',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
        label='Опубликовано после указываемой даты'
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],

        }
