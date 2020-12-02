from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
    id =models.AutoField(primary_key=True)
    title=models.CharField(max_length=127,verbose_name='Заголовок')
    content=models.TextField(verbose_name='Сообщение')
    timestamp= models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name='Дата создания')
    updated= models.DateTimeField(auto_now=True, auto_now_add=False,verbose_name='Дата создания')
    post_likes=models.IntegerField(default=0)
    status=(('r1','Роман'),('p','Поэма'),('r2','Реферат'),('r3','Рассказ'))
    status=models.CharField(max_length=2, choices=status, default='r1',verbose_name='Жанр')
    post_author=models.ForeignKey('Author', blank=True, null=True, verbose_name='Автор')
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return '{}'.format(self.id)
        return reverse('posts:detail',kwargs={'id':self.id})
    class Meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"
        db_table='posts'
        ordering=['-timestamp']

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=127, verbose_name='Имя')
    second_name = models.CharField(max_length=127, verbose_name='Фамилия')
    email=models.EmailField(max_length=254, verbose_name='Почтовый адрес')
    def __unicode__(self):
        return self.first_name+' '+self.second_name

    def __str__(self):
        return self.first_name+' '+self.second_name

    class Meta:
        verbose_name="Автор"
        verbose_name_plural="Авторы"
        db_table = 'authors'
        ordering=['second_name','first_name']

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comment_text = models.TextField(verbose_name='Комментарий')
    comment_article=models.ForeignKey(Post)
    timepublish = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True, verbose_name='Дата публикации')
    def __unicode__(self):
        return self.comment_text

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        db_table = 'comments'