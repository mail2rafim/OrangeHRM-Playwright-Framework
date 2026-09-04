import pytest

from utilities.json_reader import read_json

# Here in below ex, parametrized data is stored in same file.
@pytest.mark.parametrize(
    "fname,lname",
    [
        ("Monoj","Kumar"),
        ("Mohamed","Rafi"),
        ("John","Smith")
    ]
)
def test_employee_names(fname, lname):
    print(fname, lname)
    assert len(fname) > 0


# Below example, fetching required data from external file & just trying to access required key element.
def test_employee_dataprameter():
    data = read_json("test_data/employee_data_multi.json")
    print(data)
    for employee in data:
        print(employee["first_name"])


# here, we are actually fetching the required data from external file and passing it to the required methods, depending on data sets pytest will execute current test.
@pytest.mark.parametrize("employee", read_json("test_data/employee_data_multi.json"))
def test_employee(employee):
    print(employee["first_name"])
    print(employee["last_name"])
