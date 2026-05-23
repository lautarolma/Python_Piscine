"""
    Data pipeline module with export plugins for processed data.

    This module provides processors for numeric, text, and log data along
    with export plugins for CSV and JSON output formats. It enables chaining
    of data processing with formatted output generation.
"""

from abc import ABC, abstractmethod
from typing import Protocol
from typing import Any


class DataProcessor(ABC):
    """
        Base processor that stores validated items as ranked strings.

        Subclasses define validation and ingestion rules for a specific input
        type.
    """

    def __init__(self) -> None:
        """Initialize internal FIFO storage and rank counter."""
        self._storage: list[tuple[int, str]] = []
        self._current_rank: int = 0
        self.total_processed: int = 0
        self.name: str | None = None

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check whether 'data' is valid for this processor."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """
            Store validated input data in the internal queue.

            Args:
                data: The input data to ingest and store.

            Raises:
                ValueError: If data fails validation for this processor.
        """
        pass

    def output(self) -> tuple[int, str]:
        """
            Return and remove the oldest processed item from the queue.

            Returns:
                Tuple containing (rank: int, value: str) of the oldest item.

            Raises:
                IndexError: If the storage queue is empty.
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
        """
            Store numeric input items as strings with incremental rank.

            Args:
                data: A number or list of numbers to ingest.

            Raises:
                ValueError: If data is not numeric or list of numbers.
        """
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]

        for n in items:
            self._storage.append((self._current_rank, str(n)))
            self._current_rank += 1
        self.total_processed = self._current_rank


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
        """
            Store text input items with incremental rank.

            Args:
                data: A string or list of strings to ingest.

            Raises:
                ValueError: If data is not a string or list of strings.
        """
        if not self.validate(data):
            raise ValueError("Improper text data")

        items = data if isinstance(data, list) else [data]

        for n in items:
            self._storage.append((self._current_rank, n))
            self._current_rank += 1
        self.total_processed = self._current_rank


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
        """
            Store logs as formatted strings with incremental rank.

            Args:
                data: Log dict or list of dicts with 'log_level' and
                'log_message'.

            Raises:
                ValueError: If data does not match the log dictionary contract.
        """
        if not self.validate(data):
            raise ValueError("Improper log data")

        items = data if isinstance(data, list) else [data]

        for x in items:
            new_log = f"{x['log_level']}: {x['log_message']}"
            self._storage.append((self._current_rank, new_log))
            self._current_rank += 1
        self.total_processed = self._current_rank


class ExportPlugin(Protocol):
    """
        Protocol for data export plugins.

        Defines the interface that all export plugins must implement.
    """

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """
            Export processed data in the format specific to the plugin.

            Args:
                data: List of (rank, value) tuples to export.
        """
        ...


class CsvExportPlugin:
    """
        CSV export plugin for outputting processed data in CSV format.
    """

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """
            Export data as comma-separated values.

            Args:
                data: List of (rank, value) tuples to export as CSV.
        """
        values = [item for _, item in data]
        csv_str = ",".join(values)
        print(f"CSV Output:\n{csv_str}")


class JsonExportPlugin:
    """
        JSON export plugin for outputting processed data in JSON format.
    """

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """
            Export data as JSON key-value pairs.

            Args:
                data: List of (rank, value) tuples to export as JSON.
        """
        pairs = [f'"item_{rank}": "{value}"' for rank, value in data]
        json_str = "{" + ", ".join(pairs) + "}"
        print(f"JSON Output:\n{json_str}")


class DataStream():
    """
        Orchestrate multiple data processors for stream processing.

        Manages a collection of registered processors, routing input items
        to appropriate processors based on validation. Supports exporting
        processed data through compatible export plugins.
    """
    def __init__(self) -> None:
        """
            Initialize the data stream with empty processor list.
        """
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """
            Register a new processor if not already registered.

            Args:
                proc: A DataProcessor instance to add to the stream.
        """
        if isinstance(proc, DataProcessor) and proc not in self._processors:
            self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """
            Process each item in stream using registered processors.

            Args:
                stream: List of items to process through registered processors.
        """
        if not self._processors:
            print("No processor found, no data\n")
        else:
            for item in stream:
                processed: bool = False
                for processor in self._processors:
                    if processor.validate(item):
                        try:
                            processor.ingest(item)
                            processed = True
                        except (ValueError, TypeError) as e:
                            print(
                                "DataStream error - Processor"
                                f"{processor.name} failed on {item}: {e}"
                            )
                if not processed:
                    print(
                        "DataStream error - Can't process element in stream:"
                        f" {item}"
                    )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """
            Consume items from processors and export using the given plugin.

            Args:
                nb: Number of items to consume from each processor.
                plugin: Export plugin implementing the ExportPlugin protocol.
        """
        for processor in self._processors:
            collection: list[tuple[int, str]] = []
            for _ in range(nb):
                if len(processor._storage) == 0:
                    break
                collection.append(processor.output())
            if collection:
                plugin.process_output(collection)

    def process_stats_show(self) -> None:
        """
            Print processing statistics for all registered processors.
        """
        for processor in self._processors:
            name = processor.name if processor.name else "UnnamedProcessor"
            remaining = len(processor._storage)
            print(
                f"{name}: total {processor.total_processed} items processed,"
                f"remaining {remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    print("\n== DataStream statistics ==")

    ds = DataStream()
    stream: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    ds.process_stream(stream)

    print("Registering Processors")
    num_proc = NumericProcessor()
    num_proc.name = "Numeric Processor"
    ds.register_processor(num_proc)
    text_proc = TextProcessor()
    text_proc.name = "Text Processor"
    ds.register_processor(text_proc)
    log_proc = LogProcessor()
    log_proc.name = "Log Processor"
    ds.register_processor(log_proc)

    print(f"\nSend first batch of data on stream: {stream}")
    ds.process_stream(stream)

    print("\n== DataStream statistics ==")
    ds.process_stats_show()

    csv = CsvExportPlugin()
    nb = 3
    print(f"\nSend {nb} processed data from each processor to a CSV plugin:")
    ds.output_pipeline(nb, csv)
    print("\n== DataStream statistics ==")
    ds.process_stats_show()
    stream = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {stream}")
    ds.process_stream(stream)

    print("\n== DataStream statistics ==")
    ds.process_stats_show()
    json = JsonExportPlugin()
    nb = 5
    print(f"\nSend {nb} processed data from each processor to a JSON plugin:")
    ds.output_pipeline(nb, json)
    print("\n== DataStream statistics ==")
    ds.process_stats_show()
