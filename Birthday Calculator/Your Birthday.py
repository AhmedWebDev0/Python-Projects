import datetime

# print(dir(datetime))

a = input("What's Your Birthday With Years :\t")
h = input("What's Your Birthday With monses :\t")
s = input("What's Your Birthday With Days :\t")

birthday = datetime.datetime(int(a),int(h),int(s))
today = datetime.datetime.now()
difference = today - birthday
print(difference)
