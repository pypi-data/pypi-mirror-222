def days_habil():
    habil = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return habil


def holidays_pe(year=None):
    # https://publicholidays.pe/2020-dates/
    holidays = ""
    if year == 2025:
        holidays = [f"{year}-01-01",
                    f"{year}-04-17",
                    f"{year}-04-18",
                    f"{year}-05-01",
                    f"{year}-06-29",
                    f"{year}-07-28",
                    f"{year}-07-29",
                    f"{year}-08-30",
                    f"{year}-10-08",
                    f"{year}-11-01",
                    f"{year}-12-08",
                    f"{year}-12-09",
                    f"{year}-12-25"
                    ]
    elif year == 2024:
        holidays = [f"{year}-01-01",
                    f"{year}-03-28",
                    f"{year}-03-29",
                    f"{year}-05-01",
                    f"{year}-06-29",
                    f"{year}-07-28",
                    f"{year}-07-29",
                    f"{year}-08-30",
                    f"{year}-10-08",
                    f"{year}-11-01",
                    f"{year}-12-08",
                    f"{year}-12-09",
                    f"{year}-12-25"
                    ]
    elif year == 2023:
        holidays = [f"{year}-01-01",
                    f"{year}-04-06",
                    f"{year}-04-07",
                    f"{year}-04-09",
                    f"{year}-05-01",
                    f"{year}-06-29",
                    f"{year}-07-28",
                    f"{year}-07-29",
                    f"{year}-08-30",
                    f"{year}-10-08",
                    f"{year}-11-01",
                    f"{year}-12-08",
                    f"{year}-12-09",
                    f"{year}-12-25"
                    ]
    elif year == 2022:
        holidays = [f"{year}-01-01",
                    f"{year}-04-14",
                    f"{year}-04-15",
                    f"{year}-05-01",
                    f"{year}-06-29",
                    f"{year}-07-28",
                    f"{year}-07-29",
                    f"{year}-08-30",
                    f"{year}-10-08",
                    f"{year}-11-01",
                    f"{year}-12-08",
                    f"{year}-12-09",
                    f"{year}-12-25"
                    ]
    elif year == 2021:
        holidays = [f"{year}-01-01",
                    f"{year}-04-01",
                    f"{year}-04-02",
                    f"{year}-05-01",
                    f"{year}-06-29",
                    f"{year}-07-28",
                    f"{year}-07-29",
                    f"{year}-08-30",
                    f"{year}-10-08",
                    f"{year}-11-01",
                    f"{year}-12-08",
                    f"{year}-12-09",
                    f"{year}-12-25"
                    ]
    elif year == 2020:
        holidays = [f"{year}-01-01",
                    f"{year}-04-09",
                    f"{year}-04-10",
                    f"{year}-05-01",
                    f"{year}-06-29",
                    f"{year}-07-28",
                    f"{year}-07-29",
                    f"{year}-08-30",
                    f"{year}-10-08",
                    f"{year}-11-01",
                    f"{year}-12-08",
                    f"{year}-12-09",
                    f"{year}-12-25"
                    ]
    return holidays
