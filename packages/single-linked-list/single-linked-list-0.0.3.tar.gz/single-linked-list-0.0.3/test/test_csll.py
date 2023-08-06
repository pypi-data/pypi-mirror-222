import pytest
from slll.csll import CicruleSingeLinkedList


def test_append():
    CSLL = CicruleSingeLinkedList()
    CSLL.append(0)
    CSLL.append(1)
    CSLL.append(2)

    assert '0 --> 1 --> 2' == CSLL.__str__()
    assert 3 == CSLL.__len__()


def test_traves():
    pass


def test_pre_append():
    CSLL = CicruleSingeLinkedList()
    CSLL.pre_append(3)
    CSLL.append(0)
    CSLL.append(1)
    CSLL.append(2)

    assert '3 --> 0 --> 1 --> 2' == CSLL.__str__()
    assert 4 == CSLL.__len__()


def test_insert():
    CSLL = CicruleSingeLinkedList()
    CSLL.append(0)
    CSLL.append(1)
    CSLL.append(2)
    CSLL.insert(0, 3)
    CSLL.insert(3, 5)
    CSLL.insert(-1, 4)

    assert 6 == CSLL.__len__()
    assert '3 --> 0 --> 1 --> 5 --> 2 --> 4' == CSLL.__str__()


def test_set():
    CSLL = CicruleSingeLinkedList()
    CSLL.append(0)
    CSLL.append(1)
    CSLL.append(2)

    CSLL.set(1, 10)
    CSLL.set(2, 10)
    CSLL.set(-1, 20)

    assert 3 == CSLL.__len__()
    assert '10 --> 10 --> 20' == CSLL.__str__()


def test_get():
    CSLL = CicruleSingeLinkedList()
    CSLL.append(0)
    CSLL.append(1)
    CSLL.append(2)

    assert CSLL.get(0) == 0
    assert CSLL.get(1) == 1
    assert CSLL.get(2) == 2


def test_find():
    CSLL = CicruleSingeLinkedList()
    CSLL.append(0)
    CSLL.append(1)
    CSLL.append(2)

    assert CSLL.find(0) == 0
    assert CSLL.find(1) == 1
    assert CSLL.find(2) == 2


def test_pop():
    CSLL = CicruleSingeLinkedList()
    CSLL.append(0)
    CSLL.append(1)
    CSLL.append(2)

    assert "0 --> 1 --> 2" == CSLL.__str__()
    assert CSLL.pop() == 2
    assert "0 --> 1" == CSLL.__str__()
    assert CSLL.pop() == 1
    assert "0" == CSLL.__str__()
    assert CSLL.pop() == 0


def test_pop_first():
    CSLL = CicruleSingeLinkedList()
    CSLL.append(0)
    CSLL.append(1)
    CSLL.append(2)

    assert "0 --> 1 --> 2" == CSLL.__str__()
    assert CSLL.pop_first() == 0
    assert "1 --> 2" == CSLL.__str__()
    assert CSLL.pop_first() == 1
    assert "2" == CSLL.__str__()


def test_remove():
    CSLL = CicruleSingeLinkedList()
    CSLL.append(0)
    CSLL.append(1)
    CSLL.append(2)

    assert "0 --> 1 --> 2" == CSLL.__str__()
    CSLL.remove(2)
    assert "0 --> 1" == CSLL.__str__()


def test_celer():
    CSLL = CicruleSingeLinkedList()
    CSLL.append(0)
    CSLL.append(1)
    CSLL.append(2)

    assert "0 --> 1 --> 2" == CSLL.__str__()
    CSLL.celer()
    assert '' == CSLL.__str__()
