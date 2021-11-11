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
        'до 300к': 'https://discord.com/api/webhooks/906816748567805953/PXW_GTaxd2cGirw0D1IfbvATZBpCmjuNwob6Dd3NvBp41Cthc8dJEe3vhVZEoneEitsj',
        '300-700': 'https://discord.com/api/webhooks/906817042299109396/h9S8kV1rJOb3oBkVu4VovWoCvjwhF8alZN8Uvtld5F_YwnKrv0H4hxIYWNypJd51s3uN',
        '700-1,5млн': 'https://discord.com/api/webhooks/907967062809403442/G-cACgVGSnHAVize1U4bByGCCucV1ZhUQCe80f-qxLqzZmh6G6OxnLUgMSFghiKM-RNn',
        '1,5млн>': 'https://discord.com/api/webhooks/906817332846948382/o8P2LHSSsFofoRbVLPbTv7HAP0VQEartJ9tSTINgEo1WjqlHvGiojhJtfPMhYKBBDFWv'
    },
    'Архангельск': {
        'до 300к': 'https://discord.com/api/webhooks/906817212738863105/0abSYtxonQQ5XeyXufb7h-nFZ18LLGsMr2IqY9ddk9GfzXtHSfCCdCMm6U4JgMzKkC7Y',
        '300-700': 'https://discord.com/api/webhooks/906817468486516766/ti_CcWrWUP_XqdSYGD5bnbR4bamLKKti6scCuwsbsjgl0GQEyEpnYOpb52XAqJGJNxPH',
        '700-1,5млн': 'https://discord.com/api/webhooks/906817565307854898/E8O7lLDggtcim9zM6UZ5BSE07nvnQN9fn6KFJNX2ekhEvqKpaDU-62ehjvbZ4rgfjlCY',
        '1,5млн>': 'https://discord.com/api/webhooks/895275318527529040/EgL2LmPMAcGfu4cDAyj-t5CUhEn_VYZ3qZQD0IAIKylxmPUsb3JQXYi4CugQfEwaRzsg'
    },
}