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

@login_required(login_url='/accounts/login/')
def create(request):
	'''
	Method that create an image post
	'''
	current_user = request.user
	profile = Profile.objects.get(user = request.user.id)
	title = "Create New Post"
	if request.method == 'POST':
		form = NewImagePost(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit =  False)
			post.profile = current_user
			post.user_profile = profile
			post.save()
			return redirect('profile',current_user.id)
	else:
		
		form = NewImagePost()

	return render(request,'accounts/create_post.html',{"form":form,"title":title})

@login_required(login_url='/accounts/login/')
def updateProfile(request):
	'''
	Method that updates a user's profile.
	'''
	current_user = request.user
	
	title = "Update Profile"
	if request.method == 'POST':
		if Profile.objects.filter(user_id = current_user).exists():
			form = UpdateProfile(request.POST,request.FILES,instance = Profile.objects.get(user_id = current_user))
		else:
			form = UpdateProfile(request.POST,request.FILES)
		if form.is_valid():
			userProfile = form.save(commit = False)
			userProfile.user = current_user
			userProfile.save()
			return redirect('profile',current_user.id)
	else:
		if Profile.objects.filter(user_id = current_user).exists():
			form = UpdateProfile(instance = Profile.objects.get(user_id = current_user))
		else:
			form = UpdateProfile()

	return render(request,'accounts/update_profile.html',{"form":form,"title":title})


@login_required(login_url='/accounts/login/')
def search(request):
	'''
	Method that searches for users based on their profiles
	'''
	if request.GET['search']:
		search_term = request.GET.get("search")
		profiles = Profile.objects.filter(user__username__icontains = search_term)
		message = f"{search_term}"

		return render(request,'accounts/search.html',{"message":message,"profiles":profiles})
	