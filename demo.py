from dirty_json import dj

# Example usage
# dirty_json_string = '{"key": 1, "key": 2, \'key\': [1, 2, 3]}'
dirty_json_string = '''[5, .5, 'single quotes', "quotes in "quotes" in quotes"]'''
parsed_data = dj.parse(dirty_json_string, {"duplicateKeys": True})
print(parsed_data)
