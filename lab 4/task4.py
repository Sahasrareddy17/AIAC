import csv

def analyze_csv(file_path):
    total_rows = 0
    empty_rows = 0
    word_count = 0

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            # Check if all cells in the row are empty or whitespace
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            # Count words in the row
            for cell in row:
                word_count += len(cell.split())

    print(f"Total rows: {total_rows}")
    print(f"Empty rows: {empty_rows}")
    print(f"Total words: {word_count}")

# Example usage:
# analyze_csv('your_file.csv')