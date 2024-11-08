import math
import subprocess
import threading

def play_sound(sound_file):
    subprocess.run(["afplay", sound_file])

def calculate_shape():

    try:
        prompt_sound_thread = threading.Thread(target=play_sound, args=("Choose.mp3",))
        prompt_sound_thread.start()
        shape = input("Choose a shape to calculate (rectangle/circle/triangle): ")

        if shape == 'rectangle':

            sound_thread = threading.Thread(target=play_sound, args=("RL.mp3",))
            sound_thread.start()
            length = float(input("Enter the length of the rectangle: "))

            sound_thread = threading.Thread(target=play_sound, args=("RW.mp3",))
            sound_thread.start()
            width = float(input("Enter the width of the rectangle: "))

            sound_thread = threading.Thread(target=play_sound, args=("AP.mp3",))
            sound_thread.start()
            choice = input("Please enter 'a' for area or 'p' for perimeter:")

            if choice == 'a':
                area = length * width
                print(f"The area of the rectangle is: {area:.3g} square cm")
                play_sound("MAGA.mp3")

            elif choice == 'p':
                perimeter = 2 * (length + width)
                print(f"The perimeter of the rectangle is: {perimeter:.3g} cm")
                play_sound("MAGA.mp3")

            else:
                print("Invalid choice. Please enter 'a' for area or 'p' for perimeter.")
                play_sound("Error.mp3")

        elif shape == 'circle':

            sound_thread = threading.Thread(target=play_sound, args=("radius.mp3",))
            sound_thread.start()
            radius = float(input("Please Enter the radius of the circle: "))

            sound_thread = threading.Thread(target=play_sound, args=("AP.mp3",))
            sound_thread.start()
            choice = input("Please enter 'a' for area or 'p' for perimeter: ")

            if choice == 'a':
                area = math.pi * radius ** 2
                print(f"The area of the circle is: {area:.3g} square cm")
                play_sound("MAGA.mp3")

            elif choice == 'p':
                circumference = 2 * math.pi * radius
                print(f"The circumference of the circle is: {circumference:.3g} cm")
                play_sound("MAGA.mp3")

            else:
                print("Invalid choice. Please enter 'a' for area or 'p' for perimeter.")
                play_sound("Error.mp3")

        elif shape == 'triangle':

            sound_thread = threading.Thread(target=play_sound, args=("AP.mp3",))
            sound_thread.start()
            choice = input("Please enter 'a' for area or 'p' for perimeter:  ")

            if choice == 'a':
                sound_thread = threading.Thread(target=play_sound, args=("TB.mp3",))
                sound_thread.start()
                base = float(input("Enter the base of the triangle: "))

                sound_thread = threading.Thread(target=play_sound, args=("TH.mp3",))
                sound_thread.start()
                height = float(input("Enter the height of the triangle: "))

                area = 0.5 * base * height
                print(f"The area of the triangle is: {area:.3g} square cm")
                play_sound("MAGA.mp3")

            elif choice == 'p':
                sound_thread = threading.Thread(target=play_sound, args=("TFS.mp3",))
                sound_thread.start()
                side1 = float(input("Enter the length of the first side: "))

                sound_thread = threading.Thread(target=play_sound, args=("TSS.mp3",))
                sound_thread.start()
                side2 = float(input("Enter the length of the second side: "))

                sound_thread = threading.Thread(target=play_sound, args=("TTS.mp3",))
                sound_thread.start()
                side3 = float(input("Enter the length of the third side: "))

                perimeter = side1 + side2 + side3
                print(f"The perimeter of the triangle is: {perimeter:.3g} cm")
                play_sound("MAGA.mp3")

            else:
                print("Invalid choice. Please enter 'a' for area or 'p' for perimeter.")
                play_sound("Error.mp3")

        else:
            print("Invalid shape. Please enter 'rectangle', 'circle', or 'triangle'.")
            play_sound("Error.mp3")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        play_sound("Error.mp3")


calculate_shape()