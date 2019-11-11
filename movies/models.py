from django.db import models
# Create your models here.
class Collection(models.Model):
    c_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField(blank=True, null=True)
    m_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection'


class Movies(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_name = models.CharField(max_length=255)
    m_dir = models.CharField(max_length=255, blank=True, null=True)
    m_actor = models.TextField(blank=True, null=True)
    m_type = models.CharField(max_length=255)
    m_nation = models.CharField(max_length=255, blank=True, null=True)
    m_data = models.CharField(max_length=255, blank=True, null=True)
    m_length = models.CharField(max_length=50, blank=True, null=True)
    m_tecentlink = models.CharField(max_length=255, blank=True, null=True)
    m_post = models.ImageField(upload_to='static/img')
    m_iqylink = models.CharField(max_length=255, blank=True, null=True)
    m_youkulink = models.CharField(max_length=255, blank=True, null=True)
    m_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    u_password = models.CharField(max_length=50,blank=True, null=True)
    u_history = models.CharField(max_length=255, blank=True, null=True)
    u_tel = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'user'