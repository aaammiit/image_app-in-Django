Q. How to Upload Image and Show  in frontEnd and Save to  database
<br>
Ans. First create  virtual Envirnament and create project and app
<br>
then create image model and form =><br>

<--
from django.db import models
<br>
from django import forms
<br>


class Image(models.Model):
<br>
    image=models.ImageField(upload_to='images')
    <br>
    image_name=models.CharField(max_length=100)
    <br>
    image_desc=models.CharField(max_length=10000)
    <br>


class IForm(forms.ModelForm):
<br>
    class Meta:
    <br>
        model=Image
        <br>
        fields='__all__'    -->
        <br>


<--
Go To Settings.py =>
<br>Add these 2 lines
<br>
MEDIA_URL='www/as/asd/adf/'
<br>
MEDIA_ROOT=os.path.join(BASE_DIR, '')
<br>
-->


then create form in html and must be added => enctype="multipart/form-data" in form tag    =>
<br>
and map url in urls.py
<br>
Then go to Views
<br>
<--
view.py =>
<br>
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







