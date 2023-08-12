from django.contrib import admin
from .models import Register , Email , Image , Hero , About , Team , Blog , Projects
# Register your models here.

admin.site.register(Register)
admin.site.register(Email)
admin.site.register(Image)
# <br>
admin.site.register(Hero)
admin.site.register(About)
admin.site.register(Team)

# <br>
admin.site.register(Blog)
admin.site.register(Projects)