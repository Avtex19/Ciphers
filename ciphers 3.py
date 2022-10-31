# ----------------------Index Sub Cipher----------------------
def encryptIndexSubstitutionCipher(text):
    output = ''
    nums = {'a': '01 ', 'b': '02 ', 'c': '03 ', 'd': '04 ', 'e': '05 ', 'f': '06 ', 'g': '07 ', 'h': '08 ', 'i': '09 ',
            'j': '10 ', 'k': '11 ', 'l': '12 ', 'm': '13 ', 'n': '14 ', 'o': '15 ', 'p': '16 ', 'q': '17 ', 'r': '18 ',
            's': '19 ', 't': '20 ', 'u': '21 ', 'v': '22 ', 'w': '23 ', 'x': '24 ', 'y': '25 ', 'z': '26 '}
    for i in text:
        output += str(nums.get(i))
    return output






# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}


def encryptMorseCode(text):
    output = ''
    for i in text:
        output += str(morseCode.get(i) + ' ')
    return output.rstrip()


def decryptMorseCode(text):
    output = ''
    changed = dict([(v, k) for k, v in morseCode.items()])
    text = text.split(' ')
    for x in text:
        output += changed.get(x)
    return output


# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    output = ''
    for i in text:
        k = ord(i) - ord('a')
        k = (a * k + b) % 26
        k = chr(k + ord('a'))
        output += k
    return output


def decryptAffineCipher(text, a, b):
    output = ''
    for i in text:
        k = ord(i) - ord('a')
        k = (pow(a, -1, 26) * (k - b)) % 26
        k = chr(k + ord('a'))
        output += k
    return output


# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    output = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    arr = list(text)

    for i in range(len(arr)):
        if i % 2 == 0:
            key = key1
        else:
            key = key2
        if arr[i].isalpha():
            if arr[i].isupper():
                array = uppercase
            else:
                array = lowercase
            index = array.index(arr[i])
            encrypting = (index + key) % 26
            newL = array[encrypting]
        else:
            if arr[i].isnumeric():
                index = digits.index(arr[i])
                encrypting = (index + key) % 10
                newL = digits[encrypting]
            else:
                newL = arr[i]
        output.append(newL)
    sentence = ''
    for i in output:
        sentence += i
    return sentence


def decryptCaesarCipher(text, key1, key2):
    output = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    safe = list(text)

    for i in range(len(safe)):
        if i % 2 == 0:
            key = key1
        else:
            key = key2
        if safe[i].isalpha():
            if safe[i].isupper():
                array = uppercase
            else:
                array = lowercase
            index = array.index(safe[i])
            encrypting = (index - key) % 26
            newL = array[encrypting]
        else:
            if safe[i].isnumeric():
                index = digits.index(safe[i])
                encrypting = (index - key) % 10
                newL = digits[encrypting]
            else:
                newL = safe[i]
        output.append(newL)
    sentence = ''
    for i in output:
        sentence += i
    return sentence


# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    arr = list(text)
    output = ''
    safe = []
    for i in range(0, key):
        for j in range(i, len(text), key):
            safe.append(arr[j])
    for k in safe:
        output += k
    return output




