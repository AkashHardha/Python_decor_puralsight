class Database():
    def __init__(self, path) :
        with open (path , 'r') as handler :
            import json
            self.data = json.load(handler)
    
    def balance(self , acc_id):
        acc = self.data.get(acc_id)

        if acc :
            return int(acc['paid']) - int(acc ['due'])
        else:
            None