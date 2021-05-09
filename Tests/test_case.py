from __test__ import unitTester
from termcolor import cprint

global testCaseCounter

testCases = [
    # """
    # Test Case Set 1:
    # @author: Mayur Manohar Patil
    # """

    ['Adyar', 'No', 'Commercial', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1],
    ['Anna Nagar', 'Yes', 'Commercial', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1],
    ['Chrompet', 'no', 'others', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1],
    ['KK Nagar', 'No', 'Commercial', 'paved', 1000, 2, 3, 4, 5, 5, 7, 1],      # This  test case is wrong and hence it should fail
    ['Karapakkam', 'No', 'house', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1],
    ['T Nagar', 'No', 'Commercial', 'Gravel', 1000, 2, 3, 4, 5, 5, 3, 1],
    ['Velachery', 'YES', 'Commercial', 'Gravel', 2500, 5, 5, 6, 5, 5, 5, 5]


    # """
    # Test Case Set 2:
    # @author: Bhushan Ramkrushna Upasani
    # """








    # """
    # Test Case Set 3:
    # @author: Anup Sanjay Patil
    # """









    # """
    # Test Case Set 4:
    # @author: Janhavi Chaudhari
    # """








    
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
        cprint(f'Test Case {testCaseCounter} Passed', 'green', attrs=['bold'])
        testCaseCounter += 1
    else:
        cprint(f'Test case {testCaseCounter} Failed', 'red', attrs=['bold'])
        testCaseCounter += 1
