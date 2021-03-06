def test_fixtures_should_be_in_usefixtures(run_validator_for_test_files):
    expected_error_message = (
        'FP009 test_with_no_usefixtures_where_needed should use '
        "fixtures as follows: @pytest.mark.usefixtures('caplog', 'tmp_path')"
    )

    errors = run_validator_for_test_files('test_with_fixtures.py')

    assert len(errors) == 1
    assert errors[0][2] == expected_error_message
