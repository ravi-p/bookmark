from django.contrib import admin
from bookmarks.models import *
class LinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(Link, LinkAdmin)

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'user')
    list_filter = ('user',)
    ordering = ('title',)
    search_fields = ('title',)
admin.site.register(Bookmark, BookmarkAdmin)

class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)

class SharedBookmarkAdmin(admin.ModelAdmin):
    pass
admin.site.register(SharedBookmark, SharedBookmarkAdmin)
