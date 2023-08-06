

class Pickle:
    def __init__(self, filename):
        self.filename = filename

    def pick(self, data):
        import pickle as old_pickle
        with open(self.filename, 'wb') as f:
            old_pickle.dump(data, f)

    def unpick(self):
        import pickle as old_pickle
        with open(self.filename, 'rb') as f:
            return old_pickle.load(f)

    def remove(self):
        import os

        os.remove(self.filename)
