m = raw_input("Enter month of birth:")
d = input("Enter date of birth:")

if m.lower()=="january" and (d>=20) and (d<=31):
	print ("Zodiac sign is Aquarius")
elif m.lower()=="january" and (d<=19) and (d>=1):
	print ("Zodiac sign is Capricorn")

elif m.lower()=="february" and (d<=18) and (d>=1):
	print ("Zodiac sign is Aquarius")
elif m.lower()=="february" and (d>=19) and (d<=29):
	print ("Zodiac sign is Pisces")

elif m.lower()=="march" and (d>=1) and (d<=20):
	print ("Zodiac sign is Pisces")
elif m.lower()=="march" and (d>=21) and (d<=31):
	print ("Zodiac sign is Aries")

elif m.lower()=="april" and (d>=1) and (d<=19):
	print ("Zodiac sign is Aries")
elif m.lower()=="april" and (d>=20) and (d<=30):
	print ("Zodiac sign is Taurus")

elif m.lower()=="may" and (d<=20) and (d>=1):
	print ("Zodiac sign is Taurus")
elif m.lower()=="may" and (d>=21) and (d<=31):
	print ("Zodiac sign is Gemini")

elif m.lower()=="june" and (d<=20) and (d>=1):
	print ("Zodiac sign is Gemini")
elif m.lower()=="june" and (d>=21) and (d<=30):
	print ("Zodiac sign is Cancer")

elif m.lower()=="july" and (d<=22) and (d>=1):
	print ("Zodiac sign is Cancer")
elif m.lower()=="july" and (d>=23) and (d<=31):
	print ("Zodiac sign is Leo")

elif m.lower()=="august" and (d<=22) and (d>=1):
	print ("Zodiac sign is Leo")
elif m.lower()=="august" and (d>=23) and (d<=31):
	print ("Zodiac sign is Vigro")

elif m.lower()=="september" and (d<=22) and (d>=1):
	print ("Zodiac sign is Vigro")
elif m.lower()=="september" and (d>=23)and (d<=30):
	print ("Zodiac sign is Libra")

elif m.lower()=="october" and (d<=22) and (d>=1):
	print ("Zodiac sign is Libra")
elif m.lower()=="october" and (d>=23) and (d<=31):
	print ("Zodiac sign is Scorpio")

elif m.lower()=="november" and (d<=21) and (d>=1):
	print ("Zodiac sign is Scorpio")
elif m.lower()=="november" and (d>=22) and (d<=30):
	print ("Zodiac sign is Sagittarius")

elif m.lower()=="december" and (d<=21) and (d>=1):
	print ("Zodiac sign is Sagittarius")
elif m.lower()=="december" and (d>=22) and (d<=31):
	print ("Zodiac sign is Capricorn")
else:
	print("Invalid input")
