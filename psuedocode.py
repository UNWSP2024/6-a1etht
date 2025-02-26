#Programmer: Alethea Lo
#Date: 2/25/25
#Title: Pseudocode for Monthly Tax Rate

#BEGIN OF FUNCTION

    FUNCTION: CalculateSalesTax(totalSales)
        SET COUNTY_TAX_RATE = 0.025  // 2.5%
        SET STATE_TAX_RATE = 0.05   // 5%

        SET countyTax = totalSales * COUNTY_TAX_RATE
        SET stateTax = totalSales * STATE_TAX_RATE
        SET totalTax = countyTax + stateTax

        RETURN countyTax, stateTax, totalTax
    #END OF FUNCTION

    FUNCTION:Main()
        DISPLAY "Enter the total sales for the month: "
        INPUT totalSales

        CALL CalculateSalesTax(totalSales) -> countyTax, stateTax, totalTax

        DISPLAY "Sales Tax Report:"
        DISPLAY "Total Sales: $" + FORMAT(totalSales, 2)
        DISPLAY "County Sales Tax: $" + FORMAT(countyTax, 2)
        DISPLAY "State Sales Tax: $" + FORMAT(stateTax, 2)
        DISPLAY "Total Sales Tax: $" + FORMAT(totalTax, 2)
    #END OF FUNCTION

    CALL Main()
END