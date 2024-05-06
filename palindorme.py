# programa que recibe un string y determina si es palíndromo

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('ana'))
print(is_palindrome('anita lava la tina'))
print(is_palindrome('hola mundo'))
print(is_palindrome('reconocer'))
