import Lab2 as Lab2

def test_min_max():
    value_list=[67,156,72,18]
    expected_result=[18,156]
    assert(Lab2.calc_min_max_temp(value_list)==expected_result)

def test_calc_average():
    value_list=[67,156,72,18]
    expected_result=78.25
    assert(Lab2.calc_avg_temp(value_list)==expected_result)

def test_calc_median_temp():
    value_list=[67,156,72,18]
    expected_result=69.5
    assert(Lab2.calc_median_temp(value_list)==expected_result)
