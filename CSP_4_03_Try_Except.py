


def sum(arr : list) -> int:
    """
    Modify the function such that it returns the sum of all numbers within the given list.
    :param arr:
    :return:
    """
    sum = 0
    for i in arr:
        try:
            sum += i
        except:
            print("Type not addable")
    return(sum)


def cleanData(rawData : list) ->list:
    """
    modify the function such that it takes in a list as an argument and will return a new list that
     contains only the values that can be typecast to a float.
    :param rawData:
    :return:
    """
    newList = []
    for i in rawData:
        try:
            newList.append(float(i))
        except:
            print("Sorry, this can't cast to a float!")
    return newList


def unreliableCalculator(divisors : list) -> list:
    """
    Modify the function such that it takes in a list as an argument and returns a new list where each
    index is 100 divided by the values from the input list.
    If division ever causes an error instead have the value be the type of error as a string.
    Example the list [100,50,25,"5"] as an argument would return [1, 2, 4, "TypeError"]
    :param divisors:
    :return:
    """
    newList = []
    for i in divisors:
        try:
            newList.append(100/i)
        except ZeroDivisionError:
            newList.append("ZeroDivisionError")
        except TypeError:
            newList.append("TypeError")
    return newList


def upperAll(arr : list) -> None:
    """
    Modify the function such that it "uppercases" all strings within the given argument list.
    The string method .upper() turns all characters in a string uppercase.
    You should modify the original list, not return a new list.
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        try:
            arr[i] = arr[i].upper()
        except:
            print("Cannot upper :(")

def firstItems(arr : list) -> list:
    """
    Modify the function below such that given a list of values. Many of the list elements will be lists
    themselves. For any list element that is a list, grab the first element from that list. If the list
    element is not a list then just grab the value itself.
    Create a new list of all the first indexes of inner lists or just values themselves.
    Example firstItems( [[1,2],[3,4],[5,6],[7,8]],9 ) == [1,3,5,7,9]
    :param arr:
    :return:
    """
    newList = []
    for i in arr:
        try:
            newList.append(i[0])
        except TypeError:
            newList.append(i)
    return newList
