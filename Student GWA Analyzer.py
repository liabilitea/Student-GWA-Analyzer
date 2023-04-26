#Initialize two variables as empty and none where we append the values after evaluating each line in the text
highest_gwa = None
highest_student = ""

#Open the txt file as read mode and iterate through each line of txt with for loop
with open("samplerecord.txt", "r") as file:
    for line in file:    
    #Split the each line into two parts, where the first part is the students' name and the second is their GWA
        name, gwa = line.strip().split(" - ")
        gwa = float(gwa)
    # Compare the current GWA value with the highest GWA value
    # If the current GWA is lower than highest_gwa, update highest_gwa and highest_student
    # The lower the value, the higher the GWA

#Display the output