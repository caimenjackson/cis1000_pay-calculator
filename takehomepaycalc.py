####### Take Home Pay Calculator ####### CAIMEN JACKSON, ELLA JACKSON ####### ####### ####### ####### ####### #######

####### Section 1 ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######

def national_insurance_deductions(currentsalary):
    if currentsalary < 9569:
        return 0
    elif currentsalary < 50270:
        newsalary = currentsalary - 9569
        deduction = newsalary * 0.12
    elif currentsalary > 50270 or currentsalary == 50270:
        firstband = currentsalary - 9569
        deductionOne = firstband * 0.12
        secondband = currentsalary - 50269
        deductionTwo = secondband * 0.02
        deduction = deductionOne + deductionTwo
    return deduction

    def studentfinancecalculator(currentincome):
        print ("Please select your payback plan \n 1) Plan 1 \n 2) Plan 2 \n 3) Plan 4 \n 4) Postgraduate Loan ")
        planselection = int(input)
        if planselection == 1:
            print("placeholder")
        elif planselection == 2:
            print("placeholder")
        elif planselection == 3:
            print("placeholder")
        elif planselection == 4:
            print("placeholder")
        else:
            print("Invalid option chosen. Exiting program.")
            exit




def tax_band_one(currentsalary): #runs if income is below 50,000
    if currentsalary > 50000:
        currentsalary = 50000
    else:
        if currentsalary > 12500:
            taxbandone = currentsalary - 12500
            taxbandoneremainder = taxbandone * 0.8
            total_band_one = taxbandoneremainder + 12500
            taxpaid = taxbandone * 0.2
            return total_band_one
        else:
            return currentsalary

def tax_band_two(currentsalary): #runs if income is between 50,000 and 100,000
    if currentsalary > 100000:
        currentsalary = 100000
    else:
        currentsalary = currentsalary
    taxbandtwo = currentsalary - 50000
    taxbandtwocalculation = taxbandtwo * 0.6
    total_band_two = taxbandtwocalculation + tax_band_one(currentsalary)
    taxpaid = taxbandtwo * 0.4
    return total_band_two

#def tax_band_two(currentsalary):
#    if currentsalary > 100000:
#        currentsalary = 100000
 #   else:
#        currentsalary = currentsalary
#        taxbandone = 50000 * 0.8
 #       taxbandone_tax = 50000 * 0.2
#        currentsalary = currentsalary - 12500
 #       taxbandtwo = currentsalary * 0.6 
 #       taxbandtwo_tax = currentsalary * 0.4
#        taxbandtwo_takehomepay = taxbandone + 12500 + taxbandtwo
 #       return taxbandtwo_takehomepay


def tax_band_three(currentsalary): #runs if income is between 100,000 and 150,000 
    difference = currentsalary - 100000
    taxfree_reduction = difference / 2
    taxfree = 12500 - taxfree_reduction
    personal_allowance = 12500 - taxfree_reduction
    fixed_band_one = 50000 * 0.8
    dynamic_band_two = (50000 - personal_allowance) * 0.6
    total_band_three = fixed_band_one + dynamic_band_two + personal_allowance
    return total_band_three

def tax_band_four(currentsalary):
    total_band_four = currentsalary * 0.55
    return total_band_four


####### Section 2 ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######


def takehomecalculator(currentsalary):
    if currentsalary < 50000:
        return(tax_band_one(currentsalary))
    elif currentsalary > 50000 and currentsalary < 100000:
        return(tax_band_two(currentsalary))
    elif currentsalary > 100000 and currentsalary < 150000:
        return(tax_band_three(currentsalary))
    else:
        return(tax_band_four(currentsalary))



def takehomecalculatordompare(salaryA, salaryB):
    if salaryA < 50000: #this runs the indented code if the salary is less than the £50k threshold
        salaryA_result = tax_band_one(salaryA) 
    elif salaryA > 50000 and salaryA < 100000:
        salaryA_result = tax_band_two(salaryA)
    elif salaryA > 100000 and salaryA < 150000:
        salaryA_result=tax_band_three(salaryA) #passes through the starting salary and runs it in the tax badn three function
    else:
        salaryA_result=tax_band_four(salaryA)

    if salaryB < 50000: #this runs the indented code if the salary is less than the £50k threshold
        salaryB_result = tax_band_one(salaryB) #passes through the starting salary and runs it in the tax band one function
    elif salaryB > 50000 and salaryB < 100000: #runs the code if starting salary is in tax band two
        salaryB_result = tax_band_two(salaryB) #passes through the starting salary and runs it in the tax band two function
    elif salaryB > 100000 and salaryB < 150000:
        salaryB_result=tax_band_three(salaryB) #passes through the starting salary and runs it in the tax badn three function
    else:
        salaryB_result=tax_band_four(salaryB)

    return salaryA_result, salaryB_result

####### Section 3 ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######


def runtime(): #defines a main function which will handle the running of all the other functions in the code

    mode = int(input("Please enter run mode \n 1) Standalone take-home pay calculator \n 2) Comparison take-home pay calculator\n"))
    
    if mode == 1: #runs the following indented code if the user inputs the value 1 
        salaryA = int(input("Please enter Salary A: £"))
        nicalc = input("Do you want to calculate national insurance deductions? Y/N") #allows an input asking if they want a national insurance calculation
        if nicalc.upper() == "Y": #runs the following code if the user inputs y or Y
            totaltakehome = takehomecalculator(salaryA) - national_insurance_deductions(salaryA)
            print("Take home pay after tax and NI is £", str(totaltakehome))
        else: #runs the following code without national insurance calculations if the input isn't y or Y
            print("Take-home pay after tax is £" + str(takehomecalculator(salaryA)))
            taxdifference = salaryA - takehomecalculator(salaryA) #works out the difference by taking the final salary away from the starting salary
            print("The total tax deduction is £" + str(taxdifference))


    elif mode == 2: #runs the code if the user inputs a value fo 2
        salaryA = int(input("Please enter Salary A: £")) #allows an integer input for salary a
        salaryB = int(input("Please enter Salary B: £")) #allows an integer input for salary b
        result = takehomecalculatordompare(salaryA, salaryB) #runs the function result and passes through the starting salary inputs
        print("Salary A: " + str(result[0]) + "\nSalary B: " + str(result[1])) #Returns the salary for A and the salary for B to the user
        salarydiff = result[0] - result[1] #subtracting one salary from another and saving it under a new variable
        salarydiff = abs(salarydiff) #this will make the difference variable always positive for the user
        print("Difference in salary: £" + str(salarydiff)) #prints the value of the salary difference variable and tells the user 


    else: #runs the following code if an unexpected input is recieved by the program
        print("Invalid selection made. Program exiting.") #print a warning to the user that there has been an invalid selection made
        exit #exits the program by halting the running of the code
        

####### Section 1 ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######


 
runtime() #this will run the main function when the program is executed to run the actual calculator