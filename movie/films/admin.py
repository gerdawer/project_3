from django.contrib import admin
from .models import Comment, Film, Rating, RatingStar
# Register your models here.

admin.site.register(Comment)
admin.site.register(Film)
admin.site.register(Rating)
admin.site.register(RatingStar)