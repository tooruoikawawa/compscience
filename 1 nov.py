#questions page 46
'''
1. A test case uses a set of conditions or inputs to test a piece of code.
2. The purpose of running code with test cases is to test a range of values or inputs to cover all the possible values that
    could be entered.
3. ID, description, test data, expected result, actual result, pass y/n
4. The difference is that the expected value is the correct value and the actual value is the output of the code.
5. The golden rule is that the expected result mujst never be taken from the output of the code
6. Code coverage is covering every case of the code
7. Equivalence partitions are a techique that partitions the range of conditions/inputs in areas that should have the
    same behaviour
8. Extreme values are really high numbers
9. Testing boundary values involves testing values in the region where partitions meet
10. Error anticipation is knowing that the code will have a bug or wil go wrong
11. There may be a higher number than there should be inputted
12. To prevent bugs
'''

#task 1
'''
ID     Description     Expected Result     Actual Result     Passed?(Y/N)

1      Testing value      Eligible            Eligible           Y
        17 years old         

2      Testing value
        16 years old      Not eligible       Not eligible        Y
        
3      Testing value
        12 years old      Not eligible       Not eligible        Y

4      Testing value
        20 years old      Eligible            Eligible           Y
        
5      Testing input      Error                Error             N
        "seventeen
         years old"


'''
#task 2
'''
ID     Description     Expected Result          Actual Result        Passed?(Y/N)

1      User inputs      "Please insert         "Please insert           Y
         "cash"          cash" is printed      cash" is printed


2      User inputs      "Please insert         "Please insert           Y
         "card"          card" is printed       card" is printed


3      User inputs      "Coupons are only      "Coupons are only        Y
         "coupon"        accepted at customer   accepted at customer
                         services" is printed   services" is printed

4      User inputs          Error                    Error              N
         "cheque"        

'''
#task 3
'''














'''