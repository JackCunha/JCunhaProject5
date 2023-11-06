import Project5Start

game_data = Project5Start.get_project5_data()
print("choose from the following menu")
print("1 - find recent games")
print("2 - find total copies")
print("3 - Find average revenue per year")
print("4 - Find the highest average revenue per year")
user_input = int(input("enter your choice: "))
if user_input ==1:
    year_input = int(input("enter a year:"))
    for lines in game_data:
        year = int(lines["release"])
        if year >= year_input:
            print(lines["name"])

if user_input ==2:
    for lines in game_data:
        name = (lines["name"])
        price = (lines["price"])
        total_sales = (lines["total_sales"])
        total_copies_sold = int(total_sales)/int(price)
        print(f"{name} has {total_copies_sold} copies sold")





if user_input ==3:
    for lines in game_data:
        name = (lines["name"])
        release_date = (lines["release"])
        years_released = 2023-release_date
        total_sales = (lines["total_sales"])
        average_revenue = int(total_sales)/int(years_released)
        print(f"{name} has an average revenue of {average_revenue}$ per year")

if user_input ==4:
    for lines in game_data:
        revenue = "average_revenue"
        if revenue > 30000000:
            print(lines["name"])








    



