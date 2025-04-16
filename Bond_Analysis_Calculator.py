# The Bond_Analysis_Calculator is a project based on the concept of bond analysis and valuation.
 # This is in relations with my financial analysis class work.

print("\n") # This is used to add a new line for better readability
print("Bond Analysis Calculator") # This is the title of the program


# Step 1: Get the Face (Market) Value and Cash Received
print("""
Bond Issuance Analyzer
        
      \nEnter the bond's Face Value and the Cash Received at issuance 
to determined if the bond was issued at:
        1. Par Value (Equal to Face Value)
        2. Premium Value (Greater than Face Value)
        3. Discount Value (Less than Face Value)
      """)
print("\n")


# Step 2: Get the Face (Market) Value and Cash Received
face_value = float(input("Enter the Face (Market) Value: ")) # float is used to allow decimal values
cash_received = float(input("Enter the Cash Received: ")) # float is used to allow decimal values
print("\n")

print("""
Formula:
      \nPremium or Discount = Face Value - Cash Received
      """) # This is the formula to calculate the premium or discount amount
print("\n")


# Step 3: adding variables for our logic in step 4
premium = 0
discount = 0
par = 0


# Step 4: Calculate face_value - cash_received = premium_or_discount_amount
premium_or_discount_amount = cash_received - face_value # This is the formula to calculate the premium or discount amount
if premium_or_discount_amount > 0: # > This is used to check if the premium_or_discount_amount is greater than 0
    premium = premium_or_discount_amount
    print(f"The bond was issued at Premium Value of ${premium:,.2f}.") # This is used to print the result
    # The :,.2f is used to format the number to 2 decimal places
elif premium_or_discount_amount < 0: # < This is used to check if the premium_or_discount_amount is less than 0
    discount = abs(premium_or_discount_amount)
    print(f"The bond was issued at Discount Value of ${discount:,.2f}.")
else:
    par = face_value # This is used to check if the premium_or_discount_amount is equal to 0
    print(f"The bond was issued at Par Value of ${par:,.2f}.")
print("\n")



    