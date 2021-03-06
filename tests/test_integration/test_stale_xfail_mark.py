def test_xfail_mark_absent(run_validator_for_test_files):
    errors = run_validator_for_test_files('test_absent_xfail_until_mark.py')

    lineno, _, error_message, _ = errors[0]

    assert len(errors) == 1
    assert lineno == 4
    assert error_message == 'FP006 xfail mark has wrong format. It should has `until` argument'


def test_xfail_until_mark_has_wrong_format(run_validator_for_test_files):
    errors = run_validator_for_test_files('test_xfail_until_wrong_format.py')

    lineno, _, error_message, _ = errors[0]

    assert len(errors) == 1
    assert lineno == 4
    assert error_message == 'FP007 xfail mark has wrong format. It should has `until` argument with datetime.date type'


def test_xfail_mark_has_stale_until_arg(run_validator_for_test_files):
    errors = run_validator_for_test_files('test_stale_xfail.py')

    lineno, _, error_message, _ = errors[0]

    assert len(errors) == 1
    assert lineno == 6
    assert error_message == 'FP008 stale xfail mark'
