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
        'до 300к': 'https://discord.com/api/webhooks/945707729652162562/DQpbVIkP2yrQRqch6FzzsVablYx4l0o3vus7dO4G9HOtrTH9M71qhl6owNznYY8CsXva',
        '300-700': 'https://discord.com/api/webhooks/945707776720654388/lfrupcaQO4SdVtGgjuIhD21ltzEGFu7p-03OeOVhEqQ1uUMAbNIQAOpznthZDLID2P_K',
        '700-1,5млн': 'https://discord.com/api/webhooks/945707844798394378/CGQxtAkGwuEokvbaLEJ-KA-fNCd6sVU_jzexlnKxBfg9TWKLyjqlbsVW4wN3JlH3YM0V',
        '1,5млн>': 'https://discord.com/api/webhooks/946627733692243978/GonZoajJrTp4ElfsV6R0uL9wmCdxjGb5x1k-tiu6uGolIqefWc_6yOFA-SbLgOls2jw7'
    },
    'Казань': {
        'до 300к': 'https://discord.com/api/webhooks/946627770425938000/0_LfEy4fIC1lbyCERu8oRKWOHJS25uVS8q8CpxidmEVgjjXPOcQ4FssDM9e_rzbY_yIl',
        '300-700': 'https://discord.com/api/webhooks/946627809097433169/7TW-3wSIU9IOlm5Kjl7ODVrG8BphD1iUW_lfRdk6C8k0yWuFHOMGTVUdgHOFUKtAUPF6',
        '700-1,5млн': 'https://discord.com/api/webhooks/946627847743766548/6kJXDYcN9fGEwVxxMH2LBAUoILjxgFdi9lkjROaaw2aKz53NBV1W-dPOt4UPSB4toLYg',
        '1,5млн>': 'https://discord.com/api/webhooks/946627883168854126/2B8yPE5uo7QbXVB-_TQ9Lg6wx8cuYwuhQyVcGt_D34aqSA5qDTJGoCsIljmriuAQCyuT'
    },
}