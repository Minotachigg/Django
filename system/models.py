from django.db import models
from django.contrib.auth.models import AbstractUser
# -------------------------------------------------------------------------------------------------

class User(AbstractUser):

    username = models.CharField(max_length = 100, unique=True)
    full_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    address = models.CharField(max_length = 100)
    badge_no = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.username

# -------------------------------------------------------------------------------------------------


class Crimelist(models.Model):

    SOURCE_CHOICES = (
        ('Theft', 'Theft'),
        ('Murder', 'Murder'),
        ('Fraud', 'Fraud'),
        ('Traficking', 'Traficking'),
        ('Kidnapping', 'Kidnapping'),
        ('Rape', 'Rape'),
    )

    # imp info
    title = models.CharField(choices = SOURCE_CHOICES, max_length = 100)
    city = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000)
    criminalDesc = models.TextField(max_length = 1000)
    date = models.DateTimeField(auto_now_add = True)
    done_by = models.CharField(max_length=30)

    # personal info
    reported_by = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField()

    SOURCE_CHOICES_STATUS = (
        ('PENDING...', 'Pending'),
        ('DONE.', 'Done'),
    )
    status = models.CharField(default = 'PENDING...', choices = SOURCE_CHOICES_STATUS, max_length=10)
    
    def __str__(self):
        return self.title


# -------------------------------------------------------------------------------------------------

class Complainlist(models.Model):

    # imp info
    title = models.CharField(max_length = 20)
    city = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000)
    date = models.DateTimeField(auto_now_add = True)
    done_by = models.CharField(default= None, max_length=30)


    # personal info
    reported_by = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField()

    SOURCE_CHOICES_STATUS = (
        ('PENDING...', 'Pending'),
        ('DONE.', 'Done'),
    )
    status = models.CharField(default = 'PENDING...', choices = SOURCE_CHOICES_STATUS, max_length=10)
    
    def __str__(self):
        return self.title


# -------------------------------------------------------------------------------------------------
class Contact(models.Model):

    # imp info
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 100)
    subject = models.CharField(max_length = 30)
    contDesc = models.TextField(max_length = 1000)
    date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.subject