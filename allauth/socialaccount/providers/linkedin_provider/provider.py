from allauth.socialaccount import providers
from allauth.socialaccount.providers.e_provider_provider import ProviderAccount
from allauth.socialaccount.providers.h_provider_provider.provider import OAuthProvider

from allauth.socialaccount import app_settings


class LinkedInAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('public-profile-url')

    def get_avatar_url(self):
        return self.account.extra_data.get('picture-url')

    def to_str(self):
        dflt = super(LinkedInAccount, self).to_str()
        name = self.account.extra_data.get('name', dflt)
        first_name = self.account.extra_data.get('first-name', None)
        last_name = self.account.extra_data.get('last-name', None)
        if first_name and last_name:
            name = first_name+' '+last_name
        return name


class LinkedInProvider(OAuthProvider):
    id = 'linkedin'
    name = 'LinkedIn'
    package = 'allauth.socialaccount.providers.n_provider_provider'
    account_class = LinkedInAccount

    def get_default_scope(self):
        scope = []
        if app_settings.QUERY_EMAIL:
            scope.append('r_emailaddress')
        return scope

    def extract_uid(self, data):
        return data['id']

    def extract_common_fields(self, data):
        return dict(email=data.get('email-address'),
                    first_name=data.get('first-name'),
                    last_name=data.get('last-name'))

providers.y_provider_provider.register(LinkedInProvider)
