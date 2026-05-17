"""Simple data processors for numeric, text, and log payloads."""

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Base processor that stores validated items as ranked strings.

    Subclasses define validation and ingestion rules for a specific input type.
    """

    def __init__(self) -> None:
        """Initialize internal FIFO storage and rank counter."""
        self._storage: list[tuple[int, str]] = []
        self._current_rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check whether 'data' is valid for this processor."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Store validated input data in the internal queue.

        Raises:
            ValueError: If 'data' is invalid for the processor.
        """
        pass

    def output(self) -> tuple[int, str]:
        """Return and remove the oldest processed item from the queue.

        Returns:
            tuple[int, str]: A pair '(rank, value)' from the queue.

        Raises:
            IndexError: If there are no processed items available.
        """
        if not self._storage:
            raise IndexError("No data to output")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    """Processor for numbers and lists of numbers."""

    def validate(self, data: Any) -> bool:
        """Check whether data is numeric or a list of numeric values."""
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int] | list[float]) -> None:
        """Store numeric input items as strings with incremental rank.

        Raises:
            ValueError: If 'data' does not match the numeric contract.
        """
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]

        for n in items:
            self._storage.append((self._current_rank, str(n)))
            self._current_rank += 1


class TextProcessor(DataProcessor):
    """Processor for text values and lists of text values."""

    def validate(self, data: Any) -> bool:
        """Check whether data is a string or a list of strings."""
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        """Store text input items with incremental rank.

        Raises:
            ValueError: If 'data' does not match the text contract.
        """
        if not self.validate(data):
            raise ValueError("Improper text data")

        items = data if isinstance(data, list) else [data]

        for n in items:
            self._storage.append((self._current_rank, n))
            self._current_rank += 1


class LogProcessor(DataProcessor):
    """Processor for structured logs with level and message fields."""

    def validate(self, data: Any) -> bool:
        """Check whether data is a valid log dict or a list of log dicts."""
        if isinstance(data, dict):
            return self._is_valid_log_dic(data)
        if isinstance(data, list):
            return all(
                isinstance(x, dict) and
                self._is_valid_log_dic(x) for x in data
            )
        return False

    def _is_valid_log_dic(self, data: Any) -> bool:
        """Check that a log dict has required string fields."""
        if not isinstance(data, dict):
            return False

        if 'log_level' not in data or 'log_message' not in data:
            return False

        check_message = isinstance(data['log_message'], str)
        check_level = isinstance(data['log_level'], str)

        return check_level and check_message

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        """Store logs as '"LEVEL: message"' strings with incremental rank.

        Raises:
            ValueError: If 'data' does not match the log contract.
        """
        if not self.validate(data):
            raise ValueError("Improper log data")

        items = data if isinstance(data, list) else [data]

        for x in items:
            new_log = f"{x['log_level']}: {x['log_message']}"
            self._storage.append((self._current_rank, new_log))
            self._current_rank += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    # --- TESTING NUMERIC PROCESSOR ---
    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()

    # Validation tests
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    # Invalid ingest testing (Raises an exception)
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        # The mypy warning will trigger, based on subject's requires
        num_proc.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")

    # Procesamiento y extracción
    data_num = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num}")
    num_proc.ingest(data_num)

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = num_proc.output()
        print(f" Numeric value {rank}: {value}")

    # --- TESTING TEXT PROCESSOR ---
    print("\nTesting Text Processor...")
    text_proc = TextProcessor()

    print(f" Trying to validate input '42': {text_proc.validate(42)}")

    data_text = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {data_text}")
    text_proc.ingest(data_text)

    print(" Extracting 1 value...")
    rank, value = text_proc.output()
    print(f" Text value {rank}: {value}")

    # --- TESTING LOG PROCESSOR ---
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()

    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    data_log = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f" Processing data: {data_log}")
    log_proc.ingest(data_log)

    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log_proc.output()
        print(f" Log entry {rank}: {value}")
