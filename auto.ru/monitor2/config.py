PARAMS = {
    'МСК': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [213],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [213],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [213],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "used",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [213],
            'top_days': "1"
        }
    },
    'Ростов-на-дону': {
        'до 300к': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_to': 300000,
            'geo_id': [39],
            'top_days': "1"
        },
        '300-700': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 300000,
            'price_to': 700000,
            'geo_id': [39],
            'top_days': "1"
        },
        '700-1,5млн': {
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 700000,
            'price_to': 1500000,
            'geo_id': [39],
            'top_days': "1"
        },
        '1,5млн>': {
            'section': "used",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [39],
            'top_days': "1",
        }
    },
}

WEBHOOK_URLS = {
    'МСК': {
        'до 300к': 'https://discord.com/api/webhooks/927571326833676308/lrPGNhjWv-Hh-B4ij5GuOXhTMo14X4hQt_UXCPMGDQ1IbXICEqxWxdONLB-ti5NtayHj',
        '300-700': 'https://discord.com/api/webhooks/927571450259439676/mGqjm7JGzshfG3peiGPhEYnoo0_Yyn_EAny_YO-ceAhdM1FxRAdkP0HbtxusV5y2BtlD',
        '700-1,5млн': 'https://discord.com/api/webhooks/908295403726831647/3WGHVQ5B518eDpBADl92COypCP0nJiJd56OtWLGS_jQz41Ihb4DiVPNftn9O7fPXEawb',
        '1,5млн>': 'https://discord.com/api/webhooks/927571649522466836/AGsmcYxZHK_c9SRKiPcgP_kV9O9orFDBBDBjx5nC_rCJ7ZtCSSnAEgO3Ip9RcIUBKbXf'
    },
    'Ростов-на-дону': {
        'до 300к': 'https://discord.com/api/webhooks/907327712799121449/ahnwgjQwwbpy8XeK4j36Q8LGxiIY-lL8GqWG6b0VfXXt36mpEEk63WQSfoQscDvvbHJC',
        '300-700': 'https://discord.com/api/webhooks/907327844772900874/awS1DISLXH6FiHI3kg6q1FieNcgZApIHM-XyMYoCneiLOVkE-LiErWzxgjLR4m2epOoS',
        '700-1,5млн': 'https://discord.com/api/webhooks/907327966298660905/s6JzdnDwpZtqgYnA2hH-yRgSuPJFVGiWoxNyGeyneOIB_RyN5GSZ4Pij7didW9CjoLTZ',
        '1,5млн>': 'https://discord.com/api/webhooks/907328074843054081/ce72Zg-vPvfv997IKwQxwi0sH6ujU7FaPzFl6aLaAz5ceriMbPsZKfPYkfm6XMYGxfoX'
    },
}