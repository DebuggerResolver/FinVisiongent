from utils.pocketflow import Node

class InputMode(Node):
    def prep(self,shared):
        if "input_type" not in shared:
            input_type=input('Enter the input type : text or sound : ')
            shared['input_type']=input_type
        return shared['input_type']
    
    def exec(self,prep_res):
        if prep_res is None:
            return None
        if prep_res =='sound':
            return "capture_audio"
        return "capture_text"
            
    
    def post(self,shared,prep_res,exec_res):
        if prep_res is None or exec_res is None:
            return None
        return exec_res
    