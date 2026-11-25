import pytest
from services.testcase_service import TestCaseService
from models.testcase_status import TestCaseStatus

def test__add_test_case__should_create_test_case__when_all_required_field_are_filled():
    service = TestCaseService()
    title = "Register test case"
    description = "Add a new test case and see that it is added"
    expected_result = "Test case is added with ID TC-001."

    result = service.add_test_case(title, description, expected_result)

    assert result.succeeded is True
    assert result.test_case is not None
    assert result.test_case.id == "TC-001"
    assert result.test_case.title == title
    assert result.test_case.description == description
    assert result.test_case.expected_result == expected_result
    assert result.test_case.status == TestCaseStatus.NOT_RUN

def test__add_test_case__should_not_add_test_case__when_description_is_empty():
    service = TestCaseService()
    title = "Add test case validation"
    description = ""
    expected_result = "No test case is added"

    result = service.add_test_case(title, description, expected_result)

    assert result.succeeded is False
    assert result.test_case is None
    assert service.get_test_cases() == []


@pytest.mark.parametrize("title, description, expected_result, expected_errors", [
        ("", "Valid description", "Valid expected result", ["title is required"]),
        ("Valid title", "", "Valid expected result", ["description is required"]),
        ("Valid title", "Valid description", "", ["expected result is required"]),
        ("", "", "", ["title is required", "description is required", "expected result is required"])])

def test__validate_test_case__should_fail_when_required_field_is_empty(title, description, expected_result, expected_errors):
    service = TestCaseService()

    result = service.validate_test_case(title, description, expected_result)

    assert result.succeeded is False
    assert result.test_case is None
    for message in expected_errors:
        assert message in result.message

def test__validate_test_case__should_succeed__when_required_fields_are_filled_in():
    service = TestCaseService()
    title = "title"
    description = "description"
    expected_result = "expected result"

    result = service.validate_test_case(title, description, expected_result)
    
    assert result.succeeded is True


def test__add_test_case__should_assign_sequential_ids_to_new_test_cases():
    service = TestCaseService()
    title = "Generate ID"
    description = "Test that IDs increment for each new id"
    expected_result = "First test should have ID TC-001 and second TC-002"

    result1 = service.add_test_case(title, description, expected_result)
    result2 = service.add_test_case(title, description, expected_result)

    assert result1.succeeded is True
    assert result2.succeeded is True
    assert result1.test_case is not None
    assert result2.test_case is not None
    assert result1.test_case.id == "TC-001"
    assert result2.test_case.id == "TC-002"


@pytest.mark.parametrize("find_title", [
    "VALID TITLE",
    " valid title",
    "Valid Title ",
    " vAlId TiTlE "])

def test__find_test_cases_by_title__should_ignore_case_and_surrounding_whitespace(find_title):
    service = TestCaseService()
    title = "Valid title"
    description = "Should not be case sensitive and ignore surrounding whitespace"
    expected_result = "Should find title"

    result = service.add_test_case(title, description, expected_result)
    found_test_cases = service.find_test_cases_by_title(find_title)

    assert found_test_cases != []
    assert found_test_cases[0] == result.test_case

def test__find_test_cases_by_title__should_return_empty_list__when_title_does_not_match():
    service = TestCaseService()
    title = "title"
    description = "description"
    expected_result = "expected result"
    search_title = "another title"

    result = service.add_test_case(title, description, expected_result)
    found_test_cases = service.find_test_cases_by_title(search_title)
    
    assert result.succeeded is True
    assert isinstance(found_test_cases, list)
    assert found_test_cases == []
    assert len(service.get_test_cases()) == 1


def test__get_test_cases__should_return_list__with_added_test_cases():
    service = TestCaseService()
    title1 = "title1"
    description1 = "description1"
    expected_result1 = "expected result1"
    title2 = "title2"
    description2 = "description2"
    expected_result2 = "expected result2"

    result1 = service.add_test_case(title1, description1, expected_result1)
    result2 = service.add_test_case(title2, description2, expected_result2)
    all_test_cases = service.get_test_cases()

    assert isinstance(all_test_cases, list)
    assert len(all_test_cases) == 2
    assert all_test_cases[0] == result1.test_case
    assert all_test_cases[1] == result2.test_case


def test__update_test_case_status__should_update_status__of_test_case_with_valid_id():
    service = TestCaseService()
    title = "title"
    description = "description"
    expected_result = "expected result"
    new_status = TestCaseStatus.PASSED

    result = service.add_test_case(title, description, expected_result)
    change_status_result = service.update_test_case_status(result.test_case.id, new_status)

    assert change_status_result.succeeded is True
    assert change_status_result.test_case.status == TestCaseStatus.PASSED
    assert service.get_test_cases()[0].status == TestCaseStatus.PASSED

def test__update_test_case_status__should_not_update_status__of_test_case_with_invalid_id():
    service = TestCaseService()
    title = "title"
    description = "description"
    expected_result = "expected result"
    new_status = TestCaseStatus.PASSED

    result = service.add_test_case(title, description, expected_result)
    change_status_result = service.update_test_case_status("TC-999", new_status)

    assert change_status_result.succeeded is False
    assert result.test_case.status == TestCaseStatus.NOT_RUN
    assert change_status_result.test_case is None
    assert "TC-999" in change_status_result.message

