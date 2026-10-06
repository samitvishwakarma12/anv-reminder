# ANVReminder

A lightweight command-line reminder application built from scratch in Python.

ANVReminder lets you create reminders directly from the terminal using a small custom command syntax and displays a Tkinter notification when the specified duration has elapsed.

## Beta

ANVReminder is currently in beta. The project is focused on developing a simple and flexible reminder system while gradually introducing reminder management, persistence, and more advanced scheduling features.

## Usage

Start ANVReminder and enter a reminder command:

```text
remind in 30m for "Drink some water"
```

ANVReminder will set the reminder and trigger a notification after the specified duration.

### Available Syntax

|Syntax|Description|
|-|-|
|`remind`|Creates a one-off reminder|
|`in`|Specifies the reminder duration|
|`for`|Specifies the reminder message|
|`exit`|Exits the program|

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
Tkinter Notification
```

Duration conversion is performed while parsing the reminder input.

The command parser was implemented from scratch rather than relying on a command-line argument parsing library.

Each reminder currently has a type. The `remind` type represents a one-off reminder, while the `repeat` type is currently groundwork for future recurring reminders.

## Development

Development plans and upcoming milestones are maintained in [`PLANS.md`](PLANS.md).

The current development roadmap includes:

* Input validation
* Tkinter stability improvements
* Persistent reminder storage
* Repeating reminders
* Reminder cancellation
* Active reminder listing
* Improved reminder management
* More flexible duration syntax

## Requirements

* Python 3
* Tkinter

## Status

**Open Beta**

The project is actively being developed. The command syntax and internal architecture may change as new features are introduced.