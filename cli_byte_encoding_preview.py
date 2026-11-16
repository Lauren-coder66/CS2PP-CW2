"""Preview CLI input and byte conversion for CW2.

This module does not create a QR code or check Version 1 capacity.
"""

from __future__ import annotations

import argparse
from pathlib import Path


DEMO_INPUTS = (
    "known",
    "We've succeeded!",
    "~¡256_-_aA&ñ",
    "From α to ɷ...",
    "Sugarplum_Fairy_Nightmare",
)


def describe_input(value: str) -> str:
    """Return the completed encoding steps, or identify the first failure."""
    lines = [
        f"Input: {value!r}",
        "Mode: byte (0100)",
        "Character set attempted: ISO-8859-1",
    ]
    try:
        data = value.encode("iso-8859-1", errors="strict")
    except UnicodeEncodeError as error:
        character = value[error.start]
        lines.extend(
            [
                "Status: encoding stopped",
                f"First unsupported character: {character!r} at index {error.start} "
                f"(U+{ord(character):04X})",
                "No characters were replaced or removed.",
            ]
        )
        return "\n".join(lines)

    lines.extend(
        [
            "Status: byte conversion completed",
            f"Byte count: {len(data)}",
            f"Bytes (hex): {data.hex(' ')}",
            "Data bits: " + " ".join(f"{byte:08b}" for byte in data),
            "QR capacity, error correction, matrix and mask: not implemented yet",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--demo-dir",
        type=Path,
        help="Write one numbered progress record per specified coursework input.",
    )
    args = parser.parse_args()

    if args.demo_dir is not None:
        args.demo_dir.mkdir(parents=True, exist_ok=True)
        for number, value in enumerate(DEMO_INPUTS, start=1):
            path = args.demo_dir / f"demo_{number}.txt"
            path.write_text(describe_input(value) + "\n", encoding="utf-8")
            print(path)
        return

    value = input("Text to encode: ")
    print(describe_input(value))


if __name__ == "__main__":
    main()
