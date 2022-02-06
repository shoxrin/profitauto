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
            'section': "used",
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
            'section': "used",
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
        'до 300к': 'https://discord.com/api/webhooks/939795992440614953/1liBotVRH1hVApHuFskakTOyOioJmOlOOSM-rFGhCTBo8VYaYcCc35uw01LqlPyokGp5',
        '300-700': 'https://discord.com/api/webhooks/939796027014271029/xu9W2d-2otY9NQWDxzvj6t6q8xeya3LNaU5gi5uHTCOEYvDelPJnERkM_Y_7n-JRpteO',
        '700-1,5млн': 'https://discord.com/api/webhooks/939796066428137534/JFt7ggxrdQtq5KQb5Lta24nCaYViVwYF14D-AuxoNvA4p5tiOQl47LMc96Ih0dDH_k1I',
        '1,5млн>': 'https://discord.com/api/webhooks/939796214889709588/g5Mo4onIA9PpzpknlqhHI9pSZhsxkxZ_lccFCRYx0gxXZrqGYsJP_kQmMjpspPg0uB9G'
    },
    'Омск': {
        'до 300к': 'https://discord.com/api/webhooks/939796261131939860/3S2lr-fSHRgM4NWm1pkl_qBiEW0DrSaAXrlHmnMzsdaQaYgxJy1LkKGjJceI1n4mDaVg',
        '300-700': 'https://discord.com/api/webhooks/939796305977434122/2nY7O9ES9aufLeKp6MAep1sK_spWIK-v_Qzv8gBmvdAsa9Kqf008-RHudey_n1Y7Y8gQ',
        '700-1,5млн': 'https://discord.com/api/webhooks/939796341335416852/eTzSLouLeWISEbzehasNqVKypGMyP5uj7hsFQT-0Br8EXL6Evnqm5YpMJ50r-C1JLrTD',
        '1,5млн>': 'https://discord.com/api/webhooks/939796375665774622/rc1_Ep926QhPB_7HDevU75Kv6YV_jjKxf0Pq52ZAJPtrLnSACk0WI1OwDAqdNbwPrnZ5'
    },
}