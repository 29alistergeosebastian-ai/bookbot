# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

# stats.py

## get_num_words

| Input          | process                                                                                      |output                          |
| ---------------| ---------------------------------------------------------------------------------------------|--------------------------------|
| text           |  1.make a dict named chars                                                                   | return len of words in list    |
|                |  2.converts to lower case                                                                    |                                |

## get_chars_dict
| Input          | process                                                                                      | output                         |
| ---------------| -------------------------------------------------------------------------------------------- | ------------------------------ |
| text           |  1. chars(dict) = {}                                                                         |  return chars (dict)           |
|                |  2. loop through text > convert each char to lowercase                                       |                                |
|                |  3. if lowered char in chars > increment count, else set count to 1                          |                                |

## sort_on
| Input          | process                                                                                      | output                         |
| ---------------| ---------------------------------------------------------------------------------------------|--------------------------------|
| char_count     |  1. extract second item in tuple: char_count[1]                                              |return count (int)              |

## chars_dict_to_sorted_list
| Input          | process                                                                                      | output                         |
| -------------- | ---------------------------------------------------------------------------------------------|--------------------------------|
| num_chars_dict |  1. chars_list(list) = []                                                                    | return sorted chars_list       |
|                |  2. loop dict > convert key-value pairs to (char, count) tuples and append to list           |                                |
|                |  3. sort chars_list in descending order using key=sort_on                                    |                                | 

<img width="291" height="887" alt="image" src="https://github.com/user-attachments/assets/7a440512-c476-44f0-938f-ded508978603" />

 
