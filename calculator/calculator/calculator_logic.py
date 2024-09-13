"""
The module contains the Calculator class that performs basic arithmetic operations.
"""


class Calculator:
    """
    A Calculator class that performs basic arithmetic operations and can take the nth root of
    a number.
    Operations are performed using a memory value that stores the result of the last operation.
    """

    def __init__(self) -> None:
        """Initializes the calculator with memory set to 0."""
        self.memory: float = 0

    def __str__(self) -> str:
        """Returns a string representation of the current memory value."""
        return f"Result: {self.memory}"

    def add(self, num: float) -> float:
        """
        Adds a number to the memory value.

        Parameters:
        num (float): The number to add to the memory.

        Returns:
        The new memory value after addition.
        """
        self.memory += num
        return self.memory

    def subtract(self, num: float) -> float:
        """
        Subtracts a number from the memory value.

        Parameters:
        num (float): The number to subtract from the memory.

        Returns:
        The new memory value after subtraction.
        """
        self.memory -= num
        return self.memory

    def multiply(self, num: float) -> float:
        """
        Multiplies the memory value by a number.

        Parameters:
        num (float): The number to multiply the memory by.

        Returns:
        The new memory value after multiplication.
        """
        self.memory *= num
        return self.memory

    def divide(self, num: float) -> float:
        """
        Divides the memory value by a number.

        Parameters:
        num (float): The number to divide the memory by.
        Division by zero will raise a ValueError.

        Returns:
        The new memory value after division.

        Raises:
        ValueError: If num is 0.
        """
        if num == 0:
            raise ValueError("Cannot divide by zero.")
        self.memory /= num
        return self.memory

    def nth_root(self, num: float) -> float:
        """
        Takes the nth root of the memory value.

        Parameters:
        num (float): The degree of the root to be taken. Must be greater than 0.

        Returns:
        The new memory value after taking the nth root.

        Raises:
        ValueError: If n is less than or equal to 0.
        """
        if num <= 0:
            raise ValueError("n must be greater than 0.")
        self.memory **= 1 / num
        return self.memory

    def reset_memory(self) -> float:
        """
        Resets the memory value to 0.

        Returns:
        The memory value after reset (which will be 0).
        """
        self.memory = 0
        return self.memory
