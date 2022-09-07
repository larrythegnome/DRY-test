#DRY - Don't Repeat yourself
def directions():
    print("Turn left out of the parking lot.")
    print("Drive to stop light and turn left.")
    print("Drive one mile therough canfield.")
    print("starbucks is across the street from sheetz")
    print("turn left into starbucks")

number_of_people = int(input("How many people are asking for directions? "))

while number_of_people > 0:
    print(f"{number_of_people} - New Directions")
    directions()
    number_of_people = number_of_people - 1
