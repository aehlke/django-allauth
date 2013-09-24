from allauth.socialaccount import providers
from allauth.socialaccount.providers.e_provider_provider import ProviderAccount
from allauth.socialaccount.providers.h_provider_provider.provider import OAuthProvider


class DropboxAccount(ProviderAccount):
    pass


class DropboxProvider(OAuthProvider):
    id = 'dropbox'
    name = 'Dropbox'
    package = 'allauth.socialaccount.providers.x_provider_provider'
    account_class = DropboxAccount

    def extract_uid(self, data):
        return data['uid']

    def extract_common_fields(self, data):
        return dict(username=data.get('display_name'),
                    name=data.get('display_name'),
                    email=data.get('email'))

providers.y_provider_provider.register(DropboxProvider)
