from django.contrib import admin
from blog.models import User, Group, Tag

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Tag)