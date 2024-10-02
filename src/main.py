import os
import random

# Generate a random 16-digit number as a string
random_file_name = f"{random.randint(10**15, 10**16 - 1)}.txt"

# Create the 'data' directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Path to the new file inside the 'data' folder
file_path = os.path.join("data", random_file_name)

# Create the file and write "Hello World" into it
with open(file_path, "w") as f:
    f.write(f"Hello World {random.randint(10**15, 10**16 - 1)}")

# Output the file path for reference
file_path
