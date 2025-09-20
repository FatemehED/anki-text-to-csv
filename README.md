✅ TXT to Anki CSV converter
A simple Python script that converts a plain text (`.txt`) vocabulary file into a CSV file ready for import into [Anki](https://apps.ankiweb.net/).
🤖 Features
- Converts word pairs from a `.txt` file into `anki_cards.csv`
- Input format: `word, translation`
- Output format is fully compatible with Anki
- UTF-8 support (works with English, Russian, Persian, etc.)
📥Input Format
The input text file should contain one word pair per line, separated by a comma:
apple, яблоко
book, книга
house, дом
📤 Output
The script will generate a `anki_cards.csv` file:
You can then import this CSV into Anki and set **Column 1 = Front** and **Column 2 = Back**.
👥Usage
1. Clone this repository or download `converter.py`.
2. Update the paths in the script:
   ```python
   txt_path = r"path\to\your\words.txt"
   output_path = r"path\to\anki_cards.csv"
3. Run the script:
python converter.py
🤝Contributing
Feel free to open issues or pull requests with improvements🩷