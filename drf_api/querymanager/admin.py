from django.contrib import admin

from .models import Programmer, Query, Tag

admin.site.register(Programmer)
admin.site.register(Query)
admin.site.register(Tag)

