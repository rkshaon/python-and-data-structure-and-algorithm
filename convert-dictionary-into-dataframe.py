# Input
emp_details = {
    "Employee": {
        "Jessica": {"ID": "001", "Salary": "2000", "Designation": "Team Lead"},
        "Alba": {"ID": "002", "Salary": "1800", "Designation": "Associate Team Lead"},
        "Scarlett": {"ID": "003", "Salary": "1500", "Designation": "Senior Developer"},
        "Johansson": {"ID": "004", "Salary": "1200", "Designation": "Developer"}
    }
}

# Output
#                Jessica                 Alba          Scarlett  Johansson
# ID                 001                  002               003        004
# Salary            2000                 1800              1500       1200
# Designation  Team Lead  Associate Team Lead  Senior Developer  Developer

import pandas as pd

data_frame = pd.DataFrame(emp_details["Employee"])