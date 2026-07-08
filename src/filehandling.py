try:
    # Open file in write + read mode
    with open("students.txt", "w+") as file:

        # Writing to file
        file.write("Ashmitha\n")
        file.write("John\n")
        file.write("Alice\n")

        # Current pointer position
        print("Pointer after writing:", file.tell())

        # Move pointer to beginning
        file.seek(0)

        # Read entire file
        print("\nFile Content:")
        print(file.read())

        # Move pointer again
        file.seek(0)

        print("Reading line by line:")
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("Error:", e)

finally:
    print("\nFile operation completed.")