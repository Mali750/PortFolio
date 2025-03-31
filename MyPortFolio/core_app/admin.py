from django.contrib import admin
from .models import Query_Details, model_login

# Register your models here.
@admin.register(Query_Details)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    # list_filter = ('name',)


@admin.register(model_login)
class modelAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'password')
