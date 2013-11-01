import re

from django import template

register = template.Library()

@register.filter(name='mention')
def mention(value):
    return re.sub(r'\@(\w+)', r'<a href="/user/\1">@\1</a>', value)

mention.is_safe = True

@register.inclusion_tag('website/toggle_follow.html')
def follow_or_unfollow_link(user, list_user):
    is_friend = user.profile.following.filter(user=list_user).exists()
    return {'is_friend': is_friend, 'list_user': list_user}