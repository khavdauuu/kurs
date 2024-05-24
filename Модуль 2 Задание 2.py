def process_string(input_str):
    result_str = input_str.replace("!", "").replace("@", "").replace("#", "").replace("%", "")
    if input_str.startswith("!"):
        return result_str.upper()
    else:
        return result_str.lower()

while True:
    input_str = input()
    if not input_str:
        break
    print(process_string(input_str))