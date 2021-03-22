dictionary_1 = {"name": "Jenna", "gender": "female", "age": 23}
string_text = "Hello, my name is {name}. I am a {gender}. I am {age} years old."
string_filled = string_text.format(**dictionary_1)
print(string_filled)

f_string = f"Hello, my name is {dictionary_1['name']}. I am a {dictionary_1['gender']}. I am {dictionary_1['age']} years old."
print(f_string)
