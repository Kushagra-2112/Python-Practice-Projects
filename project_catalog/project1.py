# TITLE: Band Name Generator
# DESCRIPTION: A simple text utility that combines input strings using f-strings to generate creative band name recommendations.
# LIMITATIONS: Lack of Spatial Formatting: The program mashes words together directly without spacing or title capitalization adjustments. | Redundant Inputs: No checks to stop users from entering completely blank spaces or numbers as names.
# CHALLENGE: Modify the string output formatting so that it automatically strips accidental white spaces and capitalizes the first letter of both words cleanly.

print("Band_Name_Generator")
print()
city_name = input("Enter the name of your city where you grew up")
nick_name = input("Enter your nick name")
band_name = city_name+nick_name
print(f"Band name recommended: {band_name}")

