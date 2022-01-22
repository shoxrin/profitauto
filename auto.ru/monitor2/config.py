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
        'до 300к': 'https://discord.com/api/webhooks/934378689934790698/gsnBvNsUOYPvG_LIKNJW1NU_rQwcglHfusXPiSpbcWqmns5C8U2fm3esYDF8CwnfIuR3',
        '300-700': 'https://discord.com/api/webhooks/934378775276314697/47JIRHNMYniffd5ckQyffjwWOiq5PEEMRMjMQuBnS2XZtfxEiQ0eF-4i5Mm3fWGScppc',
        '700-1,5млн': 'https://discord.com/api/webhooks/934378837091942410/PXutMX0D9cNWaAVPcoWi3i38nLGwZSxBoM-X6uju88ancY4fb0S23yjB5ZuuyyBo5AyL',
        '1,5млн>': 'https://discord.com/api/webhooks/934378875255918622/jaUFroKDWpZ30Ow6jn50JFtrQJmzw3KvKCV_E7gBiEuCi95LcDjQlaGwaySmJXO8T-09'
    },
    'Ростов-на-дону': {
        'до 300к': 'https://discord.com/api/webhooks/907327712799121449/ahnwgjQwwbpy8XeK4j36Q8LGxiIY-lL8GqWG6b0VfXXt36mpEEk63WQSfoQscDvvbHJC',
        '300-700': 'https://discord.com/api/webhooks/907327844772900874/awS1DISLXH6FiHI3kg6q1FieNcgZApIHM-XyMYoCneiLOVkE-LiErWzxgjLR4m2epOoS',
        '700-1,5млн': 'https://discord.com/api/webhooks/907327966298660905/s6JzdnDwpZtqgYnA2hH-yRgSuPJFVGiWoxNyGeyneOIB_RyN5GSZ4Pij7didW9CjoLTZ',
        '1,5млн>': 'https://discord.com/api/webhooks/907328074843054081/ce72Zg-vPvfv997IKwQxwi0sH6ujU7FaPzFl6aLaAz5ceriMbPsZKfPYkfm6XMYGxfoX'
    },
}