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
        'до 300к': 'https://discord.com/api/webhooks/930335717169709076/ujn7Mtc2AA-pGbBMHmuR5TGdh1mG3zeOaVzjcyRU4RBqUgn3vYLeM6yG7HRVKj9to0Xy',
        '300-700': 'https://discord.com/api/webhooks/930335754675163206/JFL18ujlMc0zY8F4ev98i7Uf4w1vJyHz9ZXQ9LO1x7fERKaD_GgM5LP85xz5Zn1JQlgQ',
        '700-1,5млн': 'https://discord.com/api/webhooks/930335790481936385/1Z4S8gTDjUw2s666rOYZMikzKaKd9QUNiMC016wgoM-oDO5dHTgo66wAA19K9jmN64u2',
        '1,5млн>': 'https://discord.com/api/webhooks/930335826146119710/HtoAKWJAGDxsDi1ZqBKxSjPJi64Nr6r2zGuMCbXXvyXmZq6YeflpG573r0DC1QB5YghX'
    },
    'Казань': {
        'до 300к': 'https://discord.com/api/webhooks/930335857997652028/YL8pIBtEhse0NrkoUVGU6s6vZIBQ4ynRGH32ijfqU1xk6edCNEA8kPItBj250Z7zTMHu',
        '300-700': 'https://discord.com/api/webhooks/930335891837308949/eYK6qliUFyEaz2fp2HKWs8UZwxk-_Sa-kfTT3I5aV5uYyu61K0IKgPpzmhuGZ-tvxRir',
        '700-1,5млн': 'https://discord.com/api/webhooks/930335931062448138/Wq_mSpWr8QamCM9sdK3SFswTwzkLlMERGxQKWffvfkq_s8R7aNZn8IcS6D2ISmoAsg8h',
        '1,5млн>': 'https://discord.com/api/webhooks/930335969708757012/ixUvrqROP87jNCCbAfPyWv-0Vo7Xjg6hY5wkeQLWb_DbNyeFhkJhZvexKEeoNukUvLPY'
    },
}