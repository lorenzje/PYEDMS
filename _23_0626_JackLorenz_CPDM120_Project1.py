
#******************************************************* 
#Assignment: Project 1 
#Name: Jack Lorenz
#Semester: SU23                                          
#Class: CPDM120
#*******************************************************


#|-------------------------------------------------------------------------------|
#| table of contents                                                             | 
#|-------------------------------------------------------------------------------|

# 1.0.0 Project 1 Function Area                        2.0.0 Project 1 Main
#------------------------------                       ---------------------
# 1.1.0 Display Instructions                           2.1.0 Declare Variables
#                                                      2.1.1 Declare Inputs
# 1.2.1 Validate Integer                               2.1.2 Declare Outputs (Employee)       
# 1.2.2 Validate Float                                 2.1.3 Declare Outputs (Summary
# 1.2.3 Validate Boolean                               2.1.4 Declare Validators
                                
# 1.3.1 Determine Discount Bonus                       2.2.0 Get/Validate Inputs
# 1.3.2 Calculate Discount Percentage                  2.2.1 Get/Validate Employee Type
# 1.3.3 Calculate YTD Discount                         2.2.2 Get/Validate Years Employed
# 1.3.4 Calculate Discount                             2.2.3 Get/Validate YTD Total
# 1.3.5 Calculate Employee Total                       2.2.4 Get/Validate Today's Purchase Amount

# 1.4.0 New Employee                                   2.3.0 Discount Calculations
#                                                      2.3.1 Determine Employee Discount                    
# 1.5.1 Display Results                                2.3.2 Discount This Purchase
# 1.5.2 Display Summary                                2.3.3 Total With Discount
#                                                     
#                                                      2.4.0 Display Outputs (Employee)
#                                                      2.4.1 Add to Daily Totals
#
#                                                      2.5.0 Loop for new Employee
#                                                      2.6.0 Display Global Outputs



#                                                                       [1.0.0]
#|-----------------------------------------------------------------------------------------|
#|     PROJECT 1 FUNCTION AREA |  PROJECT 1 FUNCTION AREA |  PROJECT 1 FUNCTION AREA       | 
#|-----------------------------------------------------------------------------------------|


# Function Name:      DisplayIntructions                                   [1.1.0]
# Function Purpose:   Instructions on what the program accomplishes
# --------------------------------------------------------------------------------

def DisplayInstructions():
    print("Project 1 : Calculate Employee Discounts")
    print("CINCISTATE_CPDM120")
    print("Calculates employee discounts based on number of years worked, employee status, with a cap of $200 ")
    print("--------------------------------------------------------------------------------------------- ")
    print("")
    
    return




# Function Name:      ValidateInteger                                      [1.2.1]
# Function Purpose:   Instructions on what the program accomplishes
# --------------------------------------------------------------------------------

def ValidateInteger(intInteger):
   try:
        intInteger = int(intInteger)
        if(intInteger >= 0):
            global strValidated
            strValidated = True
        else:
            print("Input Must Be 0 or More")
   except ValueError:
        intInteger = int(0)
        print("Input Must be Numeric")
        
   return intInteger




# Function Name:      ValidateFloat                                        [1.2.2]
# Function Purpose:   Instructions on what the program accomplishes
# --------------------------------------------------------------------------------

def ValidateFloat(dblFloat):
   try:
        dblFloat = float(dblFloat)
        if(dblFloat >= 0):
            global strValidated
            strValidated = True
        else:
            print("Input Must Be 0 or More")
   except ValueError:
        dblFloat = int(0)
        print("Input Must be Numeric")
   return dblFloat




# Function Name:      ValidateBoolean [YES vs NO]                          [1.2.3]
# Function Purpose:   Validates a string input for 'YES' or 'NO' 
# --------------------------------------------------------------------------------

def ValidateBoolean(strBool):

   if(strBool == 'YES') or (strBool == 'NO'):
      global strValidated
      strValidated = True
   else:
      print("Response must be 'YES' or 'NO'")
      print("")
   return strBool




# Function Name:      DetermineDiscountBonus                               [1.3.1]
# Function Purpose:   
# --------------------------------------------------------------------------------

def DetermineDiscountBonus(strEmployeeType):

    dblDiscountBonus = int(0)
    
    if (strEmployeeType == "YES"):
        
        dblDiscountBonus = 10
    else:
        dblDiscountBonus = 0
    return dblDiscountBonus




# Function Name:     CalculateDiscountPercent                              [1.3.2]
# Function Purpose:   
# --------------------------------------------------------------------------------
dblDiscount=float(0)
def CalculateDiscountPercent(YearsWorked, DiscountBonus):

    if YearsWorked > 15:
        dblDiscount= 30 + DiscountBonus
    else:
        if YearsWorked > 10:
            dblDiscount = 25 + DiscountBonus
        else:
            if YearsWorked > 6:
                dblDiscount = 20 + DiscountBonus
            else:
                if YearsWorked > 3:
                    dblDiscount = 14 + DiscountBonus
                else:
                    dblDiscount = 10 + DiscountBonus
    return dblDiscount




# Function Name:     CalculateYTDiscount                                   [1.3.3]
# Function Purpose:   
# --------------------------------------------------------------------------------

def CalculateYTDiscount(DiscountPercent, YTDTotal):
    dblYTDDiscount = float(0)
    dblYTDDiscount = YTDTotal * (DiscountPercent/100)
    if dblYTDDiscount > 200:
        dblYTDDiscount = 200
    return dblYTDDiscount




# Function Name:     CalculateDiscount                                     [1.3.4]
# Function Purpose:   
# --------------------------------------------------------------------------------

def CalculateDiscount(Purchase, DiscountPercent, YTD):
    # Declare Local Variables
    dblDiscountCap = float(200)
    dblRemainder = float(0)
    
    #Calculate Discount
    dblRemainder = 200 - YTD
    if YTD >= 200:
        dblEmployeeDiscount = 0
    else:
        dblEmployeeDiscount = dblTodayPurchase * (dblDiscountPercent/100)       
        if YTD + dblEmployeeDiscount > dblRemainder:
            dbldblEmployeeDiscount = dblRemainder

    return dblEmployeeDiscount




# Function Name:        CalculateEmployeeTotal                             [1.3.5]
# Function Purpose:   
# --------------------------------------------------------------------------------

def CalculateEmployeeTotal(dblPurchasetotal, dblDiscount):
    dblEmployeeTotal = dblPurchasetotal - dblDiscount
    return dblEmployeeTotal




# Function Name:        NewEmployee                                        [1.4.0]
# Function Purpose:   
# --------------------------------------------------------------------------------

def NewEmployee(strEmployee):
    if (strNewEmployee == "YES"):
        global strRepeat 
        strRepeat= bool(True)
    else:
        strRepeat = bool(False)

    return 




# Function Name:      DisplayResults                                       [1.5.1]
# Function Purpose:   Displays the results (whoda thunk?)
# --------------------------------------------------------------------------------

def DisplayResults(DiscountPercent, YTD, PurchaseTotal, EmployeeDiscount, Total):
    print("-------------------------------------------------------------------")
    print("Employee Discount Percentage         : {:.2f}%".format(DiscountPercent))
    print("YTD Amount of discount in dollars    : ${:.2f}".format(YTD))
    print("Total purchase today before discount : ${:.2f}".format(PurchaseTotal))
    print("Employee discount this purchase      : ${:.2f}".format(EmployeeDiscount))
    print("Total with discount                  : ${:.2f}".format(Total))
    print("")
    print("-------------------------------------------------------------------")
    return




# Function Name:      DisplaySummary                                       [1.5.2]
# Function Purpose:   Displays the results (whoda thunk?)
# --------------------------------------------------------------------------------

def DisplaySummary(Subtotal, Total):
    print("-------------------------------------------------------------------")
    print("Daily Total Before Discount          : ${:.2f}".format(Subtotal))
    print("Daily Total After Discount           : ${:.2f}".format(Total))
    print("")
    print("-------------------------------------------------------------------")

    return




#                                                                       [2.0.0]
#|-------------------------------------------------------------------------------------------|
#|           ~PROJECT 1 MAIN AREA |  PROJECT 1 MAIN AREA |  PROJECT 1 MAIN AREA~             | 
#|-------------------------------------------------------------------------------------------|
DisplayInstructions()

                                                                      
# Define Variables                                                          [2.1.0]
#------------------
#Inputs                                                                          [2.1.1]   
strEmployeeType = str("")
intYearsWorked = int(0)
dblYTDTotal = float(0)
dblTodayPurchase = float(0)

#Outputs (Employee)                                                              [2.1.2]
dblDiscountBonus=int(0)  
dblDiscountPercent = float(0)
dblYTDiscount = float(0)
dblEmployeeDiscount = float(0)
dblEmployeeTotal = float(0)

#Outputs (Summary)                                                               [2.1.3] 
dblDailySubtotal= float(0)
dblDailyTotal=float(0)

#Validators                                                                      [2.1.4] 
strValidated = bool(False)
strRepeat = bool(True)
strNewEmployee = str("")



# Get/Validate Inputs                                                      [2.2.0]
#------------------
while strRepeat is True:


    # Get and Validate Employee Type (strEmployeeType)                           [2.2.1] 
    while strValidated is False:
        strEmployeeType = input(" Is the Employee a manager? (YES or NO) : ")
        strEmployeeType = ValidateBoolean(strEmployeeType)

    strValidated = bool(False)
    print("")


    # Get and Validate Years Employed (intYearsWorked)                           [2.2.2] 
    while strValidated is False:
        intYearsWorked = input(" Enter the # of Years Employed : ")
        intYearsWorked = ValidateInteger(intYearsWorked)

    strValidated = bool(False)
    print("")


    # Get and Validate YTD Total (dblYTDTotal)                                   [2.2.3] 
    while strValidated is False:
        dblYTDTotal = input(" Enter Employee's YTD purchase total : ")
        dblYTDTotal = ValidateFloat(dblYTDTotal)

    strValidated = bool(False)
    print("")


    # Get and Validate Today's Purchase (dblTodaysPurchase)                      [2.2.4] 
    while strValidated is False:
        dblTodayPurchase = input(" Enter Total for Today's Purchase : ")
        dblTodayPurchase = ValidateFloat(dblTodayPurchase)

    strValidated = bool(False)
    print("")



    # Discount Calculations                                                 [2.3.0]
    #----------------------
    #Determine Employee Discount                                                 [2.3.1]
    dblDiscountBonus = DetermineDiscountBonus(strEmployeeType)
    dblDiscountPercent=CalculateDiscountPercent(intYearsWorked, dblDiscountBonus)
    dblYTDiscount = CalculateYTDiscount(dblDiscountPercent, dblYTDTotal)
    
    #Discount this purchase                                                      [2.3.3]
    dblEmployeeDiscount=CalculateDiscount(dblTodayPurchase, dblDiscountPercent, dblYTDiscount)

    #Total With Discount                                                         [2.3.4]
    dblEmployeeTotal = CalculateEmployeeTotal(dblTodayPurchase, dblEmployeeDiscount)



    # Display Outputs (Employee)                                           [2.4.0]
    #---------------------------
    DisplayResults(dblDiscountPercent, dblYTDiscount, dblTodayPurchase, dblEmployeeDiscount, dblEmployeeTotal)



    # Add to Daily Totals                                                  [2.4.1]
    #--------------------
    dblDailySubtotal = dblDailySubtotal + dblTodayPurchase
    dblDailyTotal = dblDailyTotal + dblEmployeeTotal



    # Loop for new Employee                                                [2.5.0]
    #----------------------                                                
    while strValidated is False:
        strNewEmployee = input(" Would you like to enter another employee? : ")
        strNewEmployee = ValidateBoolean(strNewEmployee)

    strValidated = bool(False)
    NewEmployee(strNewEmployee)



# Display Outputs (Global)                                                 [2.6.0]
#---------------------------

DisplaySummary(dblDailySubtotal, dblDailyTotal)