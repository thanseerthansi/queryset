from django.contrib import admin

from selectedrelated.models import Author, Books, Students, banking ,store

# Register your models here.
admin.site.register(Author)
admin.site.register(Books)
admin.site.register(store)
admin.site.register(banking)
admin.site.register(Students)