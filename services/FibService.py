from typing import List

from injector import inject

from repository.MyDatabase import DatabaseBase


# Fibonacci Service
class FibService:
    @inject
    def __init__(self, db: DatabaseBase):
        print(f"DatabaseBase instance is {db}")
        self.db = db

    # Get all data from Database
    def get_all_data(self):
        return self.db.get_all()

    # Get  data from Database by Fib Value
    def get_data_by_fib(self, fib: int):
        return self.db.get(fib)

    # Save data to Database
    def save_data(self, fib: int, combination: str):
        return self.db.save(fib, combination)

    # Get combination of target sum
    def get_combination_sum(self, target: int) -> List[List[int]]:
        fib_value = self.get_fibonacci_series(target)
        # print(fib_value)
        combination_series = self.unique_combination_series_sum(fib_value, target)
        return combination_series

    # Get Fibonacci series, it's based on requirement that 0 and 1 will not included
    def get_fibonacci_series(self, target: int):
        fib_value = []
        f_0 = 0
        f_1 = 1
        # fib_value.append(f_0)  # We do not need 0 and 1
        # fib_value.append(f_1)  # We do not need 0 and 1
        for i in range(2, target):
            f_n = f_0 + f_1
            fib_value.append(f_n)
            f_0 = f_1
            f_1 = f_n

        if fib_value.__contains__(1):
            fib_value.remove(1)  # We do not need 0 and 1
        return fib_value

    # unique_combination_series_sum, we use backtrack algorithm
    def unique_combination_series_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()

        backtrack(target, [], 0)

        return results
