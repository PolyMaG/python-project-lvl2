def get_paths(first_file, second_file):
    import os
    import json
    
    
    abspath_to_first_file = os.path.abspath(first_file)
    abspath_to_second_file = os.path.abspath(second_file)
    first_file = json.load(open(abspath_to_first_file))
    second_file = json.load(open(abspath_to_second_file))
    return first_file, second_file
