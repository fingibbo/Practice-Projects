class ReverseString:
    def __init__(self, input_string: str) -> None:
        if not isinstance(input_string, str):
            raise TypeError("Must be a string")
        if not input_string.strip():
            raise ValueError("String is Empty")
        self.input_string = input_string

    @property
    def input_string(self):
        return self._input_string

    @input_string.setter
    def input_string(self, new_string: str):
        if not isinstance(new_string, str):
            raise TypeError("Must be a string")
        if not new_string.strip():
            raise ValueError("String is Empty")
        self._input_string = new_string

    def slice_syntax(self) -> str:
        return self.input_string[::-1]

    def reverse_func(self) -> str:
        reversed_list = reversed(self.input_string)
        new_string = ""
        for char in reversed_list:
            new_string += char
        return new_string

    def my_idea(self) -> str:
        listed_string = []
        reversed_string = ""
        for char in self.input_string:
            listed_string.append(char)
        for char in listed_string:
            reversed_string = char + reversed_string
        return reversed_string

    def __str__(self) -> str:
        return (
            f"Using Slice Syntax: {self.slice_syntax()}\n"
            f"Using the reverse function: {self.reverse_func()}\n"
            f"Using my own original idea: {self.my_idea()}\n"
            )
