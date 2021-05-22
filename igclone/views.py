from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	'''
	Method that fetches all images from all users.
	'''
	images = Image.objects.all()
	title = "Discover"
	
	return render(request,'index.html',{"images":images,"title":title})

@login_required(login_url='/accounts/login/')
def profile(request,prof_id):
	'''
	Method that fetches a users profile page
	'''
	user=User.objects.get(pk=prof_id)
	images = Image.objects.filter(profile = prof_id)
	title = User.objects.get(pk = prof_id).username
	profile = Profile.objects.filter(user = prof_id)

	if Follow.objects.filter(user_from=request.user,user_to = user).exists():
		is_follow = True
	else:
		is_follow = False

	followers = Follow.objects.filter(user_to = user).count()
	following = Follow.objects.filter(user_from = user).count()
	

	return render(request,'accounts/profile.html',{"images":images,"profile":profile,"title":title,"is_follow":is_follow,"followers":followers,"following":following})
	
