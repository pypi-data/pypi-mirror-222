# import turtle
# from PIL import Image, ImageTk
# import tempfile
# import pkg_resources
#
#
# def love(girlfriendname,text):
#
#
# # Set up the turtle screen
#     screen = turtle.Screen()
#     screen.setup(width=800, height=600)  # Adjust the screen size as desired
#
#     # Load the background image and resize it
#     image_path = pkg_resources.resource_filename(__name__, 'https://ibb.co/qFGBqCS')
#     bg_image = Image.open("https://ibb.co/qFGBqCS")
#     bg_image = bg_image.resize((800, 600))  # Adjust the size to match the screen size
#
#     # Save the resized image as a temporary file
#     temp_filename = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
#     temp_filename.close()
#     bg_image.save(temp_filename.name)
#
#     # Set up the background image
#     screen.bgpic(temp_filename.name)
#     screen.bgcolor("lightpink")  # Changing the background color to light pink
#
#     # Create a turtle instance
#     pen = turtle.Turtle()
#     pen.shape("turtle")
#     pen.color("red")
#     pen.pensize(3)
#     pen.speed(1)  # Adjust the speed to a slower value (1-10)
#
#     # Draw the heart shape
#     pen.penup()
#     pen.goto(0, -200)
#     pen.pendown()
#     pen.color("black")  # Set the fill color for the heart shape
#     pen.left(140)
#     pen.forward(180)
#     pen.circle(-90, 200)
#     pen.color("red")
#     pen.left(120)
#     pen.circle(-90, 200)
#     pen.forward(180)
#     pen.end_fill()
#
#
#     pen.goto(0, -100)  # Position the turtle for writing the name inside the heart
#     pen.color("red")  # Set the text color
#     pen.write(f"{girlfriendname}", align="center", font=("Algerian", 24, "italic"))
#
#     # Change the color of the text
#     pen.color("white")  # Set the new text color
#
#     # Add text: "I love you"
#     pen.goto(0, -180)  # Position the turtle for writing "I love you" inside the heart
#     pen.write(f"{text}", align="center", font=("Lucida Handwriting", 24, "normal"))
#
#     # Hide the turtle and display the result
#     pen.hideturtle()
#     turtle.done()
#
# love("asdasd","Asdasd")
import turtle
from PIL import Image, ImageTk
import requests
import tempfile
import pkg_resources
from io import BytesIO

def love(girlfriendname, text):
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)  # Adjust the screen size as desired

    # Download the background image
    image_url = "https://media.istockphoto.com/id/510082458/vector/young-lover.jpg?s=612x612&w=0&k=20&c=t7vdxyP0dAKc3pI8gtTxUWlsfkQopI88X6z_ihfE7xU="  # Replace this URL with the actual image URL
    response = requests.get(image_url)
    response.raise_for_status()

    # Load the background image
    bg_image = Image.open(BytesIO(response.content))
    bg_image = bg_image.resize((800, 600))  # Adjust the size to match the screen size

    # Save the resized image as a temporary file
    temp_filename = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    temp_filename.close()
    bg_image.save(temp_filename.name)

    # Set up the background image
    screen.bgpic(temp_filename.name)
    screen.bgcolor("lightpink")  # Changing the background color to light pink

    # Create a turtle instance
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color("red")
    pen.pensize(3)
    pen.speed(1)  # Adjust the speed to a slower value (1-10)

    # Draw the heart shape
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    pen.color("black")  # Set the fill color for the heart shape
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.color("red")
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

    pen.goto(0, -100)  # Position the turtle for writing the name inside the heart
    pen.color("red")  # Set the text color
    pen.write(f"{girlfriendname}", align="center", font=("Algerian", 24, "italic"))

    # Change the color of the text
    pen.color("white")  # Set the new text color

    # Add text: "I love you"
    pen.goto(0, -180)  # Position the turtle for writing "I love you" inside the heart
    pen.write(f"{text}", align="center", font=("Lucida Handwriting", 24, "normal"))

    # Hide the turtle and display the result
    pen.hideturtle()
    turtle.done()
