from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio =  models.TextField(blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    @classmethod
    def search_user(cls,username): 
        return User.objects.filter(username = username)
        
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length = 30)
    caption = models.TextField(blank= True)
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Profile, related_name="posts")
    
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

    def like_count(self):
        return self.likes.count()

    @classmethod
    def get_profile_images(cls,profile):
        return cls.objects.filter(profile = profile)

    class Meta:
        ordering = ['-post_date']

class Comment(models.Model):
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete= models.CASCADE, related_name = "comments")

    def __str__(self):
        return self.content

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls,image):
        return cls.objects.filter(image =image)

    class Meta:
        ordering = ['-post_date']

class Follow(models.Model): 
    posted = models.DateTimeField(auto_now_add=True)
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_followed')
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_following')

    def __str__(self):
        return self.pk 












































































































































# from django.db import models
# from django.contrib.auth.models import User
# from tinymce.models import HTMLField
# import datetime as dt

# # Create your models here.
# class Profile(models.Model):
# 	bio = models.CharField(max_length = 300,blank = True,default = 'Bio Will Appear Here')
# 	profile_pic = models.ImageField(upload_to = 'profile/', blank = True,default = '../static/images/default.png')
# 	user = models.ForeignKey(User, on_delete = models.CASCADE)



	
# 	def __str__(self):
# 		return self.user

# 	@property
# 	def all_comments(self):
# 		return self.comments.all()

# class Image(models.Model):
	
# 	image_name = models.CharField(max_length = 60, blank = True)
# 	image_caption = models.CharField(max_length = 60, blank = True)
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	profile = models.ForeignKey(User, on_delete=models.CASCADE)
# 	user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
# 	likes = models.ManyToManyField(User,related_name = 'likes', blank = True)
# 	image = models.ImageField(upload_to = 'images/', blank = True)


# 	@classmethod
# 	def save_image(self):
# 		self.save()

# 	@classmethod
# 	def delete_image(self):
# 		self.delete()

# 	@classmethod
# 	def update_caption(cls,id,caption):
# 		updated_caption = cls.objects.filter(pk = id).update(image_caption = caption)
# 		return updated_caption

# 	@classmethod
# 	def get_image_by_id(cls,image_id):
# 		image = cls.objects.get(id = image_id)
# 		return image

# 	def total_likes(self):
# 		self.likes.count()

# 	@property
# 	def all_comments(self):
# 		return self.comments.all()

# 	def __str__(self):
# 		return self.image_name

# class Comment(models.Model):
# 	comment = models.CharField(max_length = 1000)
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	image = models.ForeignKey(Image, on_delete=models.CASCADE)
# 	profile = models.ForeignKey(User, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.profile

# #Add the following field to User dynamically
# 	def get_first_name(self):
# 		return self.first_name

# class Follow(models.Model):
#     user_from = models.ForeignKey(User,on_delete=models.CASCADE, related_name='rel_from_set')
#     user_to = models.ForeignKey(User,on_delete=models.CASCADE, related_name='rel_to_set')
  
#     def __str__(self):
#         return '{} follows {}'.format(self.user_from, self.user_to)