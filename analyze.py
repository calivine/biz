

class Analyzer:

    def __init__(self, price):
        self.history = []
        self.old_price = None
        self.new_price = price
        self.alert_rule = 'change'
        self.cycles = 0

    def update_price(self, price):
        self.old_price = self.new_price
        self.history.append(self.old_price)
        self.new_price = price
        self.cycles += 1

    def alert_setting(self, rule):
        self.alert_rule = rule

    def analyze(self):
        if self.alert_rule == 'change':
            return self._change()
        elif self.alert_rule == 'big_move':
            return self._big_move()
        else:
            return False

    def _change(self):
        return self.new_price != self.old_price

    def _big_move(self):
        if self.cycles == 15:
            print(self.history)
            previous_price = self.history.pop(0)
            print(self.history)
            print("Previous price: {}".format(previous_price))
            change = self.new_price - previous_price
            percent_change = change / previous_price
            print("Price change: {}".format(percent_change))
            self.cycles = 0
            return percent_change >= 0.03 or percent_change <= -0.03
        else:
            return False



