def load_main_wordlist(path):
    with open(path, 'r', encoding='utf-8') as f:
        return set(word.strip() for word in f if word.strip().isalpha())

def load_common_words(path, min_freq=1000):
    common = set()
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 2:
                continue
            word, freq = parts[0], parts[1]
            if word.isalpha() and word.islower() and int(freq) >= min_freq:
                common.add(word)
    return common

def filter_words(words, common):
    return [w for w in words if 5 <= len(w) and w in common]

def main():
    words = load_main_wordlist('words_alpha.txt')
    common_words = load_common_words('common_words_10000.txt', min_freq=4000)

    filtered = filter_words(words, common_words)
    print(f"Kept {len(filtered)} words from {len(words)}")

    with open('filtered_words.txt', 'w', encoding='utf-8') as f:
        for word in sorted(filtered):
            f.write(word + '\n')

if __name__ == "__main__":
    main()
