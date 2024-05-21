import datetime
from pathlib import Path
from loguru import logger
import pytest
from _pytest.logging import caplog as _caplog
import logging
import os
from pytest_metadata.plugin import metadata_key


@pytest.fixture
def caplog(_caplog):
    """
    A fixture that captures log output for testing.

    This fixture adds a custom logging handler to the Loguru logger to propagate log records
    to the standard logging module, allowing pytest's caplog fixture to capture Loguru logs.

    Args:
        _caplog: The caplog fixture provided by pytest.

    Yields:
        The caplog fixture to capture log output.
    """
    class PropogateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    handler_id = logger.add(
        PropogateHandler(), format="{message} {extra}", level="TRACE"
    )
    yield _caplog
    logger.remove(handler_id)


@pytest.fixture(autouse=True)
def write_logs(request):
    """
    A fixture that configures Loguru to write logs to files.

    This fixture automatically runs before each test to set up logging.
    It creates a log file in the 'tests/logs' directory, organized by test module and class names.

    Args:
        request: The pytest request object that provides information about the test.

    Side Effects:
        Creates directories and log files in the 'tests/logs' directory.
        Configures Loguru to write log output to the appropriate file.
    """
    
    postfix_file_name = "..."
    max_file_name_len = 100
    
    # put logs in tests/logs
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    log_path = Path(os.path.join(ROOT_DIR, "logs", "tests"))

    # tidy logs in subdirectories based on test module and class names
    module = request.module
    class_ = request.cls
    name = request.node.name 
    if len(name) > max_file_name_len:
        name = name[:max_file_name_len] + postfix_file_name   
    
    name += ".log"

    if module:
        log_path /= module.__name__.replace("tests.", "")
    if class_:
        log_path /= class_.__name__

    log_path.mkdir(parents=True, exist_ok=True)

    # append last part of the name
    log_path /= name

    # enable the logger
    logger.remove()
    logger.configure(handlers=[{"sink": log_path, "level": "TRACE", "mode": "w"}])
    logger.enable("my_package")


def pytest_configure(config):
    """
    Configures pytest to set a default HTML report file path if not provided.

    This function runs before tests start and checks if an HTML report path is specified.
    If not, it generates a report filename with the current date and time and sets it as the report path.

    Args:
        config: The pytest config object.
    """
    if not config.option.htmlpath:
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_filename = f"./tests/reports/report_{current_datetime}.html"
        config.option.htmlpath = report_filename
