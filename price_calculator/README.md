# Price calculator analysis

## First observations
### Code
I can see that the price will be incorrect for 13-year-olds, since they should get the price 100 kr, but the code says

```text
if age <= 13:
    return 50
```
which means that 13-year-olds will get the price 50, since it says if age is less than or equal to 13.
### Tests
In the first test, I can see that
```text
with pytest.raises(ValueError):
    calculator.calculate(-1)
```
should raise a ValueError since the value/age is less than 0. At first since this test doesn't have an assert part I was wondering if pytest.raise would be enough to check, but after using google and reading the documentation on <https://docs.pytest.org/en/7.1.x/how-to/assert.html> I saw that this is a type of assertion, and so this test should work as intended and check that a negative age raises ValueError, which it should according to the requirements.

In the second test I can see that since it doesn't test around the values where the price changes, it will miss that the price for age 13, that should be 100, will get value 50 with the original code.

So all tests will pass and it will look like the system works if you just look at how many tests passed, but the second test doesn't actually catch the error around the age group change from 0-12 to 13-64.

## What I have changed

### Tests
I started by changing the second test def test_calculate_at_price_boundary to test at the boundaries of the age groups changing. So I changed the parametrization to:
```text
@pytest.mark.parametrize(
    ("age", "expected_price"),
    [
        (0, 50),
        (12, 50),
        (13, 100),
        (64, 100),
        (65, 80),
        (100, 80),
    ])
```
This test will fail with the original code, since it will catch that the price for age 13 will be 50, when the expected price is 100.
I ran the updated test with the original price_calculator.py code and got the following as expected:
```text
============================== short test summary info ==============================
FAILED test_price_calculator.py::test_calculate_at_price_boundary[13-100] - assert 50 == 100
============================ 1 failed, 6 passed in 0.27s
```
By changing the test to test just at the boundaries of the age groups changing the test will catch errors like these, since it can be easy to make a small mistake like writing <= 13 instead of < 13.

### Code

In the code for class PriceCalculator I changed <= 13 to < 13 in the calculate() method. Then the calculator will:
- raise ValueError if the age is under 0/negative
- return 50 if the age is 0 or above but less than 13 (so ages 0-12)
- return 100 if the age is below 65 (so ages 13-64)
- return 80 for all other ages (so ages 65 and up)

Which is in accordance with the requirements we got in the assignment specification.

When I ran the tests after changing the code I got 7 passed tests.