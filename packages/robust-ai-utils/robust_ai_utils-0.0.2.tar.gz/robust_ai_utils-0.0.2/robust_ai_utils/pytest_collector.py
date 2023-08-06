import pytest
import dataclasses
import json
from coverage import Coverage
from typing import List, Dict, Optional, Tuple


@dataclasses.dataclass
class TestFailure:
    error_type: str
    error_details: str
    test_name: str
    keywords: List[str] = dataclasses.field(default_factory=list)
    status: str = "failed"
    error_location: Optional[str] = None


coverage_files: Dict[str, Coverage] = {}


def _get_error_type_and_details(report) -> Tuple[str, str, Optional[str]]:
    # TODO: handle the case when this is of type ReprExceptionInfo or FixtureLookupErrorRepr
    failure_details = report.longrepr
    try:
        error_type = failure_details.chain[0][0].reprentries[-1].reprfileloc.message
        test_location = failure_details.chain[0][0].reprentries[0].reprfileloc

        error_details = ""
        for trace in failure_details.chain:
            for entry in trace[0].reprentries:
                error_details += "\n".join(entry.lines)
                error_details += "\n"
        return error_type, error_details, f"{test_location.path}:{test_location.lineno}"
    except Exception:
        str_failure_details = str(failure_details).splitlines()
        error_type = str_failure_details[0]
        error_details = (
            "\n".join(str_failure_details[1:]) if len(str_failure_details) > 1 else ""
        )
        return error_type, error_details, None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global coverage_files
    outcome = yield
    report = outcome.get_result()
    coverage_file_name = f"{item.path}_{item.name}.coverage"

    if coverage_file_name not in coverage_files:
        coverage_files[coverage_file_name] = Coverage(data_file=coverage_file_name)  # type: ignore

    coverage = coverage_files[coverage_file_name]

    with open(f"{item.path}.test.jsonl", "a") as output_file:
        if report.when == "setup":
            coverage.start()
            output_file.write(
                json.dumps({"test_name": item.name, "status": "setup"}) + "\n"
            )
            if report.outcome == "failed":
                (
                    error_type,
                    error_details,
                    error_location,
                ) = _get_error_type_and_details(report)
                test_failure = TestFailure(
                    error_type=error_type,
                    error_details=error_details,
                    test_name=item.name,
                    error_location=error_location,
                )
                output_file.write(json.dumps(dataclasses.asdict(test_failure)) + "\n")

        if report.when == "call":
            coverage.stop()
            coverage.save()
            if report.outcome == "failed":
                (
                    error_type,
                    error_details,
                    error_location,
                ) = _get_error_type_and_details(report)
                test_failure = TestFailure(
                    error_type=error_type,
                    error_details=error_details,
                    test_name=item.name,
                    keywords=list(report.keywords.keys()),
                    error_location=error_location,
                )
                output_file.write(json.dumps(dataclasses.asdict(test_failure)) + "\n")
            elif report.outcome == "passed":
                output_file.write(
                    json.dumps({"test_name": item.name, "status": "passed"}) + "\n"
                )
            elif report.outcome == "skipped":
                output_file.write(
                    json.dumps({"test_name": item.name, "status": "skipped"}) + "\n"
                )
