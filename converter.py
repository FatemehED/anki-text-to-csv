import csv
txt_path = r"path\to\your\words.txt"
output_path = r"path\to\anki_cards.csv"
with open(txt_path,encoding='utf-8') as txt_file, \
    open(output_path,"w",encoding="utf-8",newline="") as csvfile:
    writer = csv.writer(csvfile)
    for line in txt_file:
        clean_line = line.strip('\n')
        parts = clean_line.split(',',1)
        if len(parts) == 2:
            writer.writerow(parts)
print("file anki_cards.csv created 🎉")       