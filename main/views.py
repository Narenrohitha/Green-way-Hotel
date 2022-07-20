from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def home(request):
	return render(request,'main/home.html')

def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			Full_Name = form.cleaned_data['Full_Name']
			Email = form.cleaned_data['Email']
			Phone_No = form.cleaned_data['Phone_No']
			Message = form.cleaned_data['Message']

			Subject = "Response From contact Form"
			Message = "Name: "+Full_Name+"\nEmail: "+Email+"\nPhone_No"+Phone_No+'\nMessage'+Message
			Recipient = ['narenrohitha@gmail.com']
			sender = 'narenngl2001@gmail.com'

			send_mail(Subject,Message,sender,Recipient)


	else:
		form = ContactForm()

def about(request):
	return render(request,'main/about.html')

def menu(request):
	return render(request,'main/menu.html')

def specials(request):
	return render(request,'main/specials.html')

def events(request):
	return render(request,'main/events.html')

def contact(request):
	form = ContactForm()
	return render(request,'main/contact.html',{'form':form})

