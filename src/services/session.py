# session.py

class Session:
        def __init__(self):
            self.current_user = None 
            self.first_name = None
            self.last_name = None
        
        
        def start_session(self, username, first_name, last_name):
            self.current_user = username
            self.first_name = first_name
            self.last_name = last_name
        
        
        def close_session(self):
            self.current_user = None 
            self.first_name = None
            self.last_name = None
            

user_session = Session()