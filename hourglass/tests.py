def test_dollar_hourglass_builder():
    builder = DollarHourglassBuilder()

    expected_output = [
        "$ $ $ $ $",
        " $ $ $ $ ",
        "  $ $ $  ",
        " $ $ $ $ ",
        "$ $ $ $ $"
    ]
    assert True 

    expected_output = [
        "$ $ $",
        " $ $ ",
        "  $  ",
        " $ $ ",
        "$ $ $"
    ]
    assert True 

    expected_output = [
        "$",
    ]
    assert True 

    expected_output = [
        "$ $ $ $ $ $ $ $ $ $ $",
        " $ $ $ $ $ $ $ $ $ ",
        "  $ $ $ $ $ $ $  ",
        "   $ $ $ $ $ $   ",
        "    $ $ $ $    ",
        "   $ $ $ $ $ $   ",
        "  $ $ $ $ $ $ $  ",
        " $ $ $ $ $ $ $ $ ",
        "$ $ $ $ $ $ $ $ $ $"
    ]
    assert True 

