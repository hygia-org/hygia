import inflect
import json
import yaml
import re

def convert_to_natural_language(text):
    p = inflect.engine()

    # Convert numbers to words
    def convert_numbers(match):
        number = match.group(0)
        return p.number_to_words(number)

    # Convert currency amounts to words
    def convert_currency(match):
        currency = match.group(0)
        dollars, cents = currency.split('.')
        dollars_words = p.number_to_words(dollars)
        cents_words = p.number_to_words(cents)
        return f"{dollars_words} dollars and {cents_words} cents"

    # Convert time expressions to words
    def convert_time(match):
        time = match.group(0)
        hour, minute = time.split(':')
        hour_words = p.number_to_words(hour)
        minute_words = p.number_to_words(minute)
        return f"{hour_words} {minute_words}"

    # Convert the text
    converted_text = re.sub(r'\d+:\d+|\$\d+\.\d+|\d+', 
                            lambda match: convert_time(match) if ':' in match.group(0)
                            else convert_currency(match) if '$' in match.group(0)
                            else convert_numbers(match),
                            text)

    return converted_text

if __name__ == '__main__':
    # Open the text file in read mode
    with open('./AI/examples/ex.txt', 'r') as file:
        # Read the entire contents of the file
        content_txt = file.read()

    converted_data = convert_to_natural_language(content_txt)
    print("==== TXT ====")
    print(f"original:\n{content_txt}\n")
    print(f"converted:\n{converted_data}\n")

    # Open the text file in read mode
    with open('./AI/examples/ex.json', 'r') as file:
        # Read the entire contents of the file
        content_json = json.load(file)

    converted_data = convert_to_natural_language(json.dumps(content_json))
    print("==== JSON ====")
    print(f"original:\n{content_json}\n")
    print(f"converted:\n{converted_data}\n")

    # Open the text file in read mode
    with open('./AI/examples/ex.yaml', 'r') as file:
        # Read the entire contents of the file
        content_yaml = yaml.safe_load(file)

    converted_data = convert_to_natural_language(json.dumps(content_yaml))
    
    print("==== YAML ====")
    print(f"original:\n{content_yaml}\n")
    print(f"converted:\n{converted_data}\n")