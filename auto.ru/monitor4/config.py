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
        'до 300к': 'https://discord.com/api/webhooks/895273021894426665/XopIy4_TbxSaHDtJvpjydr1uilSBiStQfUCaELeRZ_QWJzsvBtMcQp0UvrkAc9wmhcRJ',
        '300-700': 'https://discord.com/api/webhooks/895272908153303100/WHHt961CgT4af1J81ftkCpTF-_nyCRcma02EPqskSmwwOSSO03leFHs9W8CoUQhf0fZR',
        '700-1,5млн': 'https://discord.com/api/webhooks/895272793229373460/W4t5v4q6mtsSs_L9jLLIK1QO1lHTol7WULody9BDXw1J4ZJW7CN3YK_M6pU6OOhL2kaG',
        '1,5млн>': 'https://discord.com/api/webhooks/895272687583236097/IM0h0lH1-OPIeGuxLMLne6nHl26Qat7dAyeK28_Su4cCF6mGcVvyRkzK7QcWZnP0nxwq'
    },
    'Казань': {
        'до 300к': 'https://discord.com/api/webhooks/895272541717938196/-f8mh1g-HbzgIj5ZvDSsUTjelhFRawzlVgKxaKkdK2KgScThf1rbS4zH1hG6J6RU0IcT',
        '300-700': 'https://discord.com/api/webhooks/895272419277807647/p5eigNdJpHk3h9bdqHqh6HWHrBqNR7JwHUgtpT25Lg-UtQpH88_gUAeRB0rDMXog_FpB',
        '700-1,5млн': 'https://discord.com/api/webhooks/895272274037456897/1qnT5S8vjvhI40pWOxzqYUXChSDpKdXBoIds1tKGN7Rda85fvEs44HppwLGQkRJKiEPr',
        '1,5млн>': 'https://discord.com/api/webhooks/895271472107515915/ll2z7VTfLkicye3AhxbJW5lWKExjrUKyBmjQxj2HaRrdWqJkK4AjEdbt4VBxDBbJMkhM'
    },
}