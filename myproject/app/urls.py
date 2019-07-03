
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexpage,name="indexpage"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('registerpage/',views.registerpage,name="registerpage"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('forgottpassword-page/',views.forgottpassword_page,name="forgottpassword-page"),
    path('forgottpassword/',views.forgottpassword,name="forgottpassword"),
    path('forgot-verification/',views.forgot_verification,name="forgot-verification"),
    path('reset-password/',views.reset_password,name="reset-password"),
    path('profile-page/',views.profile_page,name="profile-page"),
    path('update-profile-page/',views.update_profile_page,name="update-profile-page"),
    path('gallaryview/',views.gallaryview,name="gallaryview"),
    path('upload-img/',views.upload_img,name="upload-img"),
    path('videogallery/',views.videogallery,name="videogallery"),
    path('upload-video/',views.upload_video,name="upload-video"),
    path('audioview/',views.audioview,name="audioview"),
    path('upload-audio/',views.upload_audio,name="upload-audio"),
    path('contact-page/',views.contact_page,name="contact-page"),
    path('send-comment/',views.send_comment,name="send_comment"),
    path('my-comment/',views.my_comment,name="my-comment"),
    
    
]
