# DESIGN.md

## Simple Markdown Note-Taking App (CLI)

---

## 1. Purpose

This document specifies the complete design and behavior of a **single-user, local-only CLI application** for managing simple Markdown notes. The application prioritizes **clarity, determinism, and clean architecture**, and is intended to be small but rigorously specified.

The spec is written to be directly usable as input for implementation or as a handoff to a Large Language Model (LLM).

---

## 2. Scope

### In Scope

* CLI-based interaction only
* Single user
* Local file-based persistence
* Create, list, show, complete, delete, and purge notes
* Deterministic behavior
* Clean separation of concerns

### Out of Scope

* GUI or TUI
* Networking or synchronization
* Multiple users
* Editing note content after creation
* Markdown rendering or preview
* Configuration files or custom paths

---

## 3. High-Level Characteristics

* **Language:** Python 3
* **Interface:** Command Line Interface (CLI)
* **Persistence:** Single local file (`tasks.md`) in current working directory
* **Data Format:** Strict, versioned, internal Markdown-based format
* **Encoding:** UTF-8 only
* **Execution:** `python main.py`
* **Dependencies:** Python standard library only

---

## 4. Core Domain Concepts

### 4.1 Note

A note is an immutable unit of content.

#### Attributes

* `id` (int):

  * Human-friendly
  * Starts at 1
  * Always contiguous (no gaps)
* `content` (string):

  * Single-line text
  * Markdown allowed, but not rendered
  * Leading/trailing whitespace is significant
* `completed` (bool):

  * Either completed or not completed

#### Invariants

* Content must be non-empty and not whitespace-only
* Content must not contain newline characters
* Content length must not exceed a fixed maximum
* Duplicate notes (exact string match, case-sensitive) are not allowed

---

## 5. Persistence Model

### 5.1 File Location

* File name: `tasks.md`
* Location: current working directory
* The application is the sole intended writer

### 5.2 File Ownership

* Manual edits are unsupported
* Any malformed or unsupported file results in a hard failure

### 5.3 Atomicity & Locking

* Writes are atomic:

  * Write to temporary file
  * Replace original in a single operation
* File is locked during write
* If lock cannot be acquired, the app fails immediately

### 5.4 Encoding

* UTF-8 only
* Any other encoding causes failure

---

## 6. File Format

### 6.1 Versioning

* File must include an explicit version header
* No backward compatibility is guaranteed
* Unsupported versions cause failure

### 6.2 Stability

* Format is strictly defined and treated as an internal contract
* Changes require version bump

*(Exact format definition may be specified in a separate document or section.)*

---

## 7. CLI Commands

All commands are **explicit and non-interactive**.

### 7.1 Add Note

```bash
python main.py add "Note content"
```

* Content passed as a single argument
* Validated before creation
* Creates a new note with `completed = false`

---

### 7.2 List Notes

```bash
python main.py list
python main.py list --completed
python main.py list --pending
```

* Displays notes in creation order
* Shows:

  * ID
  * Completion status (`[ ]` or `[x]`)
  * Full content

---

### 7.3 Show Note

```bash
python main.py show <id>
```

* Prints full Markdown content of the note
* Fails if ID does not exist

---

### 7.4 Complete Note

```bash
python main.py complete <id>
```

* Marks note as completed
* Idempotent operation

---

### 7.5 Delete Note

```bash
python main.py delete <id>
```

* Permanently removes the note
* Remaining notes are reindexed to keep IDs contiguous

---

### 7.6 Purge All Notes

```bash
python main.py purge --force
```

* Deletes all notes
* Requires explicit confirmation flag

---

### 7.7 Help & Version

```bash
python main.py --help
python main.py --version
```

* Help describes commands and usage
* Version prints application version only

---

## 8. Error Handling

* Errors are:

  * Concise
  * User-facing
  * Free of stack traces or internal details

* Non-zero exit code on failure

### Examples

* `Note with id 5 not found`
* `Duplicate note content`
* `Unsupported file format version`
* `Failed to acquire file lock`

---

## 9. Determinism

* Same input + same file state → same output
* No timestamps
* No randomness

---

## 10. Project Structure

* Clear separation of concerns:

  * CLI parsing
  * Application logic
  * Domain model
  * Persistence layer

* Single entry-point script

* No installation required

---

## 11. Testing

* Basic automated tests are included
* Focus on:

  * Parsing
  * Validation
  * Command behavior
  * File handling

---

## 12. Non-Goals (Explicit)

The application intentionally does **not**:

* Edit note content
* Render Markdown
* Support multi-line notes
* Allow configuration or plugins
* Support concurrent long-running sessions

---

## 13. Design Philosophy

* Fail fast
* Be explicit
* Prefer simplicity over flexibility
* Avoid overengineering
* Treat file format and CLI behavior as contracts

---

## 14. Completion Criteria

The project is considered complete when:

* All specified commands behave exactly as defined
* Data persists correctly across runs
* Errors are deterministic and user-friendly
* Code structure reflects
