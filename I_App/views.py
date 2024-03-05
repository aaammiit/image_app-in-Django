from django.shortcuts import render,redirect,HttpResponse
from .models import Image,IForm
from django.views.generic import DeleteView,UpdateView
 

# Create your views here.
def Home(request):
    i=Image.objects.all()
    ir={'data':i}

    return render(request,'home.html',ir)

def Add_image(request):
    if request.method=='POST':
        pic=request.FILES.get('image')
        name=request.POST.get('image_name')
        desc=request.POST.get('image_desc')

        i=Image()
        i.image=pic
        i.image_name=name
        i.image_desc=desc
        try:
            i.save()
            return redirect('/')
        except:
            return HttpResponse('error')

    else:
        f=IForm()
        fr={'form':f}
        return render(request,'add_image.html',fr)

def Delete_view(request,id):
    d=Image.objects.get(id=id)
    d.delete()
    return redirect('/')

class Detail(DeleteView):
    model=Image
    template_name='detail_page.html'
    success_url='/'


class Update_dt(UpdateView):
    model=Image
    fields=['image_name','image_desc']
    template_name='update_dt.html'
    success_url='/'


def Search_view(request):
    srh=request.POST.get('srh')
    i=Image.objects.filter(image_name__icontains=srh)| Image.objects.filter(image_desc__icontains=srh)
    ir={'data':i}
    return render(request,'home.html',ir)