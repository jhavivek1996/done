from rolepermissions.permissions import register_object_checker
from webapp.roles import Library

@register_object_checker()
def publish_content(role, user, obj):
    if obj.owner == user:
        return True
    return False