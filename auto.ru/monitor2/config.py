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
        'до 300к': 'https://discord.com/api/webhooks/928548929237319742/CYdBZlmPmCW5IyPDHvhx3QAs5EPs_R82-K6qewthwpu5bG14Z1QEq-RC5XYDKgg_nRsd',
        '300-700': 'https://discord.com/api/webhooks/928549013328900128/nIlMi8AU4JFq8fgYBciGz52Be4xlcMifZ9VerGdrNhLJNLBtftldtJ-xejseGDHC06lE',
        '700-1,5млн': 'https://discord.com/api/webhooks/928549051081850930/cEMbMwaPkROGF7hZooAA49-DCJgnsOE00x_LZzXnn2heQr68XaxuEh9f-UkXu0yPQdWq',
        '1,5млн>': 'https://discord.com/api/webhooks/928549090000785458/SEqm17L-JHGh1EFjj8Jehy2o8UDEziCgs2GPx9AflyqdJdF35HfMcLxNmqntiR4OsJ2u'
    },
    'Ростов-на-дону': {
        'до 300к': 'https://discord.com/api/webhooks/907327712799121449/ahnwgjQwwbpy8XeK4j36Q8LGxiIY-lL8GqWG6b0VfXXt36mpEEk63WQSfoQscDvvbHJC',
        '300-700': 'https://discord.com/api/webhooks/907327844772900874/awS1DISLXH6FiHI3kg6q1FieNcgZApIHM-XyMYoCneiLOVkE-LiErWzxgjLR4m2epOoS',
        '700-1,5млн': 'https://discord.com/api/webhooks/907327966298660905/s6JzdnDwpZtqgYnA2hH-yRgSuPJFVGiWoxNyGeyneOIB_RyN5GSZ4Pij7didW9CjoLTZ',
        '1,5млн>': 'https://discord.com/api/webhooks/907328074843054081/ce72Zg-vPvfv997IKwQxwi0sH6ujU7FaPzFl6aLaAz5ceriMbPsZKfPYkfm6XMYGxfoX'
    },
}