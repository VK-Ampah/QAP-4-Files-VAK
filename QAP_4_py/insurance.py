
# Program Description: This program calculates new insurance policeis for One Stop Insurance Company
# Author: Valentine Ampah
# Date: 2023-07-26

from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
from tqdm import tqdm

# Read default values from OSICDef.dat
with open('OSICDef.dat', 'r') as file:
    NEXT_POLICY_NUMBER = int(file.readline())
    BASIC_PREMIUM = float(file.readline())
    DISCOUNT_FOR_ADDITIONAL_CARS = float(file.readline())
    COST_OF_EXTRA_LIABILITY_COVERAGE = float(file.readline())
    COST_OF_GLASS_COVERAGE = float(file.readline())
    COST_FOR_LOANER_CAR_COVERAGE = float(file.readline())
    HST_RATE = float(file.readline())
    MONTHLY_PROCESSING_PAYMENTS = float(file.readline())

# Getting and validating user inputs
while True:
    # Valid provinces
    valid_provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']

    # Valid payment methods
    valid_payment_methods = ['Full', 'Monthly']

    # Get user inputs
    first_name = input("Enter first name: ").title()
    last_name = input("Enter last name: ").title()
    address = input("Enter address: ")
    city = input("Enter city: ").title()
    province = input("Enter province (e.g., AB): ").upper()
    while province not in valid_provinces:
        print("Invalid province. Please enter a valid province: eg :", valid_provinces[:3])
        province = input("Enter province (e.g., AB): ").upper()

    postal_code = input("Enter postal code: e.g., A1B 3B6 ")
    phone_number = input("Enter phone number: e.g., 709-234-345 ")

    num_cars_insured = int(input("Enter the number of cars being insured: "))

    extra_liability = input("Enter Y for Yes or N for No for extra liability up to $1,000,000: ").upper()
    while extra_liability not in ['Y', 'N']:
        print("Invalid input. Please enter Y for Yes or N for No.")
        extra_liability = input("Enter Y for Yes or N for No for extra liability up to $1,000,000: ").upper()

    optional_glass_coverage = input("Enter Y for Yes or N for No for optional glass coverage: ").upper()
    while optional_glass_coverage not in ['Y', 'N']:
        print("Invalid input. Please enter Y for Yes or N for No.")
        optional_glass_coverage = input("Enter Y for Yes or N for No for optional glass coverage: ").upper()

    optional_loaner_car = input("Enter Y for Yes or N for No for optional loaner car: ").upper()
    while optional_loaner_car not in ['Y', 'N']:
        print("Invalid input. Please enter Y for Yes or N for No.")
        optional_loaner_car = input("Enter Y for Yes or N for No for optional loaner car: ").upper()

    payment_method = input("Enter payment method (Full or Monthly): ").title()
    while payment_method not in valid_payment_methods:
        print("Invalid payment method. Please enter a valid payment method from the list:", valid_payment_methods)
        payment_method = input("Enter payment method (Full or Monthly): ").title()



    #Creating functions to perform calculations
    def calculate_insurance_premium(num_cars, extra_liability, glass_coverage, loaner_car):
        # Calculate basic premium
        total_premium = BASIC_PREMIUM

        # Calculate discount for additional cars
        if num_cars > 1:
            total_premium += (num_cars - 1) * (BASIC_PREMIUM * DISCOUNT_FOR_ADDITIONAL_CARS)

        # Calculate extra costs
        extra_costs = 0
        if extra_liability == 'Y':
            extra_costs += num_cars * COST_OF_EXTRA_LIABILITY_COVERAGE
        if glass_coverage == 'Y':
            extra_costs += num_cars * COST_OF_GLASS_COVERAGE
        if loaner_car == 'Y':
            extra_costs += num_cars * COST_FOR_LOANER_CAR_COVERAGE

        # Calculate total insurance premium
        total_premium += extra_costs

        return total_premium

    def calculate_total_cost(total_premium):
        # Calculate HST
        hst = total_premium * HST_RATE

        # Calculate total cost
        total_cost = total_premium + hst

        return total_cost

    def calculate_monthly_payment(total_cost):
        # Calculate monthly payment
        monthly_payment = (total_cost + MONTHLY_PROCESSING_PAYMENTS) / 8

        return monthly_payment


    # Calculate total insurance premium
    total_premium = calculate_insurance_premium(num_cars_insured, extra_liability, optional_glass_coverage, optional_loaner_car)
    # Calculate total cost
    total_cost = calculate_total_cost(total_premium)
    # Calculate monthly payment
    monthly_payment = calculate_monthly_payment(total_cost)
    # Get current date
    current_date = datetime.now()
    # Calculate the first day of the next month
    next_payment_date = current_date.replace(day=1)
    next_payment_date += relativedelta(months=1)
    
    # Format dates
    current_date = datetime.strftime(current_date.date(), "%Y-%m-%d")
    next_payment_date = datetime.strftime(next_payment_date.date(), "%Y-%m-%d")


    # Create policy details string
    policy_details = f"{NEXT_POLICY_NUMBER}, {current_date}, {first_name}, {last_name}, {address}, {city}, {province}," \
                    f"{postal_code}, {phone_number}, {num_cars_insured}, {extra_liability}, {optional_glass_coverage}," \
                    f"{optional_loaner_car}, {payment_method}, {total_premium:.2f}\n"

    # Display receipt

    print("\nCustomer Details:")
    print('====================================================')
    print()
    print(f"First Name:                             {first_name}")
    print(f"Last Name:                              {last_name}")
    print(f"Address:                                {address}")
    print(f"City:                                   {city}")
    print(f"Province:                               {province}")
    print(f"Postal Code:                            {postal_code}")
    print(f"Phone Number:                           {phone_number}")
    print(f"Number of Cars Insured:                 {num_cars_insured}")
    if extra_liability == 'Y':
        print(f"Extra Liability:                        YES")
    else:
        print(f"Extra Liability:                        NO")
    if optional_glass_coverage == 'Y':
        print(f"Optional Glass Coverage:                YES")
    else:
        print(f"Optional Glass Coverage:                NO")
    if optional_loaner_car == 'Y':
        print(f"Optional Loaner Car:                    YES")
    else:
        print(f"Optional Loaner Car:                    NO")
    print(f"Payment Method:                         {payment_method}")
    print(f"Total Insurance Premium:                ${total_premium:.2f}")
    print(f"Total Cost (Including HST):             ${total_cost:.2f}")
    if payment_method == valid_payment_methods[0]:
        print(f"Full Payment Due:                       ${total_cost:.2f}")
    else:
        print(f"Monthly Payment:                        ${monthly_payment:.2f}")
    print(f"current Date:                           {current_date}")
    print(f"Next Payment Date:                      {next_payment_date}")
    print()
    print('====================================================')
    print()
    # ADD PROGRESS BAR
    print("\nSaving Policy information - please wait ...")
    print()
    # Processing bar
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)

    # Save policy details to file    
    with open('Policies.dat', 'a') as file:
        file.write(policy_details)
    print("\nPolicy information processed and saved...")
    time.sleep(1)

    # Update next policy number in defaults file
    print()
    print('Writing Default values to file')
    NEXT_POLICY_NUMBER += 1
    with open('OSICDef.dat', 'w') as file:
        file.write(f"{NEXT_POLICY_NUMBER}\n")
        file.write(f"{BASIC_PREMIUM}\n")
        file.write(f"{DISCOUNT_FOR_ADDITIONAL_CARS}\n")
        file.write(f"{COST_OF_EXTRA_LIABILITY_COVERAGE}\n")
        file.write(f"{COST_OF_GLASS_COVERAGE}\n")
        file.write(f"{COST_FOR_LOANER_CAR_COVERAGE}\n")
        file.write(f"{HST_RATE}\n")
        file.write(f"{MONTHLY_PROCESSING_PAYMENTS}\n")    
    print()
    print(f' ***** Default values successfully written to {file.name}  *****')
    
    # option to continue program
    Continue_options = ['Y','N']
    cont = input('Do you want to continue to enter another policy? Enter Y for yes and N for No' ).upper()
    if cont == Continue_options[1]:
        break
    
