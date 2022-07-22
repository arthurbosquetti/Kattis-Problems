
alphabet = ['A','B','C','D','E',
            'F','G','H','I','J',
            'K','L','M','N','O',
            'P','R','S','T','U',
            'V','W','X','Y','Z']

dict = {}
for letter in alphabet:
    dict[letter] = "Free"

key_phrase = input().replace(" ","").upper()
plain_text = input().replace(" ","").upper()

table = []
# add letters to table and avoid repetition
for i in range(len(key_phrase)):
    letter = key_phrase[i]
    if dict[letter]=="Free":
        dict[letter] = "Used"
        table += [letter]
# add remaining unused letters in alphabetical order to the table
for tuple in dict.items():
    if tuple[1] == "Free":
        table += tuple[0]

# recursive function that generates the diagraph of a given word
def digraph_generator(word):
    if len(word) == 1:
        return word + "X"
    if word == "":
        return ""
    else:
        if word[0] == word[1]:
            return word[0] + "X" + digraph_generator(word[1:])
        else:
            return word[0] + word[1] + digraph_generator(word[2:])

plain_text = digraph_generator(plain_text)
encrypted_text = ""

def same_row(index1, index2):
    # true whenever letters have an index with the same multiple of 5:
    return (index1)//5 == (index2)//5

def encrypt_same_row(index):
    index += 1
    # wrapping around to the left side of the row
    if index%5== 0:
        index -= 5
    return index

def same_column(index1, index2):
    # true whenever letters are 5*x elements apart
    return (index2 - index1)%5 == 0

def encrypt_same_column(index):
    index += 5
    # wrapping around to the top side of the column
    return index%25

def encrypt_diff_rows_columns(index1, index2):
    row1 = index1//5        
    column1 = index1%5     
    row2 = index2//5     
    column2 = index2%5
    # letter1 is at (row1, column1) -> encrypted1 is at (row1, column2)
    # letter2 is at (row2, column2) -> encrypted2 is at (row2, column1)
    return (row1*5+column2, row2*5+column1)

while plain_text:
    letter1 = plain_text[0]
    letter2 = plain_text[1]
    index1 = table.index(letter1)
    index2 = table.index(letter2)

    if same_row(index1, index2):
        encrypted_text += table[encrypt_same_row(index1)]
        encrypted_text += table[encrypt_same_row(index2)]
    elif same_column(index1, index2):
        encrypted_text += table[encrypt_same_column(index1)]
        encrypted_text += table[encrypt_same_column(index2)]
    else:
        (encrypted1, encrypted_2) = encrypt_diff_rows_columns(index1, index2)
        encrypted_text += table[encrypted1] + table[encrypted_2]

    plain_text = plain_text[2:]

print(encrypted_text)




   
    
    



