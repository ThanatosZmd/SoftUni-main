nums = list(map(int, input().split(",")))
positives = list(map(str, [x for x in nums if x >= 0]))
negatives = list(map(str, [x for x in nums if x < 0]))
odds = list(map(str, [x for x in nums if x % 2 != 0]))
evens = list(map(str, [x for x in nums if x % 2 == 0]))
print(f'Positive: {", ".join(positives)}\n'
      f'Negative: {", ".join(negatives)}\n'
      f'Even: {", ".join(evens)}\n'
      f'Odd: {", ".join(odds)}')
