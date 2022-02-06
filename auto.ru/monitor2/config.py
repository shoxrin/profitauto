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
        'до 300к': 'https://discord.com/api/webhooks/939795693034414100/A1pf-5Ose9A7GduJzh5UCL5MXYXmOpSBPESJAEia_MC0oHFN_9z7iEFfXp_Vk1cbtsTp',
        '300-700': 'https://discord.com/api/webhooks/939795732095971338/s4Hiqn5RpwwOdmIeqsV9tjrLp3hAowOKYRp0So5A0v02pzX1o9xWDFU5cSGZBWJk_0Q4',
        '700-1,5млн': 'https://discord.com/api/webhooks/939795777851641906/YOGAR9eBYhtjhmZJ3RLWoZaKWKFaLCY_zk5FTPGS7heSO0vs6ngQaBy_bWJSiTiJcn7Q',
        '1,5млн>': 'https://discord.com/api/webhooks/939795809451524136/XCHKzYP7j5sHpTtu5VJn_XgfbpNsNAra1Z27bWDapxcqwVKbnYGzemYjNsdki1Y3UYvb'
    },
    'Ростов-на-дону': {
        'до 300к': 'https://discord.com/api/webhooks/939795843194695720/rOt29dUhOn8EjTBQn1Tp2055APctgK4ih_N_JD6vZpURztxSXVVP-av2njuwkvvQpQw0',
        '300-700': 'https://discord.com/api/webhooks/939795883581644831/wxFTwfqz4btBKUaiGvPCNkClB6qx6jNvPtQYVHHvGA84JtPKPgwX1vdsmd1e3z5DOLP_',
        '700-1,5млн': 'https://discord.com/api/webhooks/939795913566732338/EmeJBGaz-9_MMmu9AUlbSOlHueIA_TKuxAbJzhvGpeExzoXg35OXntnRb-ygI94m1ZKk',
        '1,5млн>': 'https://discord.com/api/webhooks/939795947054071868/_NGfZ7vpkUIvvsRiEnh0U-bDQvmQKnf_A38Skb0yJznco2g3oao2n5B696LOx-Cpzqg8'
    },
}