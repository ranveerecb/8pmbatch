from django.shortcuts import render


def home(request):
    ownerName='Ranveer'
    subjectsList=['SpringBoot','Angular','Devops']
    return render(request,'index.html',{'name':ownerName,'subjects':subjectsList})
def about(request):
    ownerNativePlace='Bihar'
    exp=8
    return render(request,'about.html',{'place':ownerNativePlace,'exp':exp})
def contact(request):
    ownerPhoneNumber=9568752456
    return render(request,'contact.html',{'phone':ownerPhoneNumber})
def contactprocess(request):
    #1.Read data from html form
    studName=request.GET.get('studentName')
    studMail=request.GET.get('studentMail')
    #2.Send name & email to notification.html
    return render(request, 'notification.html',{'name':studName,'email':studMail})