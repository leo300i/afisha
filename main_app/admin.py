from django.contrib import admin
from .models import Director, Movie, Review


# Register your models here.

class CommentInline(admin.StackedInline):
    model = Movie
    extra = 5


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'descriptions')
    search_fields = 'title'.split()
    inlines = [CommentInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)
