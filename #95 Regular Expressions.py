# what is regular expressions?
import re # use for regular expressions import the re package.
pattern=r"[A-Z]+ext" # It is search ext with first later is capitale later A to Z
text="""
Next:
AsyncIO in Python | Python Tutorial - Day #96

78K views  10 months ago Aext  Python for Beginners (Full Course) | #100Day Cext OfCode Programming Tutorial in Hindi
Access the Playlist:   

 • Python for Beginne Rext rs (Full Course) | ...  
Link to the Repl: https://replit.com/@codewithharry/95-...
Join Replit the browser-based IDE used in this course - https://join.replit.com/code-with-har... …
"""

match=re.search(pattern, text) #re stop on the first mach case and stop
print(match)

matchs=re.finditer(pattern, text)
for match in matchs:
    print(match.span())
    print(type(match.span()))
    print(text[match.span()[0]:match.span()[1]])

