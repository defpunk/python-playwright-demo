def pytest_addoption(parser):
    parser.addoption("--output-subdir", action="store", default="", help="Sub directory of outout folder to store snapshots in")
