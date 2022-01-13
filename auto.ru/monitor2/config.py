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
        'до 300к': 'https://discord.com/api/webhooks/930335347370516520/kY2wCvlJZ27Qc08nqUn7je5LKGGj1nKpIr8N_zE80DER0dFES19tiK2FSkLbMk3FoKY9',
        '300-700': 'https://discord.com/api/webhooks/930335426462511105/Y8dsZy4t89FSeZeE7swWM9ERC2bA2Bocj2cq3M7Cz6UBfOuoZiDjnvwiMMyHadV2Pp7Y',
        '700-1,5млн': 'https://discord.com/api/webhooks/930335469005316127/yhhOXdOSBFjGVs9y7tpP6kMolxFMLzSSnVYVf9PC9x231pkYiLQo1eiV6zmZ_vPspRTe',
        '1,5млн>': 'https://discord.com/api/webhooks/930335527553617980/72YFjWIHQ5cL0UdcENW6jXJ2CYGK2vcuI1kck_x8xGh9dqT4TX6cmh1gciFh9KLQFzXK'
    },
    'Ростов-на-дону': {
        'до 300к': 'https://discord.com/api/webhooks/907327712799121449/ahnwgjQwwbpy8XeK4j36Q8LGxiIY-lL8GqWG6b0VfXXt36mpEEk63WQSfoQscDvvbHJC',
        '300-700': 'https://discord.com/api/webhooks/907327844772900874/awS1DISLXH6FiHI3kg6q1FieNcgZApIHM-XyMYoCneiLOVkE-LiErWzxgjLR4m2epOoS',
        '700-1,5млн': 'https://discord.com/api/webhooks/907327966298660905/s6JzdnDwpZtqgYnA2hH-yRgSuPJFVGiWoxNyGeyneOIB_RyN5GSZ4Pij7didW9CjoLTZ',
        '1,5млн>': 'https://discord.com/api/webhooks/907328074843054081/ce72Zg-vPvfv997IKwQxwi0sH6ujU7FaPzFl6aLaAz5ceriMbPsZKfPYkfm6XMYGxfoX'
    },
}