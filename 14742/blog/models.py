from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def copy(self):
        new_post = BlogPost.objects.create(title=self.title, body=self.body, author=self.author)
        for comment in self.comments.all():
            Comment.objects.create(blog_post=new_post, text=comment.text)
        new_post.date_created = models.DateTimeField(auto_now_add=True)
        new_post.id = models.AutoField(primary_key=True)
        new_post.save()
        return new_post.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
