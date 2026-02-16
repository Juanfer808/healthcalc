from abc import ABC, abstractmethod
from healthcalc import InvalidHealthDataException


class HealthCalc(ABC):
    """Interface for the calculator of health parameters."""

    @abstractmethod
    def bmi_classification(self, bmi: float) -> str:
        """Calculate the BMI classification of a person.

        :param bmi: Body Mass Index (kg/m2)
        :return: String classification
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def body_mass_index(self, weight: float, height: float) -> float:
        """Calculate the Body Mass Index (BMI).
        
        :param weight: Weight (kg)
        :param height: Height (m)
        :return: BMI value (kg/m2)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass