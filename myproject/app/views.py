from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from django.core.mail import send_mail
from random import *
from .utils import sendmail

# Create your views here.

# online Lecture - Food blog
def indexpage(request):
    return render(request,"app/index.html")

def loginpage(request):
    return render(request,"app/login.html")

def registerpage(request):
    return render(request,"app/registration.html")

def register(request):
    obj=User()
    obj.username=request.POST['username']
    obj.email=request.POST['email']
    obj.password=request.POST['password']
    insert=User.objects.create(username=obj.username,email=obj.email,password=obj.password)
    Subject="Confirmation Mail"
    Message="Hello "+obj.username+" , Welcome to Food Blog"
    send_mail("Confirmation Mail",Message,"anjali.20.learn@gmail.com",[obj.email])
    return render(request,"app/login.html")
    
def login(request):
    if 'email' in request.session:
        u_data=User.objects.get(email=request.session['email'])
        return render(request,"app/index.html",{'u_data':u_data})
    else:
        try:
            email=request.POST['uemail']
            password=request.POST['upassword']
            u_data=User.objects.get(email=email)
            if u_data.email==email and u_data.password==password:
                request.session['id']=u_data.id
                request.session['email']=u_data.email
                request.session['username']=u_data.username
                return render(request,"app/index.html",{'u_data':u_data})
            else:
                msg="invalid password"
                return render(request,"app/login.html",{'msg':msg})
        except:
            msg="user does not exist"
            return render(request,"app/login.html",{'msg':msg})
        
    
def logout(request):
    del request.session['id']
    del request.session['email']
    del request.session['username']
    return HttpResponseRedirect(reverse('loginpage'))
    
def forgottpassword_page(request):
    return render(request,"app/forgottpassword.html")

def forgottpassword(request):
    email=request.POST['email']
    try:
        user=User.objects.get(email=email)
        if user.email==email:
            otp=randint(1000,9999)
            user.otp=otp
            user.save()
            email_subject="Food blog - Forgot Password"
            print("email ---> ",email)
            sendmail(email_subject,'mail_template',email,{'otp':otp,'link':'http://localhost:8000/foodblog/forgot-verification.html/'})
            return render(request,"app/forgot-verification.html",{'email':email})
        else:
            msg="invalid email"
            return render(request,"app/forgottpassword.html",{'msg':msg})
    except:
        msg="User does not exist"
        return render(request,"app/forgottpassword.html",{'msg':msg})

def forgot_verification(request):
    return render(request,"app/forgot-verification.html")

def reset_password(request):
    email=request.POST['email']
    otp=request.POST['otp']
    newpassword=request.POST['newpassword']
    confpassword=request.POST['confpassword']
    try:
        user=User.objects.get(email=email)
        if confpassword==newpassword and str(user.otp)==otp:
            user.password=newpassword
            user.save()
            return render(request,"app/login.html")
        else:
            msg = "Either password and confirm password doesn't match or you have entered a wrong otp"
            return render(request,"app/forgot-verification.html",{'msg':msg})
    except:
        msg= "invalid request"
        return render(request,"app/forgot-verification.html",{'msg':msg})

def profile_page(request):
    u_id=request.session['id']
    u_data=User.objects.get(id=u_id)

    return render(request,"app/profile.html",{'u_data':u_data})

def update_profile_page(request):
    user=User.objects.get(id=request.session['id'])
    user.username=request.POST['username']
    user.email=request.POST['email']
    user.password=request.POST['password']
    user.profile_pic=request.FILES['pic']
    user.save()  # update profile
    return render(request,"app/profile.html")

def gallaryview(request):
    getall=GalleryView.objects.all()
    return render(request,"app/gallary.html",{'getall':getall})
    
def upload_img(request):
    pic=request.FILES['pic']
    insert=GalleryView.objects.create(pic=pic)
    getall=GalleryView.objects.all()
    return render(request,"app/gallary.html",{'getall':getall})

def videogallery(request):
    getall=VideoGallery.objects.all()
    return render(request,"app/videogallery.html",{'getall':getall})

def upload_video(request):
    name=request.POST['name']
    video=request.FILES['videofile']
    print("--------------> ",video)
    insert=VideoGallery.objects.create(name=name,videofile=video)
    getall=VideoGallery.objects.all()
    return render(request,"app/videogallery.html",{'getall':getall})

def audioview(request):
    getall=AudioGallery.objects.all()
    return render(request,"app/audioview.html",{'getall':getall})

def upload_audio(request):
    name=request.POST['name']
    audiofile=request.FILES['audiofile']

    insert=AudioGallery.objects.create(name=name,audiofile=audiofile)

    getall=AudioGallery.objects.all()
    return render(request,"app/audioview.html",{'getall':getall})

def contact_page(request):
    username=request.session['username']
    return render(request,"app/contact.html",{'username':username})

def send_comment(request):
    username=request.POST['username']
    email=request.POST['email']
    subject=request.POST['subject']
    message=request.POST['message']

    insert=Comments.objects.create(username=username,email=email,subject=subject,message=message)

    return render(request,"app/index.html")

def my_comment(request):
    getall=Comments.objects.all()
    return render(request,'app/mycomments.html',{'getall':getall})
