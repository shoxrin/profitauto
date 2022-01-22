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
        'до 300к': 'https://discord.com/api/webhooks/934379219243397130/ZYHfjZi2Wq8ZEkVOTn_I9gpuLXYfri52OVUVJfW6oPtdbvxRa4HPL9mzJdn6pPbSCAZd',
        '300-700': 'https://discord.com/api/webhooks/934379267733737493/gJmF3-RspFWiSx7SlfrAcXsQDC1e1gPdKnZ5-pH8pXnRqBaZ8g0cERvnJuRM6N-0Kcbs',
        '700-1,5млн': 'https://discord.com/api/webhooks/934379306820464690/9mSqLVOf4gi-eu5dUgMT0dYijGj-PWo0X5gUzX5Dv45MqfQndP2eiMwJ2s5m82O5sGeC',
        '1,5млн>': 'https://discord.com/api/webhooks/930335826146119710/HtoAKWJAGDxsDi1ZqBKxSjPJi64Nr6r2zGuMCbXXvyXmZq6YeflpG573r0DC1QB5YghX'
    },
    'Казань': {
        'до 300к': 'https://discord.com/api/webhooks/930335857997652028/YL8pIBtEhse0NrkoUVGU6s6vZIBQ4ynRGH32ijfqU1xk6edCNEA8kPItBj250Z7zTMHu',
        '300-700': 'https://discord.com/api/webhooks/930335891837308949/eYK6qliUFyEaz2fp2HKWs8UZwxk-_Sa-kfTT3I5aV5uYyu61K0IKgPpzmhuGZ-tvxRir',
        '700-1,5млн': 'https://discord.com/api/webhooks/930335931062448138/Wq_mSpWr8QamCM9sdK3SFswTwzkLlMERGxQKWffvfkq_s8R7aNZn8IcS6D2ISmoAsg8h',
        '1,5млн>': 'https://discord.com/api/webhooks/930335969708757012/ixUvrqROP87jNCCbAfPyWv-0Vo7Xjg6hY5wkeQLWb_DbNyeFhkJhZvexKEeoNukUvLPY'
    },
}