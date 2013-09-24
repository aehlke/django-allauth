from allauth.socialaccount import providers
from allauth.socialaccount.providers.e_provider_provider import ProviderAccount
from allauth.socialaccount.providers.oauth2_provider_provider.provider import OAuth2Provider


class VKAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('link')

    def get_avatar_url(self):
        return self.account.extra_data.get('picture')

    def to_str(self):
        dflt = super(VKAccount, self).to_str()
        return self.account.extra_data.get('name', dflt)


class VKProvider(OAuth2Provider):
    id = 'vk'
    name = 'VK'
    package = 'allauth.socialaccount.providers.k_provider_provider'
    account_class = VKAccount

    def extract_uid(self, data):
        return str(data['uid'])

    def extract_common_fields(self, data):
        return dict(last_name=data.get('family_name'),
                    username=data.get('screen_name'),
                    first_name=data.get('given_name'))


providers.y_provider_provider.register(VKProvider)
