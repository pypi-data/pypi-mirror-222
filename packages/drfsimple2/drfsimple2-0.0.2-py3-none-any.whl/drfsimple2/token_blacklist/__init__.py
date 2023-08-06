from django import VERSION

if VERSION < (3, 2):
    default_app_config = (
        "drfsimple2.token_blacklist.apps.TokenBlacklistConfig"
    )
