class tape:
    left = ['□']
    right = ['□']
    
    def __init__(self,blank='□',length=256):
        self.left = [blank]*length
        self.right = [blank]*length

class tupel:
    alphabet_symbols = ['0','1','□']
    blank_symbol = '□'
    input_symbols = ['0','1']

    #this can be configured
    states = ['Q0','Q1','Q2','Q3']
    initial_state = 'Q0'
    accepting_states = ['Q3']
                          #value#state#tape#state
    transition_functions = [['0','Q0','>','0','Q0'],
                           ['1','Q0','>','1','Q0'],
                            ['□','Q0','<','□','Q1'],
                            ['1','Q1','<','0','Q1'],
                            ['0','Q1','-','1','Q2'],
                            ['1','Q2','<','1','Q2'],
                            ['0','Q2','<','0','Q2'],
                            ['□','Q2','>','□','Q3']]

class turing_machine:
    tape = tape()
    tupel = tupel()
    programm_counter = 0
    current_state = tupel.initial_state

    def __init__(self, input):
        for i in range(len(input)):
            self.tape.right[i] = input[i]
    
    def apply_transition_function(self):
        #decide which side of the tape to look at
        pc = self.programm_counter
        tp = self.tape.right
        if self.programm_counter < 0 :
            pc = abs(self.programm_counter)-1
            tp = self.tape.left
            
        #check which transition function to apply
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
        for accepting in self.tupel.accepting_states:
            if(self.current_state == accepting):
                return True
        return False
    
    def get_current_cell(self):
        if self.programm_counter < 0:
            return self.tape.left[abs(self.programm_counter)]
        else:
            return self.tape.right[self.programm_counter]
    
    def get_return_value(self):
        return_value = []
        pc = self.programm_counter
        if self.is_accepting():
            while self.get_current_cell() !=  self.tupel.blank_symbol :
                return_value.append(self.get_current_cell())
                self.programm_counter += 1
            self.programm_counter = pc            
        return return_value
