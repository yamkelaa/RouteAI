city_network = {
    # Residential Areas
    "Rosebank": {"Sandton": 12, "Melville": 15, "Shell Rosebank": 5, "Zoo Lake": 8},
    "Sandton": {"Rosebank": 12, "Total Sandton": 4, "Sandton High": 6, "N1@William Nicol": 8, "Sandton City": 3},
    "Soweto": {"Engen Soweto": 3, "Soweto Primary": 5, "Melville": 25, "Hillbrow": 35},
    "Melville": {"Rosebank": 15, "Soweto": 25, "M1@Empire": 7, "Emmarentia Park": 5},
    "Parktown": {"Parktown Hospital": 4, "M1@Empire": 6, "Delta Park": 7},
    "Braamfontein": {"Hillbrow": 4, "Braamfontein Office Park": 2, "M2@Ellis Park": 8},
    "Hillbrow": {"Braamfontein": 4, "Hillbrow Secondary": 3, "BP Hillbrow": 2, "Soweto": 35},

    # Schools
    "Sandton High": {"Sandton": 6},
    "Soweto Primary": {"Soweto": 5},
    "Rosebank College": {"Rosebank": 4},
    "Parktown College": {"Parktown": 3},
    "Hillbrow Secondary": {"Hillbrow": 3},

    # Garages
    "Shell Rosebank": {"Rosebank": 5},
    "Total Sandton": {"Sandton": 4},
    "Engen Soweto": {"Soweto": 3},
    "BP Hillbrow": {"Hillbrow": 2},

    # Intersections / Robots
    "M1@Empire": {"Melville": 7, "Parktown": 6},
    "N1@William Nicol": {"Sandton": 8},
    "M2@Ellis Park": {"Braamfontein": 8, "Park Station": 4},
    "R24@Airport Rd": {"OR Tambo Airport": 2},
    "M1@Sandton": {"Sandton": 5},

    # Parks
    "Zoo Lake": {"Rosebank": 8, "Emmarentia Park": 4},
    "Emmarentia Park": {"Melville": 5, "Zoo Lake": 4, "Delta Park": 3},
    "Delta Park": {"Parktown": 7, "Emmarentia Park": 3},

    # Hospitals
    "Parktown Hospital": {"Parktown": 4, "M1@Empire": 6},
    "Hillbrow Hospital": {"Hillbrow": 2, "BP Hillbrow": 1},
    "Charlotte Maxeke": {"Braamfontein": 6, "Hillbrow": 5},

    # Offices / Commercial
    "Sandton City": {"Sandton": 3},
    "Braamfontein Office Park": {"Braamfontein": 2},

    # Transport hubs
    "Park Station": {"M2@Ellis Park": 4, "OR Tambo Airport": 30},
    "OR Tambo Airport": {"Park Station": 30, "R24@Airport Rd": 2}
}
