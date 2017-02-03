import pytest


@pytest.fixture()
def ies(chain):
    _ies, _ = chain.store.provider.get_or_deploy_contract('TestIndexedEnumerableSetLib')
    return _ies


def test_getting(chain, ies):
    chain.wait.for_receipt(ies.transact().add('value-a'))
    chain.wait.for_receipt(ies.transact().add('value-b'))
    chain.wait.for_receipt(ies.transact().add('value-c'))
    chain.wait.for_receipt(ies.transact().add('value-d'))
    chain.wait.for_receipt(ies.transact().add('value-e'))

    assert ies.call().indexOf('value-a') == 0
    assert ies.call().indexOf('value-b') == 1
    assert ies.call().indexOf('value-c') == 2
    assert ies.call().indexOf('value-d') == 3
    assert ies.call().indexOf('value-e') == 4

    assert ies.call().get(0) == 'value-a' + '\x00' * 25
    assert ies.call().get(1) == 'value-b' + '\x00' * 25
    assert ies.call().get(2) == 'value-c' + '\x00' * 25
    assert ies.call().get(3) == 'value-d' + '\x00' * 25
    assert ies.call().get(4) == 'value-e' + '\x00' * 25


def test_size(chain, ies):
    assert ies.call().size() == 0

    chain.wait.for_receipt(ies.transact().add('value-a'))

    assert ies.call().size() == 1

    chain.wait.for_receipt(ies.transact().add('value-a'))

    assert ies.call().size() == 1

    chain.wait.for_receipt(ies.transact().add('value-b'))
    chain.wait.for_receipt(ies.transact().add('value-c'))
    chain.wait.for_receipt(ies.transact().add('value-d'))

    assert ies.call().size() == 4

    chain.wait.for_receipt(ies.transact().add('value-e'))

    assert ies.call().size() == 5

    chain.wait.for_receipt(ies.transact().remove('value-a'))
    chain.wait.for_receipt(ies.transact().pop(ies.call().indexOf('value-c')))
    chain.wait.for_receipt(ies.transact().remove('value-e'))

    assert ies.call().size() == 2

    chain.wait.for_receipt(ies.transact().add('value-a'))
    chain.wait.for_receipt(ies.transact().add('value-e'))
    chain.wait.for_receipt(ies.transact().pop(ies.call().indexOf('value-d')))

    assert ies.call().size() == 3


def test_adding(chain, ies):
    assert ies.call().contains('value-a') is False
    chain.wait.for_receipt(ies.transact().add('value-a'))
    assert ies.call().contains('value-a') is True

    assert ies.call().size() == 1

    chain.wait.for_receipt(ies.transact().add('value-a'))
    assert ies.call().contains('value-a') is True


def test_removing(chain, ies):
    chain.wait.for_receipt(ies.transact().add('value-a'))
    chain.wait.for_receipt(ies.transact().add('value-b'))
    chain.wait.for_receipt(ies.transact().add('value-c'))
    chain.wait.for_receipt(ies.transact().add('value-d'))
    chain.wait.for_receipt(ies.transact().add('value-e'))

    assert ies.call().contains('value-a') is True
    assert ies.call().contains('value-b') is True
    assert ies.call().contains('value-c') is True
    assert ies.call().contains('value-d') is True
    assert ies.call().contains('value-e') is True

    chain.wait.for_receipt(ies.transact().remove('value-c'))

    assert ies.call().contains('value-a') is True
    assert ies.call().contains('value-b') is True
    assert ies.call().contains('value-c') is False
    assert ies.call().contains('value-d') is True
    assert ies.call().contains('value-e') is True

    chain.wait.for_receipt(ies.transact().remove('value-b'))

    assert ies.call().contains('value-a') is True
    assert ies.call().contains('value-b') is False
    assert ies.call().contains('value-c') is False
    assert ies.call().contains('value-d') is True
    assert ies.call().contains('value-e') is True

    chain.wait.for_receipt(ies.transact().remove('value-e'))

    assert ies.call().contains('value-a') is True
    assert ies.call().contains('value-b') is False
    assert ies.call().contains('value-c') is False
    assert ies.call().contains('value-d') is True
    assert ies.call().contains('value-e') is False

    chain.wait.for_receipt(ies.transact().remove('value-a'))

    assert ies.call().contains('value-a') is False
    assert ies.call().contains('value-b') is False
    assert ies.call().contains('value-c') is False
    assert ies.call().contains('value-d') is True
    assert ies.call().contains('value-e') is False

    chain.wait.for_receipt(ies.transact().remove('value-d'))

    assert ies.call().contains('value-a') is False
    assert ies.call().contains('value-b') is False
    assert ies.call().contains('value-c') is False
    assert ies.call().contains('value-d') is False
    assert ies.call().contains('value-e') is False


def test_removing(chain, ies):
    chain.wait.for_receipt(ies.transact().add('value-a'))
    chain.wait.for_receipt(ies.transact().add('value-b'))
    chain.wait.for_receipt(ies.transact().add('value-c'))
    chain.wait.for_receipt(ies.transact().add('value-d'))
    chain.wait.for_receipt(ies.transact().add('value-e'))

    assert ies.call().contains('value-a') is True
    assert ies.call().contains('value-b') is True
    assert ies.call().contains('value-c') is True
    assert ies.call().contains('value-d') is True
    assert ies.call().contains('value-e') is True

    chain.wait.for_receipt(ies.transact().remove('value-c'))

    assert ies.call().contains('value-a') is True
    assert ies.call().contains('value-b') is True
    assert ies.call().contains('value-c') is False
    assert ies.call().contains('value-d') is True
    assert ies.call().contains('value-e') is True

    chain.wait.for_receipt(ies.transact().remove('value-b'))

    assert ies.call().contains('value-a') is True
    assert ies.call().contains('value-b') is False
    assert ies.call().contains('value-c') is False
    assert ies.call().contains('value-d') is True
    assert ies.call().contains('value-e') is True

    chain.wait.for_receipt(ies.transact().remove('value-e'))

    assert ies.call().contains('value-a') is True
    assert ies.call().contains('value-b') is False
    assert ies.call().contains('value-c') is False
    assert ies.call().contains('value-d') is True
    assert ies.call().contains('value-e') is False

    chain.wait.for_receipt(ies.transact().remove('value-a'))

    assert ies.call().contains('value-a') is False
    assert ies.call().contains('value-b') is False
    assert ies.call().contains('value-c') is False
    assert ies.call().contains('value-d') is True
    assert ies.call().contains('value-e') is False

    chain.wait.for_receipt(ies.transact().remove('value-d'))

    assert ies.call().contains('value-a') is False
    assert ies.call().contains('value-b') is False
    assert ies.call().contains('value-c') is False
    assert ies.call().contains('value-d') is False
    assert ies.call().contains('value-e') is False


def test_popping(chain, ies):
    chain.wait.for_receipt(ies.transact().add('value-a'))
    chain.wait.for_receipt(ies.transact().add('value-b'))
    chain.wait.for_receipt(ies.transact().add('value-c'))
    chain.wait.for_receipt(ies.transact().add('value-d'))
    chain.wait.for_receipt(ies.transact().add('value-e'))

    assert ies.call().indexOf('value-a') == 0
    assert ies.call().indexOf('value-b') == 1
    assert ies.call().indexOf('value-c') == 2
    assert ies.call().indexOf('value-d') == 3
    assert ies.call().indexOf('value-e') == 4

    chain.wait.for_receipt(ies.transact().pop(0))

    assert ies.call().lastPop() == 'value-a' + '\x00' * 25
    assert ies.call().indexOf('value-b') == 1
    assert ies.call().indexOf('value-c') == 2
    assert ies.call().indexOf('value-d') == 3
    assert ies.call().indexOf('value-e') == 0

    chain.wait.for_receipt(ies.transact().pop(2))

    assert ies.call().lastPop() == 'value-c' + '\x00' * 25
    assert ies.call().indexOf('value-b') == 1
    assert ies.call().indexOf('value-d') == 2
    assert ies.call().indexOf('value-e') == 0

    chain.wait.for_receipt(ies.transact().pop(1))

    assert ies.call().lastPop() == 'value-b' + '\x00' * 25
    assert ies.call().indexOf('value-d') == 1
    assert ies.call().indexOf('value-e') == 0

    chain.wait.for_receipt(ies.transact().pop(0))

    assert ies.call().lastPop() == 'value-e' + '\x00' * 25
    assert ies.call().indexOf('value-d') == 0

    chain.wait.for_receipt(ies.transact().pop(0))

    assert ies.call().lastPop() == 'value-d' + '\x00' * 25


def test_indexes(chain, ies):
    chain.wait.for_receipt(ies.transact().add('value-a'))
    chain.wait.for_receipt(ies.transact().add('value-b'))
    chain.wait.for_receipt(ies.transact().add('value-c'))
    chain.wait.for_receipt(ies.transact().add('value-d'))
    chain.wait.for_receipt(ies.transact().add('value-e'))

    assert ies.call().indexOf('value-a') == 0
    assert ies.call().indexOf('value-b') == 1
    assert ies.call().indexOf('value-c') == 2
    assert ies.call().indexOf('value-d') == 3
    assert ies.call().indexOf('value-e') == 4

    chain.wait.for_receipt(ies.transact().remove('value-c'))

    assert ies.call().indexOf('value-a') == 0
    assert ies.call().indexOf('value-b') == 1
    assert ies.call().indexOf('value-d') == 3
    assert ies.call().indexOf('value-e') == 2 # moved to fill gap

    chain.wait.for_receipt(ies.transact().remove('value-a'))

    assert ies.call().indexOf('value-b') == 1
    assert ies.call().indexOf('value-d') == 0 # moved to fill gap
    assert ies.call().indexOf('value-e') == 2 # moved to fill gap

    chain.wait.for_receipt(ies.transact().remove('value-e'))

    assert ies.call().indexOf('value-b') == 1
    assert ies.call().indexOf('value-d') == 0 # moved to fill gap

    chain.wait.for_receipt(ies.transact().remove('value-d'))

    assert ies.call().indexOf('value-b') == 0 # moved to fill gap


def test_contains(chain, ies):
    assert ies.call().contains('value-a') == False
    assert ies.call().contains('value-b') == False
    assert ies.call().contains('value-c') == False
    assert ies.call().contains('value-d') == False
    assert ies.call().contains('value-e') == False

    chain.wait.for_receipt(ies.transact().add('value-a'))
    chain.wait.for_receipt(ies.transact().add('value-b'))
    chain.wait.for_receipt(ies.transact().add('value-c'))
    chain.wait.for_receipt(ies.transact().add('value-d'))
    chain.wait.for_receipt(ies.transact().add('value-e'))

    assert ies.call().contains('value-a') == True
    assert ies.call().contains('value-b') == True
    assert ies.call().contains('value-c') == True
    assert ies.call().contains('value-d') == True
    assert ies.call().contains('value-e') == True

    chain.wait.for_receipt(ies.transact().remove('value-d'))

    assert ies.call().contains('value-a') == True
    assert ies.call().contains('value-b') == True
    assert ies.call().contains('value-c') == True
    assert ies.call().contains('value-d') == False
    assert ies.call().contains('value-e') == True

    chain.wait.for_receipt(ies.transact().remove('value-a'))

    assert ies.call().contains('value-a') == False
    assert ies.call().contains('value-b') == True
    assert ies.call().contains('value-c') == True
    assert ies.call().contains('value-d') == False
    assert ies.call().contains('value-e') == True

    chain.wait.for_receipt(ies.transact().remove('value-b'))

    assert ies.call().contains('value-a') == False
    assert ies.call().contains('value-b') == False
    assert ies.call().contains('value-c') == True
    assert ies.call().contains('value-d') == False
    assert ies.call().contains('value-e') == True

    chain.wait.for_receipt(ies.transact().remove('value-c'))

    assert ies.call().contains('value-a') == False
    assert ies.call().contains('value-b') == False
    assert ies.call().contains('value-c') == False
    assert ies.call().contains('value-d') == False
    assert ies.call().contains('value-e') == True

    chain.wait.for_receipt(ies.transact().remove('value-e'))

    assert ies.call().contains('value-a') == False
    assert ies.call().contains('value-b') == False
    assert ies.call().contains('value-c') == False
    assert ies.call().contains('value-d') == False
    assert ies.call().contains('value-e') == False
