from allauth.socialaccount.providers.h_provider_provider.urls import default_urlpatterns

from .provider import TwitterProvider

urlpatterns = default_urlpatterns(TwitterProvider)
