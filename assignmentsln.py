#Reading the file
with open("student_records.txt", "r") as file:
    content = file.read()
    print(content)
# writing a modified version of existing file in a new file
#Step 1: Open the existing file in read mode
with open("student_records.txt", "r") as original_file:
    # Step 2: Read the contents of the file
    cont = original_file.read()
    # Step 3: Modify the content as needed - convert the content to uppercase
    modified_content = cont.upper()
    # Step 4: Open a new file in write mode to save the modified content
    with open("new_file.txt", "w") as new_file:
        # Write the modified content to the new file
        new_file.write(modified_content)
    #Reading the content of the newly created file.
    with open("new_file.txt", "r") as new_file:
        new_content = new_file.read()
        print(new_content)