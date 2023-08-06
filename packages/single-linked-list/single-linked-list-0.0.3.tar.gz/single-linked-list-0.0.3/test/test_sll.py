import pytest
from slll.slll import SingleLinkedList


def test_append():
    SLL = SingleLinkedList()
    SLL.append(0)
    SLL.append(1)
    SLL.append(2)

    assert '0 --> 1 --> 2' == SLL.__str__()
    assert 3 == SLL.__len__()


def test_traves():
    pass


def test_pre_append():
    SLL = SingleLinkedList()
    SLL.pre_append(3)
    SLL.append(0)
    SLL.append(1)
    SLL.append(2)

    assert '3 --> 0 --> 1 --> 2' == SLL.__str__()
    assert 4 == SLL.__len__()


def test_insert():
    SLL = SingleLinkedList()
    SLL.append(0)
    SLL.append(1)
    SLL.append(2)
    SLL.insert(0, 3)
    SLL.insert(3, 5)
    SLL.insert(-1, 4)

    assert 6 == SLL.__len__()
    assert '3 --> 0 --> 1 --> 5 --> 2 --> 4' == SLL.__str__()


def test_get():
    SLL = SingleLinkedList()
    SLL.append(0)
    SLL.append(1)
    SLL.append(2)

    assert SLL.get(0) == 0
    assert SLL.get(1) == 1
    assert SLL.get(2) == 2


def test_find():
    SLL = SingleLinkedList()
    SLL.append(0)
    SLL.append(1)
    SLL.append(2)

    assert SLL.find(0) == 0
    assert SLL.find(1) == 1
    assert SLL.find(2) == 2


def test_set():
    SLL = SingleLinkedList()
    SLL.append(0)
    SLL.append(1)
    SLL.append(2)

    SLL.set(0, 10)
    SLL.set(1, 10)
    SLL.set(2, 20)

    assert '10 --> 10 --> 20' == SLL.__str__()


def test_pop():
    SLL = SingleLinkedList()
    SLL.append(0)
    SLL.append(1)
    SLL.append(2)

    assert "0 --> 1 --> 2" == SLL.__str__()
    assert SLL.pop() == 2
    assert "0 --> 1" == SLL.__str__()
    assert SLL.pop() == 1
    assert "0" == SLL.__str__()


def test_pop_first():
    SLL = SingleLinkedList()
    SLL.append(0)
    SLL.append(1)
    SLL.append(2)

    assert "0 --> 1 --> 2" == SLL.__str__()
    assert SLL.pop_first() == 0
    assert "1 --> 2" == SLL.__str__()
    assert SLL.pop_first() == 1
    assert "2" == SLL.__str__()


def test_remove():
    SLL = SingleLinkedList()
    SLL.append(0)
    SLL.append(1)
    SLL.append(2)

    assert "0 --> 1 --> 2" == SLL.__str__()
    SLL.remove(2)
    assert "0 --> 1" == SLL.__str__()


def test_celer():
    SLL = SingleLinkedList()
    SLL.append(0)
    SLL.append(1)
    SLL.append(2)

    assert "0 --> 1 --> 2" == SLL.__str__()
    SLL.clear()
    assert '' == SLL.__str__()
