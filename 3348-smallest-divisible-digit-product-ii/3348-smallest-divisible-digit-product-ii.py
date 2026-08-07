from collections import Counter

DIGIT_PRIMES = {
    0: Counter(), 1: Counter(),
    2: Counter({2: 1}), 3: Counter({3: 1}),
    4: Counter({2: 2}), 5: Counter({5: 1}),
    6: Counter({2: 1, 3: 1}), 7: Counter({7: 1}),
    8: Counter({2: 3}), 9: Counter({3: 2}),
}
PRIMES = (2, 3, 5, 7)

def factorize_t(t):
    need = Counter()
    for p in PRIMES:
        while t % p == 0:
            t //= p
            need[p] += 1
    return need, t == 1

def string_prime_count(s):
    cnt = Counter()
    for ch in s:
        cnt.update(DIGIT_PRIMES[int(ch)])
    return cnt

def clamp_subtract(a, b):
    res = Counter(a)
    for k, v in b.items():
        res[k] = max(0, res[k] - v)
    return res

def covers(have, need):
    return all(have[p] >= need[p] for p in PRIMES)

def digits_for(need):
    eights, rem2 = divmod(need[2], 3)
    nines, threes = divmod(need[3], 2)
    fours, twos = divmod(rem2, 2)
    sixes = 0
    if twos == 1 and threes == 1:
        twos, threes, sixes = 0, 0, 1
    if threes == 1 and fours == 1:
        twos, sixes, threes, fours = 1, sixes + 1, 0, 0
    return Counter({2: twos, 3: threes, 4: fours, 5: need[5],
                     6: sixes, 7: need[7], 8: eights, 9: nines})

def digit_total(counter):
    return sum(counter.values())

def render(counter):
    return ''.join(str(d) * counter[d] for d in range(2, 10))

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        need, feasible = factorize_t(t)
        if not feasible:
            return "-1"

        base = digits_for(need)
        if digit_total(base) > len(num):
            return render(base)

        total = string_prime_count(num)
        first_zero = num.find('0')
        if first_zero == -1:
            first_zero = len(num)
            if covers(total, need):
                return num

        prefix_count = Counter(total)
        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])
            prefix_count = clamp_subtract(prefix_count, DIGIT_PRIMES[d])
            space_after = len(num) - 1 - i
            if i > first_zero:
                continue
            for bigger in range(d + 1, 10):
                remaining_need = clamp_subtract(clamp_subtract(need, prefix_count), DIGIT_PRIMES[bigger])
                fill = digits_for(remaining_need)
                if digit_total(fill) <= space_after:
                    pad = space_after - digit_total(fill)
                    return num[:i] + str(bigger) + '1' * pad + render(fill)

        extra = digits_for(need)
        return '1' * (len(num) + 1 - digit_total(extra)) + render(extra)