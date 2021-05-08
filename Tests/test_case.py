from __test__ import unitTester
from termcolor import cprint

global testCaseCounter

testCases = [
    ['Anna Nagar', 'No', 'Commercial', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1],
    ['Anna Nagar', 'No', 'Commercial', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1],
    ['Anna Nagar', 'No', 'Commercial', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1],
    ['Anna Nagar', 'No', 'Commercial', 'Gravel', 1000, 2, 3, 4, 5, 5, 7, 1],
    ['Anna Nagar', 'No', 'Commercial', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1],
    ['Anna Nagar', 'No', 'Commercial', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1],
    ['Anna Nagar', 'No', 'Commercial', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1]
]

testCaseCounter = 1

for testCase in testCases:

    location = testCase[0]
    parking = testCase[1]
    houseType = testCase[2]
    streetType = testCase[3]
    INT_SQFT = testCase[4]
    N_BEDROOM = testCase[5]
    N_BATHROOM = testCase[6]
    N_ROOM = testCase[7]
    QS_ROOMS = testCase[8]
    QS_BATHROOM = testCase[9]
    QS_BEDROOM = testCase[10]
    QS_OVERALL = testCase[11]


    if(unitTester(location, parking, houseType, streetType, INT_SQFT, N_BEDROOM, N_BATHROOM, N_ROOM, QS_ROOMS, QS_BATHROOM, QS_BEDROOM, QS_OVERALL)):
        cprint(f'Test Case {testCaseCounter} Passes', 'green', attrs=['bold'])
        testCaseCounter += 1
    else:
        cprint(f'Test case {testCaseCounter} Failed', 'red', attrs=['bold'])
        testCaseCounter += 1
