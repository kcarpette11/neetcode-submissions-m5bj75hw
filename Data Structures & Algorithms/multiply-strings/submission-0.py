class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = int(num1)
        num2_int = int (num2)

        product = num1_int * num2_int
        prod_str = str(product)

        return prod_str