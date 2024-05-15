import pandas as pd

# Solution to Problem 1
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if employee["salary"].nunique() < N or N < 1:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    nth = sorted(employee["salary"].unique(), reverse=True)[N - 1]
    return pd.DataFrame({f"getNthHighestSalary({N})": [nth]})

# Solution to Problem 2
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if employee["salary"].nunique() < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    nth = sorted(employee["salary"].unique(), reverse=True)[1]
    return pd.DataFrame({"SecondHighestSalary": [nth]})
