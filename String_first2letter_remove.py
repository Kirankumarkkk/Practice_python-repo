
field_value = "PR12345"

remaining_value = ""

if field_value.startswith("PR"):
    remaining_value = field_value[2:]

print("Original value: " + field_value)
print("Remaining value: " + remaining_value)

#================

# Import the necessary classes
#from psdi.mbo import MboConstants

# Get the field value (example field name: 'YOUR_FIELD_NAME')
field_value = "RR 1234"

# Extract the first few characters (e.g., first 2 characters)
num_characters = 2
extracted_value = field_value[:num_characters]

# Store the extracted value in a variable
comparison_value = extracted_value

print(field_value)
print(extracted_value)
print(comparison_value)



# Get another field value to compare (example field name: 'OTHER_FIELD_NAME')
#----other_field_value = mbo.getString("OTHER_FIELD_NAME")

# Compare the extracted value with the other field value
''''''

'''
if comparison_value == other_field_value:
    # Perform actions if the values match
    print("The extracted value matches the other field value.")
else:
    # Perform actions if the values do not match
    print("The extracted value does not match the other field value.")
'''

