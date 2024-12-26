def main():
  
  text = "books/frankenstein.txt"
  open_text = read_text(text)
  nums_words = num_words(open_text)
  chars_in_text = num_of_char(open_text)
  chars_sorted_list = dict_to_list(chars_in_text)

   

  print(f"--- Begin report of {text} ---")
  print(f"{num_words} words found in the document")
  print()

  for item in chars_sorted_list:
      if not item["char"].isalpha():
          continue
      print(f"The '{item['char']}' character was found {item['num']} times")

  print("--- End report ---")
  
  
  
  


def read_text(text):
  with open(text) as f:
    return f.read()
  
def num_words(num):
  words = num.split()
  return len(words)

def num_of_char(char):
  number_of_chars = {}
  for chars in char:
    lowerd_chars = chars.lower()
    if lowerd_chars in number_of_chars:
      number_of_chars[lowerd_chars] += 1
    else:
      number_of_chars[lowerd_chars] = 1
  return number_of_chars

def sort_on(rep):
  return rep["num"]

def dict_to_list(chars_dict):
  sorted_list = []
  for ch in chars_dict:
    sorted_list.append({"char": ch, "num": chars_dict[ch]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list







main()


