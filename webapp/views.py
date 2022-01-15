from django.shortcuts import render

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView
from .models import *

from .pod import pod
# Create your views here.

def gallery(request):
    context["data"]=PostModel.objects.all().order_by
    return render(request,'_gallery.html',context)



class IndexView(ListView):
    model = PostModel
    context_object_name = 'images'
    queryset = PostModel.objects.all().order_by('-id')[:6]
    pod = pod()
    img_url = pod["hdurl"]
    img_title = pod["title"]
    img_caption = pod["explanation"]
    pic_of_day = {
        "img":img_url,
        "title":img_title,
        "body":img_caption,
    }
    def get_queryset(self):
        return PostModel.objects.order_by('-id')[:6]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['allnotice'] = Announcements.objects.order_by('-id')[:5]
        context["pod"]=self.pic_of_day
        return context
    

    template_name = 'index.html'

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

class BlogsList(ListView):
    model = PostModel
    context_object_name = 'allblogs'
    paginate_by = 6
    queryset = PostModel.objects.order_by('-id')
    template_name = 'blogs.html'


class NewsList(ListView):
    model = PostModel
    context_object_name = 'allnews'
    paginate_by = 6
    queryset = PostModel.objects.order_by('-id').filter(post="ARKA NEWS")
    template_name = 'news.html'

class FactsList(ListView):
    model = PostModel
    context_object_name = 'allfacts'
    queryset = PostModel.objects.order_by('-id').filter(post="ARKA FACTS")
    template_name = 'facts.html'

class Notices(ListView):
    model = Announcements
    paginate_by = 6
    context_object_name = 'allnotice'
    queryset = Announcements.objects.order_by('-id')
    template_name = 'new.html'

class EventsList(ListView):
    model = PostModel
    context_object_name = 'allevents'
    paginate_by = 6
    queryset = PostModel.objects.order_by('-id').filter(post="ARKA EVENTS")
    template_name = 'event.html'

class BlogDetail(DetailView):
    model = PostModel
    context_object_name = 'blog'
    template_name = 'blog-detail.html'




class MembersList(ListView):
    model = TeamMember
    context_object_name = 'members'
    queryset = TeamMember.objects.order_by('admission_number')
    template_name = 'team.html'
    



def dashboard(request):
    return render(request,'dashboard.html')

def team(request):
    return render(request,'team.html')

def about(request):
    return render(request,'aboutus.html')




def blogDetail(request):
    return render(request, 'blog-detail.html')


