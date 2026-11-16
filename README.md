# CW2 Stage 1: first progress checkpoint

This small prototype only covers dynamic command-line input and the first byte-conversion step. It is **not** a QR generator. The coursework specifies CSGitlab; confirm with the lecturer whether the group's private GitHub repository is acceptable instead.

Run interactively with Python 3.13.9:

```text
python qr_input_preview.py
```

Create five numbered progress records:

```text
python qr_input_preview.py --demo-dir demo_outputs
```

The coursework points to ISO-8859-1 for byte-mode comparison. That encoding cannot represent every character in the five supplied strings. This prototype reports the first unsupported character without replacing it; the group should confirm the intended handling with the lecturer. Longer inputs are converted to bytes here, but Version 1 capacity is **not yet checked**.

Next implementation steps: confirm character-set policy; add byte-mode bitstream fields, Version 1 Level L capacity checks, `reedsolo` error-correction codewords, matrix layout and mask 0, then annotated logs of every step. Review the work in the group repository before treating it as coursework code.
