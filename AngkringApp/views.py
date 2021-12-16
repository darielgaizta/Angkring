from django.shortcuts import render, redirect
from .models import Angkringan, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
	return render(request, 'home.html')

def angkringan(request, angkringan):
	username = request.GET.get('username')
	angkringan_details = Angkringan.objects.get(name=angkringan)
	return render(request, 'angkringan.html', {
		'username':username,
		'angkringan':angkringan,
		'angkringan_details': angkringan_details
	})

def checkview(request):
	''' Check if the angkringan exists in the database '''
	''' True: Redirect, False: Create new and redirect '''
	angkringan = request.POST['angkringan']
	username = request.POST['username']
	if Angkringan.objects.filter(name=angkringan).exists():
		return redirect('/'+angkringan+'/?username='+username)
	else:
		new_angkringan = Angkringan.objects.create(name=angkringan)
		new_angkringan.save()
		return redirect('/'+angkringan+'/?username='+username)

def send(request):
	''' Save the sent message to database '''
	''' HttpResponse will popped up by JS '''
	text = request.POST['message']
	user = request.POST['username']
	angkringan_id = request.POST['angkringan_id']
	new_message = Message.objects.create(text=text, user=user, angkringan=angkringan_id)
	new_message.save()
	return HttpResponse('Message is sent successfully.')

def getMessages(request, angkringan):
	''' Get objects of Message in JSON '''
	'''  JSON will be processed in JS  '''
	angkringan_details = Angkringan.objects.get(name=angkringan)
	messages = Message.objects.filter(angkringan=angkringan_details.id)
	return JsonResponse({"messages":list(messages.values())})