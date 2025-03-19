text = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community."""

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary
letter_counts = {}
for letter in text:
    if letter in letter_counts:
       letter_counts[letter] +=1
    else: 
        letter_counts[letter] =1
print(letter_counts)

