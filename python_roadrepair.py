"""A number of points along the highway are in need of repair. An
equal number of crews are available, stationed at various points
along the highway. They must move along the highway to reach an
assigned point. Given that one crew must be assigned to each job,
what is the minimum total amount of distance traveled by all crews
before they can begin work?
For example, given crews at points {1 ,3,5} and required repairs at
{3,5,7}, one possible minimum assignment would be {19 3, 3-4 5, 5
-4 7} for a total of 6 units traveled.
Function Description
Complete the function getMinCost in the editor below. The function
should return the minimum possible total distance traveled as an
integer.
getMinCost has the following parameter(s):
: a vector of integers
: a vector of integers
Constraints
• 1 < n <10-5
• crewldlij: 1 crewld[ijs 109
• jobldlij: 1 Sjobld[ijs 109 """

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY crew_id
#  2. INTEGER_ARRAY job_id
#

def getMinCost(crew_id, job_id):
    sum=0
    crew_id.sort()
    job_id.sort()
    for i in range(len(crew_id)):
        if crew_id[i]<job_id[i]:
            sum+=job_id[i]-crew_id[i]
        else:
            sum+=crew_id[i]-job_id[i]
    return sum           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crew_id_count = int(input().strip())

    crew_id = []

    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(crew_id, job_id)

    fptr.write(str(result) + '\n')

    fptr.close()
