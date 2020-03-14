def generate_diff(first_data, second_data):
    result = []
    for key, value in first_data.items() & second_data.items():
        result.append('  ' + key + ': ' + str(value))
    for key in first_data.keys() & second_data.keys():
        if first_data.get(key) != second_data.get(key):
            result.append('+ ' + key + ': ' + str(second_data.get(key)))
            result.append('- ' + key + ': ' + str(first_data.get(key)))
    for key in first_data.keys() - second_data.keys():
        result.append('- ' + key + ': ' + first_data.get(key))
    for key in second_data.keys() - first_data.keys():
        result.append('+ ' + key + ': ' + str(second_data.get(key)))

    result = '{\n' + '\n'.join(result) + '\n}'
    return result
