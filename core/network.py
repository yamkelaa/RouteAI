city_network = {
    # Main hubs (central nodes with many connections)
    "Rosebank": {"Sandton": 12, "Melville": 15, "Zoo Lake": 10, "Shell Rosebank": 3, "Parktown": 8, "M1@Empire": 7},
    "Sandton": {"Rosebank": 12, "Midrand": 20, "Sandton City": 5, "Total Sandton": 3, "N1@William Nicol": 8, "Sandton High": 4, "Randburg": 15},
    "Braamfontein": {"Melville": 10, "Hillbrow": 5, "Parktown": 6, "Charlotte Maxeke": 6, "Braamfontein Offices": 2, "M1@Empire": 6, "M2@Ellis Park": 5, "Park Station": 4},
    
    # Secondary hubs
    "Soweto": {"Dobsonville": 8, "Orlando": 7, "Southgate": 15, "Engen Soweto": 3, "M1@Southgate": 10},
    "Melville": {"Rosebank": 15, "Emmarentia": 5, "Braamfontein": 10, "Zoo Lake": 8},
    "Parktown": {"Braamfontein": 6, "M1@Empire": 4, "Parktown Hospital": 3, "Parktown College": 4, "Rosebank": 8, "Hillbrow": 7},
    "Hillbrow": {"Braamfontein": 5, "Hillbrow Hospital": 2, "Hillbrow Secondary": 3, "BP Hillbrow": 2, "Parktown": 7, "M2@Ellis Park": 4},
    
    # Intersections / Roads (connecting different areas)
    "M1@Empire": {"Braamfontein": 6, "Parktown": 4, "Rosebank": 7, "N1@William Nicol": 12},
    "N1@William Nicol": {"Sandton": 8, "Randburg": 10, "M1@Empire": 12, "R24@Airport Rd": 18},
    "M2@Ellis Park": {"Braamfontein": 5, "Park Station": 4, "Hillbrow": 4, "OR Tambo": 22},
    "R24@Airport Rd": {"OR Tambo": 6, "Bedfordview": 8, "N1@William Nicol": 18, "Midrand": 15},
    "M1@Southgate": {"Southgate": 4, "Soweto": 12, "Emmarentia": 14, "Delta Park": 16},

    # Parks (natural clusters)
    "Zoo Lake": {"Rosebank": 10, "Emmarentia": 6, "Melville": 8},
    "Emmarentia": {"Melville": 5, "Zoo Lake": 6, "Delta Park": 7, "M1@Southgate": 14},
    "Delta Park": {"Emmarentia": 7, "Randburg": 8, "M1@Southgate": 16, "Sandton": 12},

    # Schools (connected to their suburbs and transport)
    "Sandton High": {"Sandton": 4, "Sandton City": 3},
    "Orlando High": {"Orlando": 3, "Soweto": 5},
    "Parktown College": {"Parktown": 4, "Braamfontein": 5},
    "Hillbrow Secondary": {"Hillbrow": 3, "M2@Ellis Park": 4},

    # Hospitals (connected to suburbs and transport)
    "Parktown Hospital": {"Parktown": 3, "M1@Empire": 5},
    "Hillbrow Hospital": {"Hillbrow": 2, "M2@Ellis Park": 3},
    "Charlotte Maxeke": {"Braamfontein": 6, "Park Station": 5},

    # Garages (connected to nearby areas)
    "Shell Rosebank": {"Rosebank": 3, "Zoo Lake": 4},
    "Total Sandton": {"Sandton": 3, "Sandton City": 2},
    "Engen Soweto": {"Soweto": 3, "Orlando": 4},
    "BP Hillbrow": {"Hillbrow": 2, "M2@Ellis Park": 3},

    # Offices (commercial centers)
    "Sandton City": {"Sandton": 5, "Total Sandton": 2, "Sandton High": 3, "N1@William Nicol": 6},
    "Braamfontein Offices": {"Braamfontein": 2, "Parktown College": 3},

    # Transport hubs (major connection points)
    "Park Station": {"M2@Ellis Park": 4, "OR Tambo": 25, "Braamfontein": 4, "Charlotte Maxeke": 5},
    "OR Tambo": {"Park Station": 25, "R24@Airport Rd": 6, "M2@Ellis Park": 22, "Bedfordview": 10},

    # Other Suburbs (outer nodes with connections to hubs)
    "Midrand": {"Sandton": 20, "R24@Airport Rd": 15, "Randburg": 18},
    "Randburg": {"Delta Park": 8, "N1@William Nicol": 10, "Sandton": 15, "Midrand": 18},
    "Bedfordview": {"R24@Airport Rd": 8, "OR Tambo": 10},
    "Southgate": {"M1@Southgate": 4, "Soweto": 15, "Emmarentia": 12},
    "Orlando": {"Soweto": 7, "Orlando High": 3, "Engen Soweto": 4},
    "Dobsonville": {"Soweto": 8, "M1@Southgate": 9}
}