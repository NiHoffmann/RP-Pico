import json
from turing_machine import tupel
    
def load_data_from_file() :
    with open('../rules', 'r', encoding='utf-8') as file:
        data = json.load(file)
        t = tupel(alphabet_symbols     = data.get("alphabet_symbols"),
                  blank_symbol         = data.get("blank_symbol"),
                  input_symbols        = data.get("input_symbols"),
                  states               = data.get("states"),
                  initial_state        = data.get("initial_state"),
                  accepting_states     = data.get("accepting_states"),
                  transition_functions = data.get("transition_functions")
                  )
        print(data)
        return t
    return None