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
        'до 300к': 'https://discord.com/api/webhooks/940000329393655828/44ZBYyi-zNuDa5KkbC0lft4gL3xALFfWya_qXEKFG-EjnswFbBuI-UValaLo1dTDmMQa',
        '300-700': 'https://discord.com/api/webhooks/940000410830241812/stuIQwx1CURwJ94hEcECGNvKvGovxFNHjXnA53-Cl5NNiTOVk8PnLutpQV0LJNM4sgWb',
        '700-1,5млн': 'https://discord.com/api/webhooks/940000447782064178/fkbDaRi9UNeZcLgvWcryLfU9wjPPDAV8ocxuoWr6Ic2HmTveu-440aWb9oHojUYpKRI5',
        '1,5млн>': 'https://discord.com/api/webhooks/940000498784800850/v6c4TfAZSu8bZME8Rb2BUugJ2LnYJIHno3u9b9xPzTsMrqEO_7mNgQMrz4t0hG0_Fl-K'
    },
    'Казань': {
        'до 300к': 'https://discord.com/api/webhooks/940000534058926081/h7ItbeJbmnCmsPytgmUSpNmtQtYf7M1DNF--YXWbqC-86YBF5pBhavoYyzfHN0P89C-Q',
        '300-700': 'https://discord.com/api/webhooks/940000565168078899/VRBh96vzqntDYzj9fzTHjbGt2j5ZCOVxjcDWtOmqDAlveV-70o9QuKlNSVapOS55bJqF',
        '700-1,5млн': 'https://discord.com/api/webhooks/940000599431315457/_E65du2PlLQ2czkRq8IU67FPHhKCbakyEKkt_3uwRUxPcgTsrwgEjwI9fLUp-piykJ2e',
        '1,5млн>': 'https://discord.com/api/webhooks/940000636626403391/wbUXtKpNVrgyYyAcq4DlS-BoKVPHlcJmsqa924RLnhEeojz9cw0a1-j_mKcMDsCrNobL'
    },
}