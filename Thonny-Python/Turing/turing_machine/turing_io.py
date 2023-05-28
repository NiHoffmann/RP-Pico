import json
from turing_machine import tupel
   
class file_reader:
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

class turing_io_converter:
    def intToBinaryTape(value, length):
        tape = ['0']*length
        i = length - 1
        
        while i >= 0 :
            if (value & 1) == 1 :
                tape[i] = '1'
            else :
                tape[i] = '0'
            value >>= 1
            i -= 1
        return tape

    def binaryTapeToInt(tape):
        value = 0
        for idx,cell in enumerate(tape):
            if cell == '1':
               value += 2**(len(tape)-(idx+1))
        return value
