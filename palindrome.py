def is_palindrome(text):
    """
    Returns True if text is a palindrome, or False otherwise.

    Takes any text as an argument. Removes all symbols except letters, and leads text to lowercase before check.

    Example of palindromes:
        "Rotor"
        "Racecar"
        "Radar"
        "Red rum, sir, is murder"
        "Eva, can I see bees in a cave?"
        "No lemon, no melon"
    """
    clear_text = ''.join([symbol for symbol in text if symbol.isalpha()])
    clear_text = clear_text.lower()

    return clear_text == clear_text[::-1]


if __name__ == '__main__':
    assert(is_palindrome('А роза упала на лапу Азора') == True)
    assert(is_palindrome('Я иду с мечем, судия!') == True)
    assert(is_palindrome('') == True)
    assert(is_palindrome('A') == True)
    assert(is_palindrome('123') == True)
    assert(is_palindrome('Муза! Ранясь шилом опыта, ты помолишься на разум') == True)
    assert(is_palindrome('AsDf.,mm/.,m/..,#$(@#*&$Fd SA') == True)
    assert(is_palindrome('AsdfdsE') == False)

    text = input('Enter text to check if it is a palindrome:')
    if is_palindrome(text):
        print('Yes! This is a palindrome.')
    else:
        print('No. It is not a palindrome.')