# List the ages that we need to check.
# Check each cutoff age, and one age above and below each cutoff age.
test_ages = [3, 4, 5, 17, 18, 19, 64, 65, 66]

# Print the price that will be assigned to each age.
for age in test_ages:
    if age < 4:
        price = 0
    elif age < 18:
        price = 5
    elif age < 65:
        price = 10
    elif age >= 65:
        price = 5

    print("Age: " + str(age) + "\t\tPrice: " + str(price))
