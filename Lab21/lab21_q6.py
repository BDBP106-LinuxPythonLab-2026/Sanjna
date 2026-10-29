# outer function takes the number of glucose and oxygen molecules
# inner function to calculate ATP yield


def cell_metabolism(glucose,oxygen):
    def energy_output():
        usable_glucose = min(glucose, oxygen//6)
        return 38 * usable_glucose
    return energy_output()


total = cell_metabolism(int(input("Enter number of glucose molecules: ")), int(input("Enter number of oxygen molecules: ")))
print(f"The ATP yield is {total} molecules")