import os
from pathlib import Path
from types import TracebackType
from typing import Optional, TextIO


# ==========================================
# 1. CUSTOM EXCEPTION DEFINITION
# ==========================================
class FileProcessingError(Exception):
    """Custom exception raised when file operations fail in high-level tasks."""
    pass


# ==========================================
# 2. ADVANCED CUSTOM CONTEXT MANAGER
# ==========================================
class SafeFileWriter:
    """
    A context manager that writes to a temporary file first.
    The original file is replaced ONLY if writing succeeds completely.
    If an error occurs mid-write, the temp file is cleaned up, preventing corruption.
    """

    def __init__(self, filename: str):
        self.filename = Path(filename)
        self.tmp_filename = Path(f"{filename}.tmp")
        self._file: Optional[TextIO] = None

    def __enter__(self) -> TextIO:
        self._file = self.tmp_filename.open("w", encoding="utf-8")
        return self._file

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[TracebackType]
    ) -> bool:
        # Always close the active stream first
        if self._file and not self._file.closed:
            self._file.close()

        # Handle failure: clean up temporary file
        if exc_type is not None:
            if self.tmp_filename.exists():
                self.tmp_filename.unlink()
            print(f"  [SafeFileWriter] Error detected ({exc_type.__name__}). Rollback complete.")
            return False  # Let exception propagate up

        # Handle success: replace original file with completed temp file
        self.tmp_filename.replace(self.filename)
        print(f"  [SafeFileWriter] Successfully saved to '{self.filename}'")
        return True


# ==========================================
# 3. INTERMEDIATE & ADVANCED FUNCTIONS
# ==========================================
def read_and_process_file(file_path_str: str) -> None:
    """
    Demonstrates:
    - pathlib usage
    - try / except / else / finally structure
    - Catching specific vs system exceptions
    """
    path = Path(file_path_str)
    file_obj = None

    print(f"\nAttempting to read: {path.name}")
    try:
        file_obj = path.open(mode="r", encoding="utf-8")
        content = file_obj.read()
    except FileNotFoundError as e:
        print(f"  [ERROR] File missing: '{e.filename}'")
    except (UnicodeDecodeError, PermissionError) as e:
        print(f"  [ERROR] Read access/encoding error: {e}")
    except OSError as e:
        print(f"  [ERROR] System I/O error: {e}")
    else:
        # Runs ONLY if try block succeeded without exceptions
        print("  [SUCCESS] Read completed!")
        print("  --- File Content ---")
        for line in content.strip().split("\n"):
            print(f"  | {line}")
        print("  --------------------")
    finally:
        # Runs ALWAYS (cleanup phase)
        if file_obj and not file_obj.closed:
            file_obj.close()
            print("  [CLEANUP] File stream explicitly closed.")
        else:
            print("  [CLEANUP] Done.")


def load_config_with_chaining(file_path_str: str) -> str:
    """Demonstrates exception chaining using 'raise ... from e'."""
    path = Path(file_path_str)
    try:
        with path.open("r", encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        # Wrap low-level system error into domain-specific exception
        raise FileProcessingError(f"Configuration load failed for '{path}'") from e


# ==========================================
# 4. MAIN EXECUTION PIPELINE
# ==========================================
def main():
    target_file = "demo_data.txt"

    print("=== STEP 1: Basic Writing & Appending ('with' context manager) ===")
    
    # Writing to file ('w' creates/overwrites)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write("Line 1: System Initialization\n")
        f.write("Line 2: Loading Parameters\n")

    # Appending to file ('a' adds to end)
    with open(target_file, "a", encoding="utf-8") as f:
        f.write("Line 3: Operation Normal\n")

    print(f"File '{target_file}' created and populated.")


    print("\n=== STEP 2: Safe File Operations (Custom Context Manager) ===")
    
    # 2a. Successful write using custom context manager
    with SafeFileWriter(target_file) as writer:
        writer.write("Line 1: Updated safely via SafeFileWriter\n")
        writer.write("Line 2: Atomic update completed successfully\n")

    # 2b. Failed write test (verifying atomic rollback)
    print("\nSimulating write failure midway through...")
    try:
        with SafeFileWriter(target_file) as writer:
            writer.write("Line 3: Temporary line before failure\n")
            raise ValueError("Simulated unexpected crash during write!")
    except ValueError as err:
        print(f"  Caught expected error: {err}")


    print("\n=== STEP 3: Comprehensive Reading with try / except / else / finally ===")
    
    # Read existing file
    read_and_process_file(target_file)
    
    # Read missing file to trigger exception flow
    read_and_process_file("non_existent_file.txt")


    print("\n=== STEP 4: Exception Chaining (raise ... from) ===")
    
    try:
        load_config_with_chaining("missing_config.json")
    except FileProcessingError as err:
        print(f"Caught high-level error: {err}")
        print(f"Underlying original error: {repr(err.__cause__)}")


    # Cleanup created demo file at the end
    if os.path.exists(target_file):
        os.remove(target_file)
        print(f"\n[CLEANUP] Deleted demo file '{target_file}'. Execution complete.")


if __name__ == "__main__":
    main()