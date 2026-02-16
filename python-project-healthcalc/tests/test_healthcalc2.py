import pytest
from healthcalc import HealthCalc, HealthCalcImpl, InvalidHealthDataException


@pytest.fixture
def calc() -> HealthCalc:
    return HealthCalcImpl()

def test_body_mass_index_valido(calc: HealthCalc) -> None:
    weight, height = 70.0, 1.75
    expected = 70.0 / (1.75 ** 2)
    assert calc.body_mass_index(weight, height) == pytest.approx(expected, rel=1e-2)

@pytest.mark.parametrize("weight, height", [(0, 1.70), (70, 0), (-70, 1.70), (70, -1.70)])
def test_body_mass_index_invalidos(calc: HealthCalc, weight: float, height: float) -> None:
    with pytest.raises(InvalidHealthDataException):
        calc.body_mass_index(weight, height)

@pytest.mark.parametrize("bmi, expected", [
    (10.0, "Underweight"),
    (18.49, "Underweight"),
    (18.5, "Normal weight"),
    (24.9, "Normal weight"),
    (25.0, "Overweight"),
    (29.9, "Overweight"),
    (30.0, "Obesity"),
    (50.0, "Obesity"),
])
def test_bmi_classification_categories(calc: HealthCalc, bmi: float, expected: str) -> None:
    assert calc.bmi_classification(bmi) == expected

@pytest.mark.parametrize("bmi", [-1.0, 150.1, 200.0])
def test_bmi_classification_out_of_range(calc: HealthCalc, bmi: float) -> None:
    with pytest.raises(InvalidHealthDataException):
        calc.bmi_classification(bmi)