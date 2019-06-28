# Dictionary
def month():
    month_conversion = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December",
    }

    print(month_conversion["Jan"])
    print(month_conversion.get("Feb"))
    print(month_conversion.get("Tup", "Not in Dictionary"))


month()