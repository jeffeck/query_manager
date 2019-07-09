from django.contrib import admin

from .models import Programmer, Query, Tag

admin.site.register(Programmer)
admin.site.register(Tag)

# admin.site.register(Query)
# Query model contains auto-add fields (timestamps) that are set to editable=False
# To display them, see the class and tag below

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]


    