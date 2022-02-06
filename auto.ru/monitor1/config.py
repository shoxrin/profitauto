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
        'до 300к': 'https://discord.com/api/webhooks/939795327555358760/u3ypOeuhMVzzJ9ZKuzajOvxclaqPaxDbtqhgUEhUF5Y3rci_i9oW21jFyXxpByhg6wy0',
        '300-700': 'https://discord.com/api/webhooks/939795435470598144/sNG5opqxBzkMWCd1A_jGaOdnFVKShzPiSJKyGNG_kiyTCsQKbNpAVAjRvFn0Q_oVdTFp',
        '700-1,5млн': 'https://discord.com/api/webhooks/939795468416876575/lCTvaD0GGW67kY32zjkyhVOUQ7r90hs-uob5G4pIdXaXKrYi7Mt9scEEd35C3MgoV9aT',
        '1,5млн>': 'https://discord.com/api/webhooks/939795506438238228/pj5--me0J7ItedSRYOYqdomL1s_QRmWhEBkezC6X5fwXEkP4wvaHUlZQoXHXDv51mF0y'
    },
    'Архангельск': {
        'до 300к': 'https://discord.com/api/webhooks/939795545986301972/a165IKtfB0kpugHUtMpeP2HZ0jVgodW9597w4I6hQwaPjPoa6W9AsDbUHPpI6udyaFcw',
        '300-700': 'https://discord.com/api/webhooks/939795588105502770/BH17BEd-r9-S61vf6qBHa5QytAc4RiGXljEt5OIfb9Uru-zj1hBI6MVflP02kuEEnnOR',
        '700-1,5млн': 'https://discord.com/api/webhooks/939795626374352926/EW0jiZn6jZ5Xh3n3-XkCtLTZGMh-GoAZvMx5JvzhTnw2f6TUDDqIgG1DMFfXbyZcdZTf',
        '1,5млн>': 'https://discord.com/api/webhooks/939795660406923294/tcvry8c-w4lS-1c971EmdXWP8eiVD5QOhCSKu7C2qeVTFkKeoYX5SSWSBH5DX-Qx9oci'
    },
}