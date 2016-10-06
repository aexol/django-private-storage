from django.conf import settings

PRIVATE_STORAGE_ROOT = getattr(settings, 'PRIVATE_STORAGE_ROOT', None)
PRIVATE_STORAGE_SERVER = getattr(settings, 'PRIVATE_STORAGE_SERVER', 'django')
PRIVATE_STORAGE_AUTH_FUNCTION = getattr(settings, 'PRIVATE_STORAGE_AUTH_FUNCTION', 'apps.utils.private_storage.permissions.allow_superuser')

# For Nginx X-Accel-Redirect
PRIVATE_STORAGE_INTERNAL_URL = getattr(settings, 'PRIVATE_STORAGE_INTERNAL_URL', '/private-x-accel-redirect/')
