from PIL import Image
# Input and Open Image
MyImage1 =Image.open(input(r"Please ,Your Image : "))

# X and Y at Image 
width ,height = MyImage1.size
print(width ,height)

# cup right helf from Image
left_helf = MyImage1.crop(((0, 0, width // 2, height)))
left_helf.save("left_helf.jfif")
left_helf.show()

# cup right helf from Image
right_helf = MyImage1.crop((width // 2, 0, width, height))
right_helf.save("right_helf.jfif")
right_helf.show()