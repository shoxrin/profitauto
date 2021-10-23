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
            'section': "all",
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
            'section': "all",
            'category': "cars",
            'sort': "cr_date-desc",
            'price_from': 1500000,
            'geo_id': [10842],
            'top_days': "1"
        }
    },
}

WEBHOOK_URLS = {
    'СПБ': {
        #'до 300к': 'https://discord.com/api/webhooks/900166495085146122/Io8Qg_UsZzKRlee7nyfpRMA3BwOWnYYX3Nw1lubFJGWjN9AiSmQY_54Du8OdybI7sV4x',
        #'300-700': 'https://discord.com/api/webhooks/900704728353214466/NWgixfk3_nd6LSzaUV00K2E4IqckqGCdAeSmyoa013gQIZH7VcIgOyBCQzVzQC4jra8L',
        #'700-1,5млн': 'https://discord.com/api/webhooks/900704641820545054/wcPWP8uAqsTAUvJt_v1jKBV_Z2CfU7hVrbpAClnjkh9WjUN_BQkIaT7ERNx9qLS1ymqL',
        #'1,5млн>': 'https://discord.com/api/webhooks/900704451017469993/KR0VJxQrskaWJsEzRaEp2kYBQSJI5O7LC7R3vfrUkVrkwBcbJUWs0aawksZCI2tjaFIk'
        'до 300к': 'https://discord.com/api/webhooks/895295379522850897/aSXGnNh0R9dPVZ0BgI-M4t2Q021XB3h5iR2W2tfc2NGNm1nmwJFRniQxgJj-Tl2IjdDj',
        '300-700': 'https://discord.com/api/webhooks/895294828257083442/Z7ZfJN_wGTG6ArxioAfbddqKZYYQpdWG_a9eiR3QuVBBjvKSamxf53lcD-Wxbj85sdT5',
        '700-1,5млн': 'https://discord.com/api/webhooks/895294741778956340/c-ff-wHIcYNBO4z1Ouc56kTfTjPEx7wJ-DBXKlu8AyaZPMWzbCmC1ACSVoylbOBaGlK1',
        '1,5млн>': 'https://discord.com/api/webhooks/895294606546202644/b2-T8jGJNPW2KGmoxgG1-rdnkRdNV2IMtNyW_mBgPxtuch13mrG3HbmgUfkSot3pvkEV'
    },
    'Архангельск': {
        'до 300к': 'https://discord.com/api/webhooks/895294523159228448/9zVhPlf2LO4P7b53CqNZCVeTDGZIhes_209QpBDsCLrfOKHV5d-7ECa-UrEY-KgyGSxU',
        '300-700': 'https://discord.com/api/webhooks/895294405957783603/BOgLd3cWdMqy1syD2dxWHMqPa9I-C2-ZtDfELUyY8A3l3UGbKJVWLXzFVaACj0Zszgno',
        '700-1,5млн': 'https://discord.com/api/webhooks/895294168144953375/jncX1o1FFdoyEDXPIzqKXb81jWNrieqiRMyYK6iSFIdhTNjMEo4n4JjOSCVSFew-bxFN',
        '1,5млн>': 'https://discord.com/api/webhooks/895275318527529040/EgL2LmPMAcGfu4cDAyj-t5CUhEn_VYZ3qZQD0IAIKylxmPUsb3JQXYi4CugQfEwaRzsg'
    },
}