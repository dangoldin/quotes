import random

def load_quotes(fn):
    with open(fn, 'r') as f:
        quotes = []
        quote_lines = f.readlines()
        quote = ''
        by = ''
        
        for quote_line in quote_lines:
            if quote_line.startswith('-'):
                by = quote_line.strip('- \n')
                if quote: 
                    quotes.append((quote.strip(), by))
                quote = ''
                by = ''
            # blank line means we're done with this quote
            elif quote_line.strip() == '':
                if quote and by:
                    quotes.append((quote.strip(), by))
                quote = ''
                by = ''
            else:
                quote += quote_line.strip() + ' '
        if quote and by:
            quotes.append((quote.strip(), by))
    
    return quotes

if __name__ == '__main__':
    quotes = load_quotes('quotes.txt')
    if quotes:
        selected_quote, author = random.choice(quotes)
        print(f'" {selected_quote}"')
        print(f'- {author}')
    else:
        print("No quotes found in file")
