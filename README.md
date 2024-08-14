# Clipboard Ai Enhancer

This Python application transforms text from your clipboard using OpenAI's GPT model. It can convert text to natural English or represent it with a single emoji.

## Features

- Convert clipboard text to natural English
- Represent clipboard text with a single emoji
- Easy-to-use command-line interface

## Requirements

- Python 3.6+
- OpenAI API key: It costs money. Get it from [OpenAI](https://platform.openai.com/account/api-keys)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/tarurata/clipboardAiEnhancer.git
   cd clipboardAiEnhancer
   ```

2. Install the required packages:
   ```
   poetry install
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your_api_key_here`

## Usage

Run the script with one of two modes:

1. Natural English mode:
   ```
   python3 main.py english
   ```

2. Emoji mode:
   ```
   python3 main.py emoji
   ```

## Using with Mac Spotlight

You can integrate this tool with Mac Spotlight for quick access. Here's how to set it up using Automator:

1. Open Automator and create a new "Quick Action" workflow.
2. Add a "Run Shell Script" action to the workflow.
3. Set "Workflow receives" to "no input" in "any application".
4. Paste the following script into the shell script box:

   ```bash
   #!/bin/bash

   cd /path/to/ClipboardAiEnhancer

   /path/to/poetry run python3 main.py emoji
   ```

   Note: Adjust the paths according to your system setup.

5. Save the Quick Action with a memorable name (e.g., "Emoji Transform").
6. You can now access this action from Spotlight by typing its name.

This setup allows you to quickly transform your clipboard text to an emoji using the Mac Spotlight, enhancing your workflow efficiency.

The transformed text will be automatically copied to your clipboard.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- OpenAI for providing the GPT model
- Pyperclip for clipboard handling
