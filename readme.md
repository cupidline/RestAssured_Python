pytest need to have "test_abcdef" in function to work and pytest.ini to collect your test case. your test case is separated by space in pytest.ini

to run it and generate report, use "py.test -sv --html YOURPATH/report.html" 