import random
import time


class PINCombo:

    def __init__(self, pin_as_int):
        pin_as_str = f"{pin_as_int:04}"
        self.first = int(pin_as_str[0])
        self.second = int(pin_as_str[1])
        self.third = int(pin_as_str[2])
        self.fourth = int(pin_as_str[3])

    def __eq__(self, other):
        return int(f"{self.first}{self.second}{self.third}{self.fourth}") == other

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"PIN: {self.first}{self.second}{self.third}{self.fourth}"

    def is_repeating(self):
        return len({self.first, self.second, self.third, self.fourth}) < 4

    def is_ascending(self):
        return self.first < self.second < self.third < self.fourth

    def is_sequential(self, num_digits):
        if num_digits == 4:
            return self.first + 1 == self.second and \
                   self.first + 2 == self.third and \
                   self.first + 3 == self.fourth
        elif num_digits == 3:
            return (self.first + 1 == self.second and self.first + 2 == self.third or
                    self.second + 1 == self.third and self.second + 2 == self.fourth)
        elif num_digits == 2:
            return (self.first + 1 == self.second or
                    self.second + 1 == self.third or
                    self.third + 1 == self.fourth)
        else:
            raise ValueError


# all_combos = [PINCombo(i) for i in range(10000)]
# repeating_combos = [i for i in all_combos if i.is_repeating()]
# four_ascend_combos = [i for i in all_combos if i.is_ascending()]
# four_sequential_combos = [i for i in all_combos if i.is_sequential(4)]
# three_sequential_combos = [i for i in all_combos if i.is_sequential(3)]
# two_sequential_combos = [i for i in all_combos if i.is_sequential(2)]
#
# print(f"All combos: {len(all_combos)} combinations")
# print(f"Repeating combos: {len(repeating_combos)} combinations")
# print(f"Four Digits Ascending combos: {len(four_ascend_combos)} combinations")
# print(f"Four Digits Sequential combos: {len(four_sequential_combos)} combinations")
# print(f"Three Digits Sequential combos: {len(three_sequential_combos)} combinations")
# print(f"Two Digits Sequential combos: {len(two_sequential_combos)} combinations")
#
# remaining_combos = [i for i in all_combos if (i not in repeating_combos and
#                                               i not in four_ascend_combos and
#                                               i not in four_sequential_combos and
#                                               i not in three_sequential_combos and
#                                               i not in two_sequential_combos)]
# print(f"Remaining valid combos: {len(remaining_combos)} ({(1-len(remaining_combos)/len(all_combos))*100:02.2f}%)")

NUM_TRIALS = 100

time_trials_in_ms = []
for tryi in range(NUM_TRIALS):
    secret_PIN = PINCombo(random.randint(0, 9999))
    start_time = time.perf_counter_ns()
    for i in range(10000):
        if secret_PIN == i:
            break
    else:
        raise ValueError
    end_time = time.perf_counter_ns()
    time_trials_in_ms.append((end_time - start_time) / 1e6)

print(time_trials_in_ms)
