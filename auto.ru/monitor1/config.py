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
        'до 300к': 'https://discord.com/api/webhooks/906816948187320340/GzAvaJaLX2J827mHFJXNR9tTFcLr0x96AitQ_yJTK404XzuuXU9lOXdkJ24nnFgNI4Tx',
        '300-700': 'https://discord.com/api/webhooks/906817100033708064/dsKVFpqk2E9WdJmPsCO4jw2aw2TKKa-nqy5_xMjflHF4QMVDXJYKTyEGIXWmHSQ3MvJe',
        '700-1,5млн': 'https://discord.com/api/webhooks/907967079670489149/sbQw2ev7pankvWf3i4SS-rWho_MRHV8NoFLL4IAEFukyDheqk6s0QjOUkhZrL6iZkll2',
        '1,5млн>': 'https://discord.com/api/webhooks/906817349217320960/Tng_V5l-Vc7dgSx1fedMjuVv7XRMT-Q2Vjrv0dLq58dXQCt_vsziUhriP62OM2JNs5K_'
    },
    'Архангельск': {
        'до 300к': 'https://discord.com/api/webhooks/906817259287236648/FDN-kk-J5cIOtqcMVyfBPTfR7RNXRCNiaePf8vYrb07dBprxmUYGXjpYQDxD4fVeYYDR',
        '300-700': 'https://discord.com/api/webhooks/906817488648564756/TADybb944AisG2LSL3EqoFFOf0N2OfxwOwgSTuNFyV_Fkmf3rLvA-bfdH9cyMwSEo8aU',
        '700-1,5млн': 'https://discord.com/api/webhooks/906817617707286548/CNN44XElPUeVXZSrkUVjGCaAWeIMqv5WffACTWYI28YyE2BGfKogzWNDm5tTnb4aw4pC',
        '1,5млн>': 'https://discord.com/api/webhooks/908295029339095041/BURYxqFiHJms2lhjA-LDqIicaoe6eS4FDbnI2N9cVpdF-ewE85XtLK0JQk6aCBsyuin2'
    },
}