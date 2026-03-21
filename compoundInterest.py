principalAmount=float(input("Enter Principal Amount:"))
rateOfInterest=float(input("Enter Rate of Interest (in %):"))
timePeriod=float(input("Enter Time in years:"))

totalAmount=(principalAmount*(1+(rateOfInterest/100))**timePeriod)
compountInterest=totalAmount-principalAmount

print("Total Amount:",round(totalAmount,2))
print("Compund Interest:",round(compountInterest,2))
