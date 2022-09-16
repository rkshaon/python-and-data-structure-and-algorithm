# Input
emp_details = {
    "Employee": {
        "Jessica": {"ID": "001", "Salary": "2000", "Designation": "Team Lead"},
        "Alba": {"ID": "002", "Salary": "1800", "Designation": "Associate Team Lead"},
        "Scarlett": {"ID": "003", "Salary": "1500", "Designation": "Senior Developer"},
        "Johansson": {"ID": "004", "Salary": "1200", "Designation": "Developer"}
    }
}

# Output 1
#                Jessica                 Alba          Scarlett  Johansson
# ID                 001                  002               003        004
# Salary            2000                 1800              1500       1200
# Designation  Team Lead  Associate Team Lead  Senior Developer  Developer

# Output 2
#             ID Salary          Designation
# Jessica    001   2000            Team Lead
# Alba       002   1800  Associate Team Lead
# Scarlett   003   1500     Senior Developer
# Johansson  004   1200            Developer

import pandas as pd

data_frame = pd.DataFrame(emp_details["Employee"])

# Output 1
print(data_frame)
# Output 2
print(data_frame.T)