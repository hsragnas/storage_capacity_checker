def main():
    print("Enter TB or GB for the advertised unit:")
    while True:
        unit = input('>').strip().upper()
        if unit == "TB":
            discrepancy = 1000000000000 / 1099511627776
            break
        elif unit == "GB":
            discrepancy =  1000000000 / 1073741824
            break
        else:
            print("Invalid input. Please enter either TB or GB")    
            
    print("Enter the advertised capacity (e.g. 1): ")
        
    while True:
        try:
            advertised_capacity = float(input(">"))
            break
        except ValueError:
            print("Please enter a valid number for capacity.")
        
    real_capacity = round(advertised_capacity * discrepancy, 2)
    print(f"The actual capacity is {real_capacity} {unit}")
main()
