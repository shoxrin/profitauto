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
        'до 300к': 'https://discord.com/api/webhooks/927572112938528808/sLgAcciaTX3gxjLRoOxUD-z0IdYcN4IoaX1dMngUcG8U6e_BLK_8Hf2MJYRcxXLHLwvj',
        '300-700': 'https://discord.com/api/webhooks/927572223512957019/hFOILPIwCfIjb0beai8W9gFYZxgNPh8m2C10fhozKUf8GNoV2kczK4Di6tOEq1Xp5EpZ',
        '700-1,5млн': 'https://discord.com/api/webhooks/927572357084766218/as_MzaRJjYfadZr_7wEkTxtyJ17JMRvwckArggwVC4xukfRLY-rzgHc71e8t7SlcJXlx',
        '1,5млн>': 'https://discord.com/api/webhooks/907850127849426994/ir1HswUrdvLBI8owEBxPCAjQeVdIJTjd6QPizLUDOSPFeAEjGAAkG5nJqwEj53U_lipQ'
    },
    'Омск': {
        'до 300к': 'https://discord.com/api/webhooks/907850249693966366/1xrRCBq5xFb4tVqG7Avn2UeXORwzGiJIHTPEsLj_FM4t0NEeGu9fs_kLmeQ6jCZSLttV',
        '300-700': 'https://discord.com/api/webhooks/907850327217278977/StlIZvklJL9TZZ2sAIpHIhI9yvDfYNNB782ewBIWeHh0YBVGsVjDqC64N-EZDDl_aPky',
        '700-1,5млн': 'https://discord.com/api/webhooks/907850422100848662/1MNGp0MbncOncTcxfgH_Yd9gC8--n9-REDl3bCr4ML16WaywWmttn8v4NoQrRe6Bq7Ew',
        '1,5млн>': 'https://discord.com/api/webhooks/907850506477666364/AItew1ZNYaAegHSYg-RKXZX-iQevWdrVPQpUVPKZA5KNsQhJSTcdf83D6yZKePx4tEA4'
    },
}