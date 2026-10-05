# ANVReminder

A lightweight command-line reminder application built from scratch in Python.

ANVReminder lets you create reminders directly from the terminal using a small custom command syntax and displays a Tkinter notification when the specified duration has elapsed.

## Beta

This is an early beta release. The current goal is to establish the core reminder functionality and develop the command syntax before adding more advanced features.

## Usage

Start ANVReminder and enter a reminder command:

```text
remind in 30m for "Drink some water"
```

ANVReminder will set the reminder and trigger a notification after the specified duration.

### Available Syntax

| Syntax | Description |
|--------|-------------|
| `remind` | Creates a one-off (`nonce`) reminder |
| `in` | Specifies the reminder duration |
| `for` | Specifies the reminder message |
| `exit` | Exits the program |

### Duration Formats

ANVReminder currently accepts:

```text
500
500ms
5s
5m
2h
```

A number without a unit is interpreted as milliseconds.

## Examples

### Setting a Reminder

```text
ANVReminder BETA...

remind in 30m for "Drink some water"
```

After 30 minutes, ANVReminder opens a notification window displaying the message.

### Setting Multiple Reminders

Multiple reminders can be created during the same session:

```text
remind in 20m for "Check the oven"
remind in 1h for "Take a break"
remind in 2h for "Call Tom"
```

### Exiting

```text
exit
```

## Current Architecture

The project is intentionally simple at this stage:

```text
User Input
    ↓
Tokenization
    ↓
Parser
    ↓
Reminder
    ↓
Duration Conversion
    ↓
Reminder Scheduler
    ↓
Tkinter Notification
```

The command parser was implemented from scratch rather than relying on a command-line argument parsing library.

Each reminder currently has a type. The `remind` command assigns the `nonce` type, representing a one-off reminder. The reminder type system is currently groundwork for future reminder types such as recurring reminders.

## Planned Features

Possible future improvements include:

* Recurring reminders
* Reminder management and cancellation
* Persistent reminders
* Better input validation
* Improved notification UI
* More flexible duration syntax
* More expressive command syntax
* Reminder presets and aliases

## Requirements

* Python 3
* Tkinter

## Status

**Open Beta**

The project is actively being developed and the command syntax is subject to change.
