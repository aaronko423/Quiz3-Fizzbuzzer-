class Fizzbuzzer:

    def __init__(self, start = 0):
        self.number = start

    def next(self):
        self.number = self.number + 1
        if self.number % 3 and self.number % 5 == 0:
            return "fizzbuzz"
        elif self.number % 3 == 0:
            return "fizz"
        elif self.number % 5 == 0:
            return "buzz"
        else:
            self.number = self.number
            return self.number

if __name__ == "__main__":

    buzzer = Fizzbuzzer()
    print(buzzer.next())
    print(buzzer.next())
    print(buzzer.next())
    print(buzzer.next())
    print(buzzer.next())
