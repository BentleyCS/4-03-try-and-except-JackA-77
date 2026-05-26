import CSP_4_03_Try_Except as HW
def test_sum():
    assert HW.sum([1,7,"hello", 8.5]) == 16.5
    assert HW.sum(["Cat", "dog","7"]) ==0
    assert HW.sum([1,2,3,4]) ==10


def test_clean_data():
    assert HW.cleanData(["1", "7.5", "cat", "14.f"]) == [1.0,7.5]
    assert HW.cleanData(["1", "7.5", "cat", "14.6"]) == [1.0,7.5,14.6]


def test_unreliable_calculator():
    assert  HW.unreliableCalculator([100,700,3,0,12,"Cat"])==[1.0, 0.14285714285714285, 33.333333333333336, 'ZeroDivisionError', 8.333333333333334, 'TypeError']


def test_upper_all():
    words = ["hello", "Class", 1, "good", "job"]
    assert HW.upperAll(words)==None
    assert words==['HELLO', 'CLASS', 1, 'GOOD', 'JOB']


def test_first_items():
    assert HW.firstItems([1,[7,5],["hello"], ["food","Hello"],8]) == [1,7,"hello","food",8]
    assert HW.firstItems([[1,2],[3,4],[5,6],[7,8]]) == [1,3,5,7]
