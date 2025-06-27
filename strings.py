''' #type1
number = "9514310972"
encrypted_num = number[:2]+"******"+number[-2:]
print(encrypted_num)
'''

""" #type2
song = "muTha Mazhai"
artist = "Chinmayi"
editted = f"{song.title()} - {artist.title()}"
print(editted)
"""

""" #type3
location = "Chennai"
print(f"Old location - {location}")
changed_loc = location.replace('Chennai', 'Mumbai')
print(f"New location - {changed_loc}")
"""

""" #type4
sentence = "Hello Ganesh. U23456 is your UID"
my_uid = sentence.split(".")[1].split("is")[0].strip()
print(my_uid)
"""

""" #type5
name = "ganesh kumar"
initials = ""
for i in name.split():
    initials += i[0].upper()
print(initials)

name = "ganesh kumar"
initials = "".join([i[0].upper() for i in name.split()])
print(initials)
"""

str = "ganesh kumar"
print(str[::-1])
