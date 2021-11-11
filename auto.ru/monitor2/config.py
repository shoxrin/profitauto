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
        'до 300к': 'https://discord.com/api/webhooks/906817711454171176/1KTL0vf4No4BRq_yI6vl4hmco7Nh1YfUs08zDIW0CwAl_5UF6Sf_RaYdkeDhgF6o9Ty0',
        '300-700': 'https://discord.com/api/webhooks/906817801883385906/pzE8KK7rFFWdx12uuJZ6iu67r-A5B-jt-ZX3K9u-aB8OM_fopRi7hqnww_EWE5OCPo7E',
        '700-1,5млн': 'https://discord.com/api/webhooks/895274802556842004/lIxs3DlT38zbXXNnTzaP8ClsjEVcxxwh31BqGA8IePM5dvsi7XdhAtW4Fq9fS6377zy1',
        '1,5млн>': 'https://discord.com/api/webhooks/906817883512922152/bIGePgcGcO8Zm_7-Ib_dLLCvAPVCulDqrZXNgL-NSW_DJsiWN2ZrgeT5JnCrFNmzSSHZ'
    },
    'Ростов-на-дону': {
        'до 300к': 'https://discord.com/api/webhooks/907327669895589888/e5jYqnNlpCFimZoNZ3yBFD0a5mz2STAdjdqlV_5sHhVXVk0bDYaLT9JRUFBAiqWhAUL8',
        '300-700': 'https://discord.com/api/webhooks/907327797993832469/zd1x5Usod_-q9mXmDmOSfBH7P5ANVRQE9RVopFwSRQdRnrHHOnQs_uMfflkfTR1s7vaj',
        '700-1,5млн': 'https://discord.com/api/webhooks/907327914050207784/s7r6eh4TlSQ8XIugpthvtHeHGDifzVhvG8YfhX3qoVIlQsBdZUTtzV2e3AKPG7lHStKn',
        '1,5млн>': 'https://discord.com/api/webhooks/907328039195664464/uewPFT-wZg9SVhISbwV3SOg0518afm5SNHmBSzeoj9focM5OK93HSUQKX6D0B1z3XqL9'
    },
}