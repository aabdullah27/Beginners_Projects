import string  # Import string module to handle punctuation removal easily


def take_input():
    text = input('Enter text here: ')
    return text

def word_frequency_counter(text):
    # Convert text to lowercase to make it case-insensitive
    text = text.lower()
    # Remove punctuation using string.punctuation
    text = ''.join(char for char in text if char not in string.punctuation)
    # Split the text into words
    words = text.split()
    # Initialize an empty dictionary to hold word frequencies
    frequency = {}
    # Count the frequency of each word
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def check_frequency():
    text = take_input()  # Take user input
    result = word_frequency_counter(text)  # Get the word frequency dictionary
    print(result)  # Print the result

if __name__ == '__main__':
    check_frequency()
