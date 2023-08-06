import pytest


def test_a1():
    print('a1')


def test_a2():
    print('a2')
    assert 1 == 0


@pytest.mark.skip("跳过")
def test_a3():
    print('a1')


@pytest.mark.xfail(reason="预期失败")
def test_a4():
    print('a4')
    assert 1 > 2


@pytest.mark.xfail(reason="预期失败")
def test_a5():
    print('a5')
    assert 1 < 2


@pytest.fixture
def a6():
    1 / 0


def test_a6(a6):
    print('a6')
