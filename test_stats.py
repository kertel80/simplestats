
from stats import mean
from nose.tools import assert_equal


def test_mean():
	assert_equal(mean([2,4]), 3)
#test_mean()

def test_float_mean():
	assert(mean([1,2]) == 1.5)
#test_float_mean()

def test_mean():
	assert(mean([4,8]) == 6)
#test_mean()
