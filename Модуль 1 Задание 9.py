#coding: utf-8
input_string = input().lower()
unique_chars = set(input_string)
sorted_chars = sorted(list(unique_chars))
print(' '.join(sorted_chars))
