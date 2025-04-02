# keyboard input translation library (fingering, but may need to be a list of dictionaries for two hands)
kb_lookup_rh = {
    ";" : "5",
    "l" : "4",
    "k" : "3",
    "j" : "2",
    " " : "1"
}

kb_lookup_lh = {
    "a" : 5,
    "s" : 4,
    "d" : 3,
    "f" : 2,
    "b" : 1
}

# function returning lookup FINGERING
def transform_input(input_pattern):
    return [kb_lookup_rh[char] for char in input_pattern if char in kb_lookup_rh]

# accepts user inupt of hand pattern
usr_hand_pattern = list(input("\nHAND PATTERN: "))

# accepts user inupt of and pitches by note name
usr_pitches_rh = list(input("PITCHES (RH): "))
usr_pitches_lh = 'null'

# prints user entries
print(f"\nusr_hand_pattern: { usr_hand_pattern }")
print(f"usr_pitches_rh: { usr_pitches_rh }\n")

# musical metrics
subdivision = '8' # v0.1 = fixed at eigth
meter = (f"{ len(usr_hand_pattern) }/{ subdivision }") 

# check if len of pattern == pitches
if len(usr_hand_pattern) == len(usr_pitches_rh):
    print("LEN CHECK: you're all good")
else:
    print("LEN CHECK: len mismatch")

# call function, store results in new variable
hp_transformed = transform_input(usr_hand_pattern)
print(f"hp_transformed: { hp_transformed }")

# remove duplicates and sort rh for purpose of matching
input_transformed_sorted = sorted(set(hp_transformed))
print(f"input_transformed_sorted: { input_transformed_sorted }")

# pitches_sorted = sorted(usr_pitches_rh)

# align fingers with pitches in new dictionary for purpose of final lookup
hp_pitches_zipped = dict(zip(input_transformed_sorted, usr_pitches_rh))
print(f"zipped: { hp_pitches_zipped }")

final_string = ""

# reference hp_transformed with hp_pitches_zipped
for x in hp_transformed:
    print(f'finger {x} plays { hp_pitches_zipped[x] }')
    final_string += (f'{hp_pitches_zipped[x]}{subdivision}-{x} ')

print(f'final string: {final_string}')
 
# open ly file
with open('./lily.ly', 'r') as file:
    lines = file.readlines()

# replace placeholder variable with finals_string
for i, line in enumerate(lines):
    if '{{VARIABLE}}' in line:
        lines[i] = line.replace('{{VARIABLE}}', final_string)
        break # for one occurance only

# writes file
with open('./test.ly', 'w') as file:
    file.writelines(lines)
print(f'wrote {lines} to test.ly')
