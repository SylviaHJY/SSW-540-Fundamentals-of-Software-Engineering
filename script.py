INSTRUCTION1 = 'Enter first value:'
INSTRUCTION2 = 'Enter Second value:'
INSTRUCTION3 = 'Enter Third value:'
VALID_CHARS = '0123456789abcdefghijklmnopqrst' 
ORD_0 = ord('0')
ORD_9 = ord('9')
ORD_a = ord('a')
ORD_z = ord('z')
ORD_A = ord('A')
ORD_Z = ord('Z')

class MaxOfThree:
    def __init__(self):
        self.values = ' '
        self.max_val = None
        
    def check_invalid_input(self, instruction: str) -> str:
        input_str = input(instruction)
        for ch in input_str:
            valid = False
            ord_ch = ord(ch)
            if valid == False and ord_ch >= ORD_0 and ord_ch <= ORD_9:
                valid = True
            if valid == False and ord_ch >= ORD_a and ord_ch <= ORD_z:
                valid = True
            if valid == False and ord_ch >= ORD_A and ord_ch <= ORD_Z:
                valid = True
            if valid == False:
                raise Exception(f'Input {input_str} is invalid')
        return input_str

    def max_of_three(self) -> None:
        instructions = [INSTRUCTION1, INSTRUCTION2, INSTRUCTION3]
        for instruction in instructions:
            try:
                curr_val = self.check_invalid_input(instruction)
            except Exception as e:
                print(e)
                return
            self.values += curr_val + ' '
            if self.max_val is None or curr_val > self.max_val:
                self.max_val = curr_val
        print(f'The maximum of {self.values} is {self.max_val}')
        
task = MaxOfThree()
task.max_of_three()