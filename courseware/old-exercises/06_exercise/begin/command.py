from calculator import Calculator
from history import History
from history_export import (
    HistoryCsvFileExport,
    HistoryJsonFileExport,
    HistoryYamlFileExport,
)
from user_input import (
    get_entry_id_to_remove,
    get_operand,
    get_save_file_name,
)


def command_math(
    history: History, calculator: Calculator, op_name: str
) -> None:
    operand = get_operand()
    history.append_history_entry(op_name, operand)
    print(f"Result: {calculator.result()}")


def command_result(calculator: Calculator) -> None:
    print(f"Result: {calculator.result()}")
    print(f"Operation Count: {calculator.operation_count()}")


def command_show_history(history: History) -> None:
    for entry in history:
        print(entry)


def command_remove_history_entry(history: History) -> None:
    history.remove_history_entry(get_entry_id_to_remove())


def command_clear_history(history: History) -> None:
    history.clear_history_entries()


def command_save_history(history: History) -> None:
    # HistoryCsvFileExport(get_save_file_name(), doublequote=True).save(history)
    # HistoryJsonFileExport(get_save_file_name(), indent=1).save(history)
    HistoryYamlFileExport(get_save_file_name()).save(history)


def command_invalid() -> None:
    print("Invalid command. Please try again.")


def is_math_command(command: str) -> bool:
    return command in ["add", "subtract", "multiply", "divide"]
