from django.contrib import admin
from website.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tweet, TweetAdmin)