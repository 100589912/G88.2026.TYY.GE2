"""Module."""
import json
import re
from datetime import datetime
from pathlib import Path

from uc3m_consulting.enterprise_management_exception import (
    EnterpriseManagementException,
)
from uc3m_consulting.enterprise_project import EnterpriseProject, ProjectData


class EnterpriseManager:
    """Class for providing the methods for managing the orders."""

    VALID_DEPARTMENTS = ["HR", "FINANCE", "LEGAL", "LOGISTICS"]

    def __init__(self):
        pass

    @staticmethod
    def _store_operation(project_id: str):
        """Add generated project IDs into corporate_operations.json file."""
        operations_file = Path(__file__).resolve().parents[4] / "corporate_operations.json"
        operations = []

        if operations_file.exists():
            with operations_file.open("r", encoding="utf-8") as input_file:
                raw_content = input_file.read().strip()
                if raw_content:
                    parsed = json.loads(raw_content)
                    if isinstance(parsed, list):
                        operations = parsed
                    elif isinstance(parsed, dict) and isinstance(
                        parsed.get("operations"), list
                    ):
                        operations = parsed["operations"]
                    else:
                        raise EnterpriseManagementException(
                            "corporate_operations.json has invalid format"
                        )

        operations.append(project_id)
        with operations_file.open("w", encoding="utf-8") as output_file:
            json.dump(operations, output_file, indent=2)

    @staticmethod
    def validate_cif(cif: str):
        """
        RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE
        """
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        letter = cif[0]
        numbers = cif[1:8]
        control_char = cif[8]
        nums = [int(digit) for digit in numbers]
        # even
        even_sum = nums[1] + nums[3] + nums[5]
        # odd
        odd_sum = 0
        for i in [0, 2, 4, 6]:
            value = nums[i] * 2
            if value >= 10:
                value = (value // 10) + (value % 10)
            odd_sum += value
        new_sum = even_sum + odd_sum

        # base digit
        digit = new_sum % 10
        if digit == 0:
            base_digit = 0
        else:
            base_digit = 10 - digit
        # control letters
        letters = "JABCDEFGHI"
        if letter in "ABEH":
            return control_char == str(base_digit)
        if letter in "KPQS":
            return control_char == letters[base_digit]

        return control_char == str(base_digit) or control_char == letters[base_digit]

    @staticmethod
    def _validate_company_cif(company_cif: str):
        if not isinstance(company_cif, str):
            raise EnterpriseManagementException("Wrong CIF value - not a string")
        if len(company_cif) != 9:
            raise EnterpriseManagementException("Wrong CIF value - incorrect length")
        if not company_cif[0].isalpha():
            raise EnterpriseManagementException(
                "Wrong CIF value - first character not a letter"
            )
        if not company_cif[1:8].isdigit():
            raise EnterpriseManagementException("Wrong CIF value - invalid numeric part")
        if not EnterpriseManager.validate_cif(company_cif):
            raise EnterpriseManagementException(
                "Wrong CIF value - invalid control character"
            )

    @staticmethod
    def _validate_project_acronym(project_acronym: str):
        if not isinstance(project_acronym, str):
            raise EnterpriseManagementException("Wrong project acronym value - not a string")
        if len(project_acronym) < 5 or len(project_acronym) > 10:
            raise EnterpriseManagementException(
                "Wrong project acronym value - incorrect length"
            )
        if not re.match(r"^[A-Z0-9]+$", project_acronym):
            raise EnterpriseManagementException(
                "Wrong project acronym value - invalid format"
            )

    @staticmethod
    def _validate_project_description(project_description: str):
        if not isinstance(project_description, str):
            raise EnterpriseManagementException("Wrong operation name value - not a string")
        if len(project_description) < 10 or len(project_description) > 30:
            raise EnterpriseManagementException("Wrong operation name value - incorrect length")

    @staticmethod
    def _validate_department(department: str):
        if not isinstance(department, str):
            raise EnterpriseManagementException("Wrong department value - not a string")
        if department not in EnterpriseManager.VALID_DEPARTMENTS:
            raise EnterpriseManagementException("Wrong department value - invalid department")

    @staticmethod
    def _validate_date(date: str):
        if not isinstance(date, str):
            raise EnterpriseManagementException("Wrong date value - not a string")

        parts = date.split("/")
        if len(parts) != 3:
            raise EnterpriseManagementException("Wrong date value - incorrect format")

        try:
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        except ValueError as exc:
            raise EnterpriseManagementException("Wrong date value") from exc

        if day < 1 or day > 31:
            raise EnterpriseManagementException("Wrong date value - invalid day")
        if month < 1 or month > 12:
            raise EnterpriseManagementException("Wrong date value - invalid month")
        if year < 2025 or year > 2026:
            raise EnterpriseManagementException("Wrong date value - invalid year")
        try:
            datetime(year, month, day)  # catches invalid dates like 31/02
        except ValueError as exc:
            raise EnterpriseManagementException("Wrong date value") from exc

    @staticmethod
    def _validate_budget(budget: float):
        if not isinstance(budget, float):
            raise EnterpriseManagementException("Wrong budget value - not a float")
        if round(budget, 2) != budget:
            raise EnterpriseManagementException(
                "Wrong budget value - more than two decimal places"
            )
        if budget < 50000.00:
            raise EnterpriseManagementException(
                "Wrong budget value - less than minimum (50000.00)"
            )
        if budget > 1000000.00:
            raise EnterpriseManagementException(
                "Wrong budget value - over the maximum (1000000.00)"
            )

    def register_project(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self,
        company_cif: str,
        project_acronym: str,
        project_description: str,
        department: str,
        date: str,
        budget: float,
    ):
        """Validate registration input, persist project ID, and return the MD5 id."""
        EnterpriseManager._validate_company_cif(company_cif)
        EnterpriseManager._validate_project_acronym(project_acronym)
        EnterpriseManager._validate_project_description(project_description)
        EnterpriseManager._validate_department(department)
        EnterpriseManager._validate_date(date)
        EnterpriseManager._validate_budget(budget)

        project_data = ProjectData(
            company_cif=company_cif,
            project_acronym=project_acronym,
            project_description=project_description,
            department=department,
            starting_date=date,
            project_budget=budget,
        )
        obj = EnterpriseProject(project_data)
        project_id = obj.project_id
        EnterpriseManager._store_operation(project_id)
        return project_id
