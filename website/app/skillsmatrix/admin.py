from django.contrib import admin

# Register your models here.
from website.app.skillsmatrix.models import Employee, Position

admin.site.register(Employee)
admin.site.register(Position)