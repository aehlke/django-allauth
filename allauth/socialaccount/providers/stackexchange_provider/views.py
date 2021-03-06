import requests

from allauth.socialaccount.providers.oauth2_provider_provider.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)
from allauth.socialaccount.providers import registry

from .provider import StackExchangeProvider


class StackExchangeOAuth2Adapter(OAuth2Adapter):
    provider_id = StackExchangeProvider.id
    access_token_url = 'https://stackexchange.com/oauth/access_token'
    authorize_url = 'https://stackexchange.com/oauth'
    profile_url = 'https://api.stackexchange.com/2.1/me'

    def complete_login(self, request, app, token, **kwargs):
        provider = registry.by_id(app.provider)
        site = provider.get_site()
        resp = requests.get(self.profile_url,
                            params={'access_token': token.token,
                                    'key': app.key,
                                    'site': site})
        extra_data = resp.json()['items'][0]
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth2_login = OAuth2LoginView.adapter_view(StackExchangeOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(StackExchangeOAuth2Adapter)
