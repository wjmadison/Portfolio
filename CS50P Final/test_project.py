from project import random_from_active
from project import scan_for_artist
from project import no_input_choices
import sys
def main():
    test_random_from_active()
    test_scan_for_artist()
    test_choices()
    sys.exit(0)

def test_random_from_active():
    l1 = ["value 1", "value 2"]
    l2 = ["value 1", "value 2"]
    l3 = ["value 1", "value 2"]
    l1_backward = ["value 2", "value 1"]
    lists = [l1, l2, l3]
    output = random_from_active(lists)
    assert output == l1 or output == l1_backward or output == ["value 1"] or output == ["value 2"]
    #Tests to confirm that it returns a randomized version of possible values in the list
    assert len(random_from_active(lists)) < 3
    #Tests trimming duplicates: random_from_active cycles through the outer list one song from each list until it has at least 5.
    #THEN it trims duplicates. Thus, this should add 6 values of some combination of value 1 and 2, then trim it back to two

def test_scan_for_artist():
    list1 = ["a - A", "b - B"]
    list2 = ["c - A", "d - B"]
    list3 = ["e - A"]
    master = [list1, list2, list3]
    assert scan_for_artist(master, "B") == [list1, list2]
    #Tests to confirm that it returns all playlists with a matching artist AND none without.

def test_choices():
    list1 = ["a - A", "b - B"]
    assert(no_input_choices(list1, "2")) == "b - B"
    #Tests to confirm there is no off-by-one error with the function

if __name__ == "__main__":
    main()