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
    if salaryA < 50000:
        salaryA_result = tax_band_one(salaryA)
    elif salaryA > 50000 and salaryA < 100000:
        salaryA_result = tax_band_two(salaryA)
    elif salaryA > 100000 and salaryA < 150000:
        salaryA_result=tax_band_three(salaryA)
    else:
        salaryA_result=tax_band_four(salaryA)

    if salaryB < 50000:
        salaryB_result = tax_band_one(salaryA)
    elif salaryA > 50000 and salaryA < 100000:
        salaryB_result = tax_band_two(salaryA)
    elif salaryA > 100000 and salaryA < 150000:
        salaryB_result=tax_band_three(salaryA)
    else:
        salaryB_result=tax_band_four(salaryA)

    return salaryA_result, salaryB_result

####### Section 3 ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######


def runtime():

    mode = int(input("Please enter run mode \n 1) Standalone take-home pay calculator \n 2) Comparison take-home pay calculator\n"))
    
    if mode == 1:
        salaryA = int(input("Please enter Salary A: £"))
        nicalc = input("Do you want to calculate national insurance deductions? Y/N")
        if nicalc.upper() == "Y":
            print("for now")
        else:
            print("Take-home pay after tax is £" + str(takehomecalculator(salaryA)))
            taxdifference = salaryA - takehomecalculator(salaryA)
            print("The total tax deduction is £" + str(taxdifference))


    if mode == 2:
        salaryA = int(input("Please enter Salary A: £"))
        salaryB = int(input("Please enter Salary B: £"))
        result = takehomecalculatordompare(salaryA, salaryB)
        print("Salary A: " + str(result[0]) + "\nSalary B: " + str(result[1]))
        salarydiff = result[0] - result[1]
        salarydiff = abs(salarydiff)
        print("Difference in salary: £" + str(salarydiff))

        

####### Section 1 ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######


 
runtime()