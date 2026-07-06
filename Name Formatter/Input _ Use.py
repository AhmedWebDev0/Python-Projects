fname =input("what\'s your first name?")
mname =input("what\'s your middle name?")
lname =input("what\'s your last name?")

fname=fname.capitalize().strip()
mname=mname.capitalize().strip()
lname=lname.capitalize().strip()

print(f'Hello {fname} {mname:.1s} {lname} Happy to see you')
