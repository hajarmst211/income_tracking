# session.py

class Session:
        def __init__(self):
            self.current_user = None 
        
        def start_session(self, username, first_name, last_name):
            self.current_user = username
        
        def close_session(self):
            self.current_user = None 
        
            

active_session = Session()