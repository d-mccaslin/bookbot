def main():
    path = "books/frankenstein.txt"
    text = get_book_contents(path)

    word_count = get_word_count(text)

    characters = get_character_count(text)

    print(f'--- Begin report of {path} ---')
    print(f'{word_count} words found in the document\n')
    
    sorted_characters = sort_dict(characters)
    for c in sorted_characters:
        character = c["character"]
        count = c["num"]
        print(f"The '{character}' character was found {count} times")

    print('--- End report ---')

def get_book_contents(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def get_word_count(text):
    words = text.split()
    word_count = len(words)
    
    return word_count

def get_character_count(text):
    character_count = {}
    text = text.lower()
    
    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict_list = []

    for d in dict:
        if d.isalpha():
            new_dict = {
                "character": d,
                "num": dict[d]
            }
            dict_list.append(new_dict)

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list


if __name__ == '__main__':
    main()