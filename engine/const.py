province_dict = {
    "Alberta": "1",
    "British Columbia": "2",
    "Manitoba": "3",
    "Nova Scotia": "6",
    "Ontario": "7",
    "Qu\u00e9bec": "9",
    "Saskatchewan": "10",
}

city_dict = {
    "1": {
        "Calgary": "2",
        "Edmonton Area": "3",
    },
    "2": {
        "Greater Vancouver Area": "6",
        "Kelowna": "8",
        "Victoria": "20",
    },
    "3": {
        "Winnipeg": "4"
    },
    "6": {
        "Halifax": "4",
    },
    "7": {
        "Barrie": "1",
        "Hamilton": "8",
        "Ottawa / Gatineau Area": "18",
        "Toronto (GTA)": "28",
    },
    "9": {
        "Greater Montr\u00e9al": "8",
        "Qu\u00e9bec City": "12",
    },
    "10": {
        "Regina Area": "5",
    }
}

#This dictionary is when we pass the id from javascript to python
#we will change the value, the idea is that i could fit with the position in the kijiji web

states_id = {
    0:1,
    1:2,
    2:3,
    3:6,
    4:7,
    5:10,
    6:11
}

city_id = {
    1:[2,3],
    2:[6,8,20],
    3:[4],
    6:[4],
    7:[1,8,18,28],
    10:[8,12],
    11:[5]
}

states_excel = {
    0:'/Toronto/',
    1:'/Vancouver/',
    2:'/Winnipeg/'
}

categories = {
    0: 'propertyforsale/',
    1: 'propertyrentals/'
}