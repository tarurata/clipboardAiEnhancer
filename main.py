import argparse
from text_generator import generate_natural_english, generate_emoji
from clipboard_handler import read_clipboard, write_clipboard

def main():
    parser = argparse.ArgumentParser(description="Generate natural English or emojis from clipboard text.")
    parser.add_argument('mode', choices=['english', 'emoji'], help="Choose 'english' for natural English or 'emoji' for emoji conversion")
    args = parser.parse_args()

    clipboard_content = read_clipboard()
    
    if args.mode == 'english':
        generated_text = generate_natural_english(clipboard_content)
    elif args.mode == 'emoji':
        generated_text = generate_emoji(clipboard_content)
    else:
        print("Invalid mode. Please choose 'english' or 'emoji'.")
        return

    write_clipboard(generated_text)

if __name__ == "__main__":
    main()