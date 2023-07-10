from django.contrib import admin
from .models import Task, Label,Priority

# Register your models here.
admin.site.register(Task)
admin.site.register(Label)
admin.site.register(Priority)