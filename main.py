"""
A statement is a string of words where each word is separated by a space. Given
a string representing a statement as input, print all the words occurring in the
string.
Input-> "Going to the market"
Output->
Going
to
the
market
"""

st = "Going to the market"
for word in st.split():
  print(word)