from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import News


class NewsList(ListView):
    template_name = 'news/news_list.html'
    paginate_by = 12

    def get_queryset(self):
        return News.objects.all()


def news_detail(request, *args, **kwargs):
    news_id = kwargs['news_id']
    detail = News.objects.filter(pk=news_id).first()
    tag = detail.tag.all()
    print(tag)
    context = {
        'news_detail': detail,
        'tag': tag,
    }
    return render(request, 'news/news-detail.html', context)
