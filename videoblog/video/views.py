from django.shortcuts import render,HttpResponse,redirect
from video.models import Video
from video.forms import VideoForm,SinupForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
# Create your views here.

def list_view(request):
    video_list = Video.objects.all()
    paginator=Paginator(video_list,3)
    page_number=request.GET.get("page")
    video_list=paginator.get_page(page_number)


    return render(request, "video/index.html", {'video_list': video_list})




@login_required
def home(request):
    if request.method == "POST":
        form=VideoForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request,"video/lastpage.html")

    else:
        form = VideoForm()
    return render(request,"video/form.html",{"form":form})
def sinup_views(request):
    form=SinupForm()
    if request.method=="POST":
        form=SinupForm(request.POST)
        form.save()
    return render(request,"video/sinupform.html",{"form":form})



@login_required
def delete(request,id):
    video=Video.objects.filter(id=id)
    video.delete()
    return redirect('/')


def thanking_view(request):
    return render(request,'video/logout.html')
