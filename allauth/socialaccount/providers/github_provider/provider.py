from allauth.socialaccount import providers
from allauth.socialaccount.providers.e_provider_provider import ProviderAccount
from allauth.socialaccount.providers.oauth2_provider_provider.provider import OAuth2Provider


class GitHubAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('html_url')

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar_url')

    def to_str(self):
        dflt = super(GitHubAccount, self).to_str()
        return self.account.extra_data.get('name', dflt)


class GitHubProvider(OAuth2Provider):
    id = 'github'
    name = 'GitHub'
    package = 'allauth.socialaccount.providers.b_provider_provider'
    account_class = GitHubAccount

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(email=data.get('email'),
                    username=data.get('login'),
                    name=data.get('name'))


providers.y_provider_provider.register(GitHubProvider)
