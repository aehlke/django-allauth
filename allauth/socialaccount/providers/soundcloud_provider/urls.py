from allauth.socialaccount.providers.oauth2_provider_provider.urls import default_urlpatterns
from .provider import SoundCloudProvider 

urlpatterns = default_urlpatterns(SoundCloudProvider)
