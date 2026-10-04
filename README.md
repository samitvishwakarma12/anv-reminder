# ANVReminder

A lightweight command-line reminder application built from scratch in Python.

ANVReminder lets you create a reminder using a small custom command syntax and displays a Tkinter notification when the specified duration has elapsed.

## Beta

This is an early beta release. The current goal is to establish the core reminder functionality and experiment with the command syntax before adding more advanced features.

## Usage

Start ANVReminder and enter a command:

```text
-m "Drink some water" -d 30m -s
```

### Available options

| Option | Description               |
| ------ | ------------------------- |
| `-m`   | Set the reminder message  |
| `-d`   | Set the reminder duration |
| `-s`   | Submit the reminder       |
| `exit` | Exit the program          |

### Duration formats

ANVReminder currently accepts:

```text
500
500ms
5s
5m
2h
```

A number without a unit is interpreted as milliseconds.

## Example

```text
ANVReminder BETA...

-m "Drink some water" -d 30m -s
```

After 30 minutes, ANVReminder opens a notification window displaying the message.

## Current Architecture

The project is intentionally simple at this stage:

```text
User Input
    ↓
Tokenization
    ↓
Parser
    ↓
Reminder Settings
    ↓
Duration Conversion
    ↓
Reminder
    ↓
Tkinter Notification
```

The command parser was implemented from scratch rather than relying on a command-line argument parsing library.

## Planned Features

Possible future improvements include:

* Multiline command input
* Recurring reminders
* Multiple simultaneous reminders
* Persistent reminders
* Better input validation
* Improved notification UI
* More flexible duration syntax
* A more expressive command language

## Requirements

* Python 3
* Tkinter

## Status

**Open Beta — v0.1.0**
