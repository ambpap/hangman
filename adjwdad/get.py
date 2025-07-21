def main():
    with open('filtered_words.txt', 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]

    formatted = '{ ' + ', '.join(f'"{word}"' for word in words) + ' }'
    print(formatted)

if __name__ == "__main__":
    main()
