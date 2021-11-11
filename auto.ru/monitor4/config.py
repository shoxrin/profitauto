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
        'до 300к': 'https://discord.com/api/webhooks/907850593639485470/_A5lND5GDkQyIfjkG8Qn7Uq_9v37G7kqeqElXxVlMcauoChU4BjIz9jA4wWdcXbzRir3',
        '300-700': 'https://discord.com/api/webhooks/907966451858669590/5bpL_Uakw3Yp9e4n_b9Cws9_oXDQ_9bfQrjSC0bUiyvnIyd1vueG-op-bT4W0fb0Uqma',
        '700-1,5млн': 'https://discord.com/api/webhooks/907966574462373928/xUaZNkLTpURJZFSXW1kjNoniJXvj8ZfHzbef4aRY9UxFuiN_z7JUvT9Q1DRcOH6YgFPH',
        '1,5млн>': 'https://discord.com/api/webhooks/907966664027562039/PvYmN4k24GR4J9mgFIlSUVgFvdAO7Ivi46Tvrj48xQRrV0l8OqVrzEIRAyFWy4EZZhK_'
    },
    'Казань': {
        'до 300к': 'https://discord.com/api/webhooks/895272541717938196/-f8mh1g-HbzgIj5ZvDSsUTjelhFRawzlVgKxaKkdK2KgScThf1rbS4zH1hG6J6RU0IcT',
        '300-700': 'https://discord.com/api/webhooks/895272419277807647/p5eigNdJpHk3h9bdqHqh6HWHrBqNR7JwHUgtpT25Lg-UtQpH88_gUAeRB0rDMXog_FpB',
        '700-1,5млн': 'https://discord.com/api/webhooks/895272274037456897/1qnT5S8vjvhI40pWOxzqYUXChSDpKdXBoIds1tKGN7Rda85fvEs44HppwLGQkRJKiEPr',
        '1,5млн>': 'https://discord.com/api/webhooks/895271472107515915/ll2z7VTfLkicye3AhxbJW5lWKExjrUKyBmjQxj2HaRrdWqJkK4AjEdbt4VBxDBbJMkhM'
    },
}