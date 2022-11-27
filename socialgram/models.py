from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    phone_no=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True)
    def __str__(self):
        return self.username
    
    
class PostModel(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=100)
    post_image=models.ImageField(upload_to='post-images',null=True,blank=True)
    post_desc=models.CharField(max_length=500)
    like=models.ManyToManyField(MyUser,related_name='like')
    
    
    @property
    def fetch_comments(self): 
        cmts=self.comments_set.all()
        return cmts

    def __str__(self):
        return self.post_title
    
    
class Comments(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    
    def __str__(self):
        return self.comment
    
    
class Saved(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    saved_post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.post.post_title