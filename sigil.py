class Sigil:
    def __init__(self, text):
        if not text:
            raise ValueError("Please write something!")
        self.text = text

    def __str__(self):
        return f"{self.text}"


def main():
    sigil = get_text()
    print(sigil)





def get_text():
    text = input("Express your Desire: ")
    return Sigil(text)
    
    

if __name__ == "__main__":
    main()

