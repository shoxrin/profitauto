PARAMS = {
    'СПБ': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [10174],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [10174],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [10174],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "used",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [10174],
            'top_days': "1"
        }
    },
    'Архангельск': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [10842],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [10842],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [10842],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "used",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [10842],
            'top_days': "1",
        }
    },
}

WEBHOOK_URLS = {
    'СПБ': {
        #'до 300к': 'https://discord.com/api/webhooks/900166495085146122/Io8Qg_UsZzKRlee7nyfpRMA3BwOWnYYX3Nw1lubFJGWjN9AiSmQY_54Du8OdybI7sV4x',
        #'300-700': 'https://discord.com/api/webhooks/900704728353214466/NWgixfk3_nd6LSzaUV00K2E4IqckqGCdAeSmyoa013gQIZH7VcIgOyBCQzVzQC4jra8L',
        #'700-1,5млн': 'https://discord.com/api/webhooks/900704641820545054/wcPWP8uAqsTAUvJt_v1jKBV_Z2CfU7hVrbpAClnjkh9WjUN_BQkIaT7ERNx9qLS1ymqL',
        #'1,5млн>': 'https://discord.com/api/webhooks/900704451017469993/KR0VJxQrskaWJsEzRaEp2kYBQSJI5O7LC7R3vfrUkVrkwBcbJUWs0aawksZCI2tjaFIk'
        'до 300к': 'https://discord.com/api/webhooks/946626944651370537/vCN4Lqrf3qYz37SIPiTZGH3hRIIQ9lt50KZ7rmH20JWny7RhUvWGbC-nESNBtiHgMHMH',
        '300-700': 'https://discord.com/api/webhooks/946627044052193330/Swrk5_cGzV64MIrOLtoqUJCKhKFkWM4G5TLqpAgiwBCk5QgBTmvKbskEINXbKySLwkEF',
        '700-1,5млн': 'https://discord.com/api/webhooks/946627083805798421/8DHPZWzvPeUR8291Zx869TE570iCTfJeFUbhDHBfK56DZgJyClcdvqZJnbbo5dUvPmSS',
        '1,5млн>': 'https://discord.com/api/webhooks/946627126440890449/QyCuj02OcFxLuQ_Mf8WSbQPrDmeYOhSVctg4nlFigkqJKHcnYlsTS5IyGM7a_vwI2iID'
    },
    'Архангельск': {
        'до 300к': 'https://discord.com/api/webhooks/946627176109850694/Y9ktYb_eoH4fqFqWccMfYRTLfAO4oGtjBVPQrk6sq245xf2E7JOTak9v1l_NT-1I0cP1',
        '300-700': 'https://discord.com/api/webhooks/946627217641865246/-Bl6-8mgd9EC6dASWdhvrGReVtcF1rD72Xd94bsSwWwjTwO1HJLemHqiEGh4nX54vIdm',
        '700-1,5млн': 'https://discord.com/api/webhooks/946627257357705276/G1Oz2buTzpR1i8lh78fFPlRRPbuG3VxIGRdZfS4KO4nK14Pkj4POlmg-CSr5uQCYqH5w',
        '1,5млн>': 'https://discord.com/api/webhooks/946627298105360414/85Avnuq9pWDWTiVdAH-2bRs609IOLENe0vIj2C_x4rqjqzizkicu8RSkeueiSEICxzHR'
    },
}