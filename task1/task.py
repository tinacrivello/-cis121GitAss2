# author:
# date:
# purpose: Sales call

# This program contains errors
# find and fix them

# NOTE: all the errors are in one line
# However you are allowed to change that line and add up to
# 3 other lines.  Note that it is possible to correct the
# program just by changing a single line.


# input
def should_call():
    name = ""
    city = ""

    while not name:
        name = input("Please enter your name: ")

    while not city:
        city = input("Please enter your city: ")

    age = 0

    while age <= 0:
        try:
            age = int(input("Please enter your age: "))
        except ValueError:
            print("Please enter age as a whole number")


    # calculations
    is_sales_call = calculate_should_call(city, age)
    # output
    print("Call", name + ":", is_sales_call)

    return is_sales_call


def calculate_should_call(city, age):
    return city == "portland" or "Hillsboro" and age > 21

if __name__ == "__main__":
    should_call()