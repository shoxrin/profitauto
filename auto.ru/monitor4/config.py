PARAMS = {
    'ЕКБ': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [54],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [54],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [54],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "used",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [54],
            'top_days': "1"
        }
    },
    'Казань': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [43],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [43],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [43],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "used",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [43],
            'top_days': "1"
        }
    },
}

WEBHOOK_URLS = {
    'ЕКБ': {
        'до 300к': 'https://discord.com/api/webhooks/907966413669531670/20vjXG1TGscKzgyUM13W7LTPWtGB8P2N6BYwmPj5i-tiUMMDsXCIqh9gVqGL8KovpA09',
        '300-700': 'https://discord.com/api/webhooks/907966504530743306/wslanh2nTQ-CfRd5jLUkLgmXwqZH_MQ4mOCQPAQI4O1M2Ps12cH2j4KO_l_wWQ4bvP2D',
        '700-1,5млн': 'https://discord.com/api/webhooks/907966609849737277/AgqSCHqYvqW-NtI7q2N3InSxBpflWnl9eHwJDhDAGQlc-DPRY5QB5Y29jCwWaV0rFL3y',
        '1,5млн>': 'https://discord.com/api/webhooks/907966682813837322/suFUZvxW2gx0pmIGVUsfjoa3BzNN5BLECi1UgfrcNFnCCHQIKJKQ8ltFoINRFgM_2LO1'
    },
    'Казань': {
        'до 300к': 'https://discord.com/api/webhooks/907966739088830464/wlhWUoWhImPoMM8w55rXLmE_O3uF56DGCgTdp9EJxZhzPf6xxnNBJ2g1ldWq74TQ-qYx',
        '300-700': 'https://discord.com/api/webhooks/907966814867304448/1f9hY4lvKQ0THf3mWtd6kPyvqJ-QLmavLOXN1PLHpihKbbxAF9_1mnj1_NWqNtJK9uml',
        '700-1,5млн': 'https://discord.com/api/webhooks/907966891472089178/ouoqKvhPAOT1sbY0KAusE0GfKvSjqWmpaD4Oy7T_8GHVzGIxP53KHS71qJTcctx8QKow',
        '1,5млн>': 'https://discord.com/api/webhooks/907966955414233168/UgGvT1bIpwOg49LP6BvSsQw0XxulTLw9PKHpx8DD3YMNlOtXBMdUxgVvmlG9Zmau9_ip'
    },
}