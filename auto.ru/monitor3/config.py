PARAMS = {
    'Самара': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [11131],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [11131],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [11131],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "used",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [11131],
            'top_days': "1"
        }
    },
    'Омск': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [11318],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [11318],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [11318],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "used",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [11318],
            'top_days': "1"
        }
    },
}

WEBHOOK_URLS = {
    'Самара': {
        'до 300к': 'https://discord.com/api/webhooks/930335583312707664/3mwK-YwSuRKw4XL8tJznW5mciM51iWFxtYD9NNmvsh9aYyCGeiHCKeqg04krAcZt7uQE',
        '300-700': 'https://discord.com/api/webhooks/930335627302563840/_JGUJzKxHijRpS_OZsBDR4dwN1gWCeDrt6zCokuVIi9oMBozQlfW298ts6GdGpR4Ih4F',
        '700-1,5млн': 'https://discord.com/api/webhooks/930335666867421184/vAhTngWp9Ub6ySlZBDcn3njjJ2fDsQH0Lb24aeON3vRQLzht0d3K0t7yVKV-dwjp1SPe',
        '1,5млн>': 'https://discord.com/api/webhooks/928549269177241670/Vvku_Xxy994N88IfHEQtGmfmsEDWP5mHI-yAPPf0bus0hWrt9do1kGpFepu46zkxVYpe'
    },
    'Омск': {
        'до 300к': 'https://discord.com/api/webhooks/928549311715868673/TU_xrpCJazHNYyundtJt9eBAzm4kGwA1s9Rh1RGVByTVm67bQMDx5lL9jJZPgqXAM0b_',
        '300-700': 'https://discord.com/api/webhooks/928549347338108969/fv3e6BF6fer66MEONlNZHLF8oyelaAs5tmgJxPV1FPyJ6UbsLubVIXpjvPthfbRUTD-M',
        '700-1,5млн': 'https://discord.com/api/webhooks/928549383048417310/nF4K-GhC12UCpzN1U7qtt4xoGh80v4h-lyV9w0txNPlnN-aMVK7_ATCk0kIHq6TpPAPN',
        '1,5млн>': 'https://discord.com/api/webhooks/928549437893140511/_mpwJPysQJwI78nu7UocWnjEsM6dS71s8ZNx1WnO_5VtQUGhwatbu-ie_Aty_NZuMQUu'
    },
}