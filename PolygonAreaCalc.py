class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> int:
        self.width = width
        return self.width

    def set_height(self, height: int) -> int:
        self.height = height
        return self.height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        #shape width is double the width just to account for the formatting in connsoles which makes it look more accurately sized. The height is not doubled because it is already represented accurately in the console.
        shape_width = self.width * 2
        if shape_width > 50 or self.height > 50:
            return "Too big for picture."

        left_padding = (50 - shape_width) // 2
        right_padding = 50 - shape_width - left_padding
        top_padding = (50 - self.height) // 2
        bottom_padding = 50 - self.height - top_padding

        picture = ""
        for i in range(top_padding):
            picture += " " * 50 + "\n"
        for i in range(self.height):
            picture += " " * left_padding + "#" * shape_width + " " * right_padding + "\n"
        for i in range(bottom_padding):
            picture += " " * 50 + "\n"

        return picture

    def get_amount_inside(self, shape) -> int:
        if self.width < shape.width or self.height < shape.height:
            return 0
        return (self.width // shape.width) * (self.height // shape.height)


    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side: int) -> None:
        super().__init__(side, side)
        self.width = side
        self.height = side
        self.side = side

    def set_width(self, width: int) -> int:
        self.width = width
        self.height = width
        self.side = width
        return self.side

    def set_height(self, height: int) -> int:
        self.height = height
        self.height = height
        self.side = height
        return self.side

    def set_side(self, side: int) -> int:
        self.width = side
        self.height = side
        self.side = side
        return self.side

    def __str__(self) -> str:
        return f"Square(side={self.side})"

rectangle1 = Rectangle(10, 5)
rectangle1.set_width(20)
rectangle1.set_height(27)
print(rectangle1.get_area())
print(rectangle1.get_perimeter())
print(rectangle1.get_diagonal())
print(rectangle1.get_picture())

square1 = Square(16)
print(square1.get_area())
print(rectangle1.get_amount_inside(square1))
print(square1.get_picture())


#     def get_picture(self) -> str:
 #        if self.width > 50 or self.height > 50:
  #           return "Too big for picture."
   #      picture = ""
    #     for i in range(self.height):
     #        picture += "*" * self.width + "\n"
      #   return picture