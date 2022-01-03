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
        'до 300к': 'https://discord.com/api/webhooks/927573147182575667/SwhY2kU8rxvfMKmW-mxM-nvBBsKAEIBLFMwmKNy2B01xgnCIjdvehbIJ3hCuJu0FLw9a',
        '300-700': 'https://discord.com/api/webhooks/927573240774283334/cXgMhzagQNA2ji81di8xX2xNCMKet42wza0LPO6-v_hwuV9lZwl1b7Fec_eHWLH-G6PR',
        '700-1,5млн': 'https://discord.com/api/webhooks/927573333627764786/ApBw0d8qV_m60WrQ3wqNwDnNrTfcyZL9yx1E8LRu7AOV-cnnPt5JTmNDLzULSEpRCEfH',
        '1,5млн>': 'https://discord.com/api/webhooks/907966697858822185/m9ov8irDr3B7L6e5t-PKOTy97AMiPJHColAToqbgu9_SyXDYGMN9GNTJSIVcja7LJouL'
    },
    'Казань': {
        'до 300к': 'https://discord.com/api/webhooks/907966756344201257/VX2GkSAuNLAHDZpYYcGffQL5s0izfuqIYTqs9FXd_iXmpFNfkWV_jQm5KPgHysRYpLPR',
        '300-700': 'https://discord.com/api/webhooks/907966833464844368/XvERNDehsFW7f1e_iDhpP4NzYENxPJnkw2HKiLxuTR3z1czTB4EeJflAVLn8N14UDFbN',
        '700-1,5млн': 'https://discord.com/api/webhooks/907966907112644608/Xv_lSJ0TEI2JC7-TmsKr5Jkz8tB3hJASQpMG2KkltOHLlM4q-R_DnBYKqyQyBnXyCrsT',
        '1,5млн>': 'https://discord.com/api/webhooks/907966981590896661/BzcXUTOcWmJrsXpzmjmsgeB4-6Ryoj0puB9dwmAl2HWfHYtZRSgMvZytW_zTLdUQexY2'
    },
}