from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.generic import ListView
# Create your views here.
class TalkViewBase(ListView):
    template_name = "talk/chatpage.html"
    model = models.TalkModel
    # queryset = models.TalkModel.objects.filter(some_column='')
    paginate_by = 20

    # def get_queryset(self):
    #     return models.TalkModel.objects.filter(publish=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["item"] = models.TalkModel.objects.order_by('-created')[:0]
        # context['talks'] = models.TalkModel.objects.created_at.order_by('-created')
        print(context)
        return context