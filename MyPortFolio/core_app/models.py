from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Query_Details(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    subject = models.TextField(_("Message"))
    message = models.TextField(_("Query"))
    submitted_at = models.DateTimeField(_("Submitted_at"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    

class model_login(models.Model):
    user_name = models.CharField(_("User Name"), max_length=50)
    password = models.CharField(_("Password"), max_length=50)

    def __str__(self):
        return self.user_name
