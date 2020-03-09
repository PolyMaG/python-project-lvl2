def generate_diff(first_file, second_file):
    result = []
    for k, v in first_file.items() & second_file.items():
        result.append('  ' + k + ': ' + str(v))
    for k in first_file.keys() & second_file.keys():
        if first_file.get(k) != second_file.get(k):
            result.append('+ ' + k + ': ' + str(second_file.get(k)))
            result.append('- ' + k + ': ' + str(first_file.get(k)))
    for k in first_file.keys() - second_file.keys():
        result.append('- ' + k + ': ' + first_file.get(k))
    for k in second_file.keys() - first_file.keys():
        result.append('+ ' + k + ': ' + str(second_file.get(k)))

    result = '{\n' + '\n'.join(result) + '\n}'
    return result
