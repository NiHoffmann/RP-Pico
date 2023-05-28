class tape:
    #place holder this is what a tape could look like
    left = ['□']
    right = ['□']
    
    def __init__(self,blank='□',length=256):
        #modulo makes sure tape is specified length     
        self.left = [blank]*(int (length/2))
        self.right = [blank]*length*((int (length/2))+length%2)

class tupel:
    #Example Tupel for increment turing machine
    alphabet_symbols = ['0','1','□']
    blank_symbol = '□'
    input_symbols = ['0','1']
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
    
    def __init__(self
                 ,alphabet_symbols = ['0','1','□']
                 ,blank_symbol = '□'
                 ,input_symbols = ['0','1']
                 ,states = ['Q0']
                 ,initial_state = 'Q0'
                 ,accepting_states = []
                 ,transition_functions = [[]]
                 ):
        self.alphabet_symbols = alphabet_symbols
        self.blank_symbol = blank_symbol
        self.input_symbols = input_symbols
        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transition_functions = transition_functions    

class turing_machine:
    tape = tape()
    tupel = tupel()
    programm_counter = 0
    current_state = None

    def __init__(self, input=[], tupel=None, length=None):
        if tupel is not None:
            self.tupel = tupel
        if length is not None:
            self.tape = tape(self.tupel.blank_symbol,length)
        #input always beginning of right tape
        if(len(input) <= len(self.tape.right)):
            for i in range(len(input)):
                self.tape.right[i] = input[i]

        self.current_state = self.tupel.initial_state
    
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