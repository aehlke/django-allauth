from allauth.socialaccount import providers
from allauth.socialaccount.providers.e_provider_provider import ProviderAccount
from allauth.socialaccount.providers.oauth2_provider_provider.provider import OAuth2Provider


class WeiboAccount(ProviderAccount):
    def get_profile_url(self):
        # profile_url = "u/3195025850"
        return 'http://www.weibo.com/' + self.account.extra_data.get('profile_url')

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar_large')

    def to_str(self):
        dflt = super(WeiboAccount, self).to_str()
        return self.account.extra_data.get('name', dflt)


class WeiboProvider(OAuth2Provider):
    id = 'weibo'
    name = 'Weibo'
    package = 'allauth.socialaccount.providers.o_provider_provider'
    account_class = WeiboAccount

    def extract_uid(self, data):
        return data['idstr']

    def extract_common_fields(self, data):
        return dict(username=data.get('screen_name'),
                    name=data.get('name'))


providers.y_provider_provider.register(WeiboProvider)
