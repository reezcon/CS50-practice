months = ["January", "February", "March", "April", "May", "June",
 "July", "August", "September", "October", "November", "December"]

while True:
    date_input = input("Date: ")

    try:
        if "/" in date_input:
            month, day, year = date_input.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <=31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
        elif "," in date_input:
            parts = date_input.replace(",", "").split()
            if len(parts) == 3:
                month_name, day, year = parts
                if month_name in months:
                    month = months.index(month_name) + 1
                    day = int(day)
                    year = int(year)

                    if 1<= day <= 31:
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
    except ValueError:
        pass

    continue

