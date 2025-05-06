class Countdown:
    def __init__(self, start):
        self.start = start
        
    def __iter__(self):
        # Initialize the countdown starting value
        self.current = self.start
        return self  # Return the object itself as an iterator
    
    def __next__(self):
        # Stop iteration when we reach 0 or below
        if self.current <= 0:
            raise StopIteration
        else:
            current_value = self.current
            self.current -= 1  # Decrement the current value
            return current_value

# Using the Countdown class
countdown = Countdown(5)
for number in countdown:
    print(number)
