import math


class FifthException(Exception):
    pass


class Fifths:
    def __init__(self):
        self.stack = []
        self.fifth_commands_dict = {
            "PUSH": self.push_stack,
            "POP": self.pop_stack,
            "SWAP": self.swap_data,
            "DUP": self.duplicate_data,
            "EXIT": self.end_session,
            "+": self.add_data,
            "-": self.minus,
            "/": self.divisor,
            "*": self.multiple,
        }

    def push_stack(self, data):
        self.stack.append(data)
        return self.stack

    def pop_stack(self):
        try:
            self.stack.pop()
            return self.stack
        except IndexError:
            raise FifthException("ERROR")

    def swap_data(self):
        self.stack[-2], self.stack[-1] = self.stack[-1], self.stack[-2]
        return self.stack

    def duplicate_data(self):
        if self.stack:
            self.push_stack(self.stack[-1])
            return self.stack
        raise FifthException("ERROR")

    def end_session(self):
        exit(0)

    def add_data(self):
        if len(self.stack) > 1:
            added_data = self.stack[-2] + self.stack[-1]
            del self.stack[-2:]
            self.push_stack(added_data)

        else:
            raise FifthException()

    def minus(self):
        if len(self.stack) > 1:
            minus_data = self.stack[-2] - self.stack[-1]
            del self.stack[-2:]
            self.push_stack(minus_data)
        else:
            raise FifthException()

    def divisor(self):
        if len(self.stack) > 1:
            divisor_data = math.floor(self.stack[-2] / self.stack[-1])
            del self.stack[-2:]
            self.push_stack(divisor_data)
        else:
            raise FifthException()

    def multiple(self):
        if len(self.stack) > 1:
            result = self.stack[-2] * self.stack[-1]
            del self.stack[-2:]
            self.push_stack(result)
        else:
            raise FifthException()

    def run(self):
        commands = "start"
        while commands != "EXIT":
            print(f"stack is {self.stack}")
            command = input().upper()
            try:
                if len(command.split()) == 2:
                    func, arg = command.split()
                    self.fifth_commands_dict[func](int(arg))
                else:
                    self.fifth_commands_dict[command]()
            except (FifthException, ValueError, TypeError):
                print("ERROR")
            except KeyError:
                print("WRONG COMMAND")


if __name__ == "__main__":
    fifths_engine = Fifths()
    fifths_engine.run()
