PARAMS = {
    'МСК': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [213],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [213],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [213],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "used",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [213],
            'top_days': "1"
        }
    },
    'Ростов-на-дону': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [39],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [39],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [39],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "used",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [39],
            'top_days': "1",
        }
    },
}

WEBHOOK_URLS = {
    'МСК': {
        'до 300к': 'https://discord.com/api/webhooks/906817751052603392/gVmOmN2yLZWo2_xH9b-iq4NtQbsFBjx2L_0q0tlCX-csrvDgJfZ5j0MScnipVukRazye',
        '300-700': 'https://discord.com/api/webhooks/906817833210642464/iYnrbOd6rWTeatECmgII0R66rwfYjvikAEJTUsc6sz81CPdDkKTwbyOTCFUDenK8s_TU',
        '700-1,5млн': 'https://discord.com/api/webhooks/908295346378129458/-pvAyMkCDfDWTGIxj5EywFNyyHDx3KuxTXE6M7zzQl_coE5fiwl_hS6dIJEaFbh0--hh',
        '1,5млн>': 'https://discord.com/api/webhooks/907327619832348694/qLD3iyIkLAnS_LZbfd-n0OsYOUuj1vABe_jAncMJYVOktUvIcYTHRoDqIPTFyCI5jtEq'
    },
    'Ростов-на-дону': {
        'до 300к': 'https://discord.com/api/webhooks/907327690149859378/bhrB-sfE-O3WgImrzJ_gKw9lptkalP27eLML0ByPNAsIMk64v9Bj5PBdxUSCvmJwuwQD',
        '300-700': 'https://discord.com/api/webhooks/907327821901344829/9-KIUETPcUzPjN_5IABRv8vqk_R0qtXXZeJ2RJat0E9WRVqLf5kweeXzAxLOLv49pzWG',
        '700-1,5млн': 'https://discord.com/api/webhooks/907327931464970260/e4u-b1_KWNRmgUm1mlqDQ8Dr_VMERPfksdQwSYDxh-YJd7U-MFyMw2xCVAgdTvG7n5mj',
        '1,5млн>': 'https://discord.com/api/webhooks/907328055775752224/z2x18KgDu9am3wdt5iXXL7ZhS4nHl17LNxPATMECqr8Ue6VTOmGclMS5VhkmPhwoN7IG'
    },
}