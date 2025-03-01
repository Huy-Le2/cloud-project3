import re
import socket
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return len(words)

def get_most_frequent_words(file_path, top_n=3, handle_contractions=False):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        
        if handle_contractions:
            text = re.sub(r"n't", " not", text)
            text = re.sub(r"'m", " am", text)
            text = re.sub(r"'re", " are", text)
            text = re.sub(r"'s", " is", text)
            text = re.sub(r"'ll", " will", text)
            text = re.sub(r"'ve", " have", text)
            text = re.sub(r"'d", " would", text)
        

        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        

        return word_counts.most_common(top_n)

def get_ip_address():
    try:

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except:
        return "Could not determine IP address"

def main():

    if_file = "/home/data/IF-1.txt"
    song_file = "/home/data/AlwaysRememberUsThisWay-1.txt"
    output_file = "/home/data/output/result.txt"
    

    if_word_count = count_words(if_file)
    song_word_count = count_words(song_file)
    

    total_words = if_word_count + song_word_count
    

    if_top_words = get_most_frequent_words(if_file)
    

    song_top_words = get_most_frequent_words(song_file, handle_contractions=True)
    

    ip_address = get_ip_address()
    

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"Word count in IF-1.txt: {if_word_count}\n")
        file.write(f"Word count in AlwaysRememberUsThisWay-1.txt: {song_word_count}\n")
        file.write(f"Total word count: {total_words}\n\n")
        
        file.write("Top 3 words in IF-1.txt:\n")
        for word, count in if_top_words:
            file.write(f"- {word}: {count}\n")
        
        file.write("\nTop 3 words in AlwaysRememberUsThisWay-1.txt (after handling contractions):\n")
        for word, count in song_top_words:
            file.write(f"- {word}: {count}\n")
        
        file.write(f"\nIP Address: {ip_address}\n")
    

    with open(output_file, 'r', encoding='utf-8') as file:
        print(file.read())

if __name__ == "__main__":
    main()