province_dict = {
    1: "Alberta",
    2: "BritishColumbia",
    3: "Manitoba",
    6: "NovaScotia",
    7: "Ontario",
    10: "Qu\u00e9bec",
    11: "Saskatchewan",
}

city_dict = {
    2: {6: "Vancouver",
        8: "Kelowna",
        20: "Victoria"},
    1: {2: "Calgary",
        3: "Edmonton"
        },
    3: {
        4: "Winnipeg"
    },
    6: {
        4: "Halifax"
    },
    7: {
        1: "Barrie",
        8: "Hamilton",
        18: "Ottawa",
        28: "Toronto"
    },
    10: {
        8: "GreaterMont",
        12: "Quebec"
    },
    11: {
        5: "Regina"
    }
}

# This dictionary is when we pass the id from javascript to python
# we will change the value, the idea is that i could fit with the position in the kijiji web

states_id = {
    0: 1,
    1: 2,
    2: 3,
    3: 6,
    4: 7,
    5: 10,
    6: 11
}

city_id = {
    1: [2, 3],
    2: [6, 8, 20],
    3: [4],
    6: [4],
    7: [1, 8, 18, 28],
    10: [8, 12],
    11: [5]
}

categories = {
    0: 'propertyforsale/',
    1: 'propertyrentals/'
}
