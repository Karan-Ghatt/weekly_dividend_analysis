import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()

# path to file
file_path = r"C:\Users\karan\Documents\testing_file_one.txt"


# Set reading rate of voice
engine.setProperty("rate", 150)

# Open file and read lines
with open(file_path) as f:
    # This creates a list of sentences from file, delineated at new line
    lines = f.readlines()

    # For each string sentence in generates list, removes new line character
    # also reads out each line
    for i in lines:
        i.strip()
        engine.say(i)
        engine.runAndWait()





