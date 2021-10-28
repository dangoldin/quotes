import random

def load_quotes(fn):
    with open('quotes.txt', 'r') as f:
        quotes = []
        quote_lines = f.readlines()
        quote = by = ''
        for quote_line in quote_lines:
            if quote_line.startswith('-'):
                by = quote_line.strip('-\n ')
                quotes.append((quote, by))
            elif quote_line == '':
                quote = by = ''
            else:
                quote = quote_line.strip('-\n ')
    return quotes

if __name__ == '__main__':
    quotes = load_quotes('quotes.txt')
    print(random.choice(quotes))
