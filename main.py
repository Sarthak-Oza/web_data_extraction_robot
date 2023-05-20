from robotics import Robot

# A list of Scientists
SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

# Create a robot Instance from Robot class
robot = Robot("Quandrinaut")

def introduce_yourself():
    robot.say_hello()

def say_goodbye():
    robot.say_goodbye()

def main():
    introduce_yourself()

    # Get a scientist from the scientists list and perform extrction
    for scientist in SCIENTISTS:
        robot.extract_details(scientist)

    say_goodbye()
    
    
if __name__ == "__main__":
    main()
