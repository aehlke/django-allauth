from allauth.socialaccount import providers
from allauth.socialaccount.providers.e_provider_provider import ProviderAccount
from allauth.socialaccount.providers.h_provider_provider.provider import OAuthProvider


class VimeoAccount(ProviderAccount):
    pass


class VimeoProvider(OAuthProvider):
    id = 'vimeo'
    name = 'Vimeo'
    package = 'allauth.socialaccount.providers.o_provider_provider'
    account_class = VimeoAccount

    def get_default_scope(self):
        scope = []
        return scope

    def extract_uid(self, data):
        return data['id']

    def extract_common_fields(self, data):
        return dict(name=data.get('display_name'),
                    username=data.get('username'))


providers.y_provider_provider.register(VimeoProvider)
