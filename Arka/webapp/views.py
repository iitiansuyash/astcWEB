from django.shortcuts import render

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView
from .models import *

# Create your views here.
class IndexView(ListView):
    model = PostModel
    context_object_name = 'images'
    queryset = PostModel.objects.all().order_by('-id')[:6]

    template_name = 'index.html'

class BlogsList(ListView):
    model = PostModel
    context_object_name = 'blogs'
    paginate_by = 6
    queryset = PostModel.objects.order_by('-id')
    template_name = 'blogs.html'

class BlogDetail(DetailView):
    model = PostModel
    context_object_name = 'blog'
    template_name = 'blog-detail.html'


class GalleryList(ListView):
    context_object_name = 'images'
    paginate_by = 12
    template_name = 'gallery.html'

    def get_queryset(self):
        return PostModel.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(GalleryList, self).get_context_data(**kwargs)
        context['videos'] = VideoModel.objects.order_by('-id')
        return context

class MembersList(ListView):
    model = TeamMember
    context_object_name = 'members'
    queryset = TeamMember.objects.order_by('admission_number')
    template_name = 'team.html'
    



def dashboard(request):
    return render(request,'dashboard.html')

def team(request):
    return render(request,'team.html')




def blogDetail(request):
    return render(request, 'blog-detail.html')


