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
        'до 300к': 'https://discord.com/api/webhooks/945706992952016986/wrImTiHOu4LRJgGAvlnp9r4sXIgY5lBlFqNloTSjaCFonkQ308SjiVZfpNmeez_8hjh9',
        '300-700': 'https://discord.com/api/webhooks/945707113446010900/7HQxkoaGn7-4mvsekMMxLFNEVwOMA1CobHOu1l3EoHB0j17oePn2Sxgy4uKCxees-S8j',
        '700-1,5млн': 'https://discord.com/api/webhooks/945707202704977970/-ASFWFnwd8eB8PMAF4wRlTMuER51sZEQLt6Ym56zsnRGDwX08wo-mJXD7Akqcrvyf-n2',
        '1,5млн>': 'https://discord.com/api/webhooks/945707351464353792/qFXWh0bwErUhlR8dRf77SBLXIOY1Do22GbQ9rCWEOUk9dY3ohysaL7e7Uqah_tIRkX8M'
    },
    'Ростов-на-дону': {
        'до 300к': 'https://discord.com/api/webhooks/946627379642654790/7p3goWFDTqwmJmgZntvvOjuBqHjG81ArAFbW4c73xhGSrYqboryshUcRCTUtarwSZ6fC',
        '300-700': 'https://discord.com/api/webhooks/946627443710631966/dXYaPocXQIceLD4wrbcI94BI8kVtzlz3i1GTp0_s9BRdOt6WNgjW4LVee10a9R2KpbRt',
        '700-1,5млн': 'https://discord.com/api/webhooks/946627485989232680/_0Bo3RgyG6v8H37l6NbS4_UGiQWUXJ5l0v8bFI-1Jf9bu5QvOxdAlSWk0YaUpV24xqN-',
        '1,5млн>': 'https://discord.com/api/webhooks/946627529719038022/UIdH78jOURKgBO10nADd4K-1LTxAONzKn9ApiFp5RJ4e_VdUNI8fmCD44O_5xj1zaGCJ'
    },
}