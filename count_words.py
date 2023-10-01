
import sys

def main():

    input_text = ""

    for line in sys.stdin:
        input_text += line.strip() + " "

    word_count = len(input_text.split())

    print(word_count)

if __name__ == '__main__':
    main()
