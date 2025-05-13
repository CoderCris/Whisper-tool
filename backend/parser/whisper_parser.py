import re
import argparse

def remove_timestamps_and_merge(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Remove Whisper timestamps
    cleaned_text = re.sub(r'\[\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}\.\d{3}\]\s*', '', text)
    
    # Merge lines into a single paragraph
    cleaned_text = ' '.join(cleaned_text.splitlines())
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

def main():
    parser = argparse.ArgumentParser(description='Remove Whisper timestamps and merge text into a single paragraph.')
    parser.add_argument('-i', required=True, help='Path to the input file')
    parser.add_argument('-o', required=True, help='Path to the output file')
        
    args = parser.parse_args()
    
    remove_timestamps_and_merge(args.i, args.o)
    print("Processing complete. Check the output file.")

if __name__ == "__main__":
    main()
