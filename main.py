from random import randint

def main():

    array = [randint(-500, 500) for _ in range(10000)]

    insertion_sort(array)

    print(*array)


def insertion_sort(array):

    for i in range(1, len(array)):

        temp = array[i]

        j = i - 1

        while j >= 0 and temp < array[j]:

            array[j+1] = array[j]

            j -= 1

        array[j+1] = temp


if __name__ == "__main__":

    main()