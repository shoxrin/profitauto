PARAMS = {
    'Самара': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [11131],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [11131],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [11131],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [11131],
            'top_days': "1"
        }
    },
    'Омск': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [11318],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [11318],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [11318],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [11318],
            'top_days': "1"
        }
    },
}

WEBHOOK_URLS = {
    'Самара': {
        'до 300к': 'https://discord.com/api/webhooks/895273910659067904/J5ANGHj8IGT5XA4HeKK2kb9V7chxRn2iblI5ptvB8S4UZqc1auX6oXxLtqLXV4xUmevv',
        '300-700': 'https://discord.com/api/webhooks/895273809224011846/2_Uprfl3rbN9338IUfyUu-czUecIVG6pG6slCAy5u_sgNpHWPSHvaum_yJRgMIZkJBZS',
        '700-1,5млн': 'https://discord.com/api/webhooks/895273715498106902/0XiAdPWGq9Bu9nZjZmNHtMGSowYVgjVCei-j5ENu40Qi1vRlj-e2AT8yRdAynkCbaxmG',
        '1,5млн>': 'https://discord.com/api/webhooks/895273625156993035/6g5RH-J5ZPjcXcO-ZywG3i-ewTXI5CVzwcQWnjmGPjStqwRJ9SaioTo84g7XAbk4suqh'
    },
    'Омск': {
        'до 300к': 'https://discord.com/api/webhooks/895273506097483876/jQgUyTjsuWv8F53M4pClIy7JJBwqAkG6wMQWZn8MpBW5Drr4M7uInZeqBF1LFNXIhTaF',
        '300-700': 'https://discord.com/api/webhooks/895273411310395412/kn5KtRdr4o9iqnfUOjim2VSJBRxYOOo6ZjiWlXtmCH7gDXZXXdI82jRP0c6SZYvfvQkW',
        '700-1,5млн': 'https://discord.com/api/webhooks/895273317991333941/41W7PCxpGXkSUjQCRB5-Mg2_swgZhgI63yBwB408t8pGlQ3ok_FtQjrnXwfENKR5JNxb',
        '1,5млн>': 'https://discord.com/api/webhooks/895273190534840331/drXa0HJIz1tOyk3Cq0Dz5uv5rSt9Gu2XIYPR2EBo8ojKDkBn84KNWCqWoKdUp0HYi1Vh'
    },
}