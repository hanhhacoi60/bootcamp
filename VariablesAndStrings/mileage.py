print("Welcome to the Mileage Converter!")

def mileage_converter():
	miles = input("How many miles did you drive today? ")
	def convert_to_km(miles):
			kilometers = float(miles)/1.60934
			kilometers = round(kilometers, 1)
			print(f"Your {miles}mi drive was approximately {kilometers}km.")
			def repeat():
				print("Would you like to try again? Please write 'yes' or 'no'")
				answer = input()
				while answer == "yes":
					mileage_converter()
				while answer == "no":
					print("Thank you for trying my first Python program. Have a nice day!")
					exit()
				while answer != "yes" or "no":
					print("Sorry, please write 'yes' or 'no' exactly. My Python skills are not that great yet!")
					repeat()
			repeat()

	def mileage_int(miles):
		try:
			miles = int(miles)
			return True
		except:
			return False
	while mileage_int(miles) == True:
		convert_to_km(miles)
	while mileage_int(miles) == False:
		def mileage_float(miles):
			try:
				miles = float(miles)
				return True
			except:
				return False
		while mileage_float(miles) == True:
			convert_to_km(miles)
		while mileage_float(miles) == False:
			print("Please enter a valid number with digits only.")
			mileage_converter()
mileage_converter()






