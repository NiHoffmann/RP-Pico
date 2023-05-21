class tape:
    left = ['□']*256
    right = ['□']*256


class tupel:
    alphabet_symbols = ['0','1','□']
    blank_symbols = '□'
    input_symbols = ['0','1']

    #this can be configured
    states = ['Q0','Q1']
    initial_state = 'Q0'
    accepting_states = ['Q1']
                          #value#state#tape#state
    transition_functions = [['0','Q0','>','1','Q0'],
                           ['1','Q0','-','0','Q1']]

class turing_machine:
    tape = tape()
    tupel = tupel()
    programm_counter = 0
    current_state = tupel.initial_state

    def __init__(self, input):
        for i in range(len(input)):
            self.tape.right[i] = input[i]
    
    def apply_transition_function(self):
        pc = self.programm_counter
        tp = self.tape.right
        if self.programm_counter < 0 :
            pc = abs(self.programm_counter)-1
            tape = self.tape.left
            
            
        for transition in self.tupel.transition_functions:
            if transition[0] == tp[pc] and self.current_state == transition[1] :
                tp[pc] = transition[3]
                if transition[2] == '>' :
                    self.programm_counter += 1    
                elif transition[2] == '<' :
                    self.programm_counter -= 1
                self.current_state = transition[4]
                break
            
    def is_accepting(self):
        for i in range(len(self.tupel.accepting_states)):
            if(self.current_state == self.tupel.accepting_states[i]):
                return True
        return False
                

t = turing_machine(['0','0','0','0','1'])
while not t.is_accepting():
    t.apply_transition_function()
