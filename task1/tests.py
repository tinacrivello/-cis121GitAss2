import task

data = [
    ['Hillsboro', 21, True, 'Edge Case'],
    ['Aloha', 59, False, 'Town negative'],
    ['Portland', 8, False, 'Age negative'],
    ['portland', 31, True, 'Spelling 1'],
    ['Portland', 51, True, 'Spelling 2']
]

def run_test():
    passed = 0
    num_tests = len(data)
    for i in range(num_tests):
        r = task.calculate_should_call(data[i][0], data[i][1])
        if r == data[i][2]:
            passed = passed + 1
            print("Test", data[i][3], "passed.")
        else:
            print("Test", data[i][3], "failed.")
    return passed, num_tests

try:
    passed, num_tests = run_test()
    print(passed, "out of", num_tests, "passed")
except Exception as e:
    print("Program Error...", e)
