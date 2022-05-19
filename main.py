# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sort_list(lst):
    # Use a breakpoint in the code line below to debug your script.
    indexes = []
    distance = 0
    i = 0

    for v in lst:
        if v == 1:
            indexes.append(i)
        i += 1
    for i in range(len(indexes) - 1):
        if indexes[i + 1] - indexes[i] > 1:
            distance += indexes[i + 1] - (indexes[i] + 1)
            indexes[i + 1] = indexes[i] + 1
    return distance


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lst = [0,1,1,1,0,0,0,1,1]
    print(sort_list(lst))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
