# f-string use to formatting the string it is bery big provlem for codes.
# Explian:-
letter="Hey my name is {} and i am from {}."
name="Deepak saini"
country="india"

print(letter.format(name,country)) # format is a string method
print(letter.format(country,name)) # It is wrog. It is solving to use value format

print(f"hey my name is {name} and i am from {country}")
print(f"hey my name is {{name}} and i am from {{country}}")

price=24.454
txt=f"for noly {price: .2f}"
print(txt)
# or
txt="for only {price: .2f} dollars"
print(txt.format(price=49.2255))

print(f"{2*3}")
print(type(f"{2*3}"))