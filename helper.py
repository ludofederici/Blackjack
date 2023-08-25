"""ensures that the user enters only valid inputs"""
def input_integer(prompt, min, max):
	while True:
		response = input(prompt)
		try:
			value = int(response)
		except ValueError:
			print("Not a valid response. Try again.")
			continue
		else:
			if value >= min and value <= max:
				return value
				break
			else:
				print(f"Please enter a value between {min} and {max}")
