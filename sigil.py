import string

class Sigil:
    def __init__(self, text):
        if not text.strip():  # Ensure input is not empty or just whitespace
            raise ValueError("Input text cannot be empty or just whitespace.")
        self.text = text

    @staticmethod
    def remove_vowels(text):
        vowels = "AEIOU"
        return ''.join([char for char in text if char not in vowels])

    @staticmethod
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def remove_repeated_letters(text):
        seen = set()
        result = []
        for char in text:
            if char not in seen and char.strip():  # Ignore spaces
                result.append(char)
                seen.add(char)
        return ''.join(result)

    @staticmethod
    def space_letters(text):
        return ' '.join(list(text))

    def process_text(self):
        normalized_text = self.text.upper()  # Convert to uppercase
        no_punctuation = self.remove_punctuation(normalized_text)
        no_vowels = self.remove_vowels(no_punctuation)
        no_repeats = self.remove_repeated_letters(no_vowels)
        spaced_text = self.space_letters(no_repeats)
        return spaced_text


def main():
    try:
        user_input = input("Enter a sentence or paragraph: ")
        sigil = Sigil(user_input)
        result = sigil.process_text()
        print("Processed text:", result)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
