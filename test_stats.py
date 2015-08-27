
from stats import mean
from nose.tools import assert_equal


def test_float_mean():
	assert_equal(mean([1,2]), 1.5)
#test_float_mean()

def test_mean():
	assert_equal(mean([4,8]), 6)
#test_mean()
