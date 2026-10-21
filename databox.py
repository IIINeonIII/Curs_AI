class DataBox:
    def __init__(self):
        self.data = []
        self.amount_of_data = 0

    def add_data(self, value):
        if isinstance(value, (int, float)):
            self.data.append(value)
            self.amount_of_data += 1

        elif isinstance(value, list) and all(isinstance(item, (int, float)) for item in value):
                self.data.extend(value)
                self.amount_of_data += len(value)
        else:
            raise TypeError("Data must be int, float, or list of int/float.")

    def clear_data(self):
        self.data.clear()
        self.amount_of_data = 0

from tensorflow import keras

