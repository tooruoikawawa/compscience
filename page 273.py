#questions
'''
1. real world data can help us by seeing any patterns and trends that will help us develop models.
2. -
3. a benefit of using a decision tree is that it is similiar to a flow chart in which the diagram will show you
   all the outcomes that come from a decision - it is easy to follow and understand.
4. if we use small data sample to develop rules for a model, if we subsequently obtain a data set with more
   attributes and records they can provide information that is not initially obvious from the data set.
'''

#task 1

def playTennis(outlook, humidity, wind):
    if outlook == "Overcast":
        return "Yes"
    elif outlook == "Sunny":
        if humidity == "High":
            return "No"
        else:
            return "Yes"
    else:
        if wind == "Strong":
            return "No"
        else:
            return "Yes"

