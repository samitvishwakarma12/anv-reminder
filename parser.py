from main import Reminder



def tokenizer(input: str) -> list:

    tokens = input.split()

    return tokens



def parser(tokens: list[str], reminder: Reminder) -> None:

    context: None | str = None

    tags = {
        "remind", "for", "in"
    }

    message = ""

    for token in tokens:

        if context == None and token in tags:  

            match token:   

                case "remind":

                    reminder.set_reminder_type("remind")

                case "for":

                    context = "message"

                    continue

                case "in":

                    context = "duration"

                    continue

        else:

            match context:

                case None:

                    raise ValueError("Argument given for an unknown context type.\nDid you miss a tag?")

                case "message":

                    message += token + " "

                    if token[-1] == "\"":

                        message = message.strip().strip('"\'')

                        reminder.set_message(message)

                        print("Set message to", reminder.message)

                        context=None



                case "duration":

                    duration = token

                    converted_duration = convert_duration(duration)

                    reminder.set_duration(converted_duration)

                    print("Set duration to", reminder.duration)

                    context=None



def convert_duration(duration: str) -> int:

    units = {

        "ms": 1,

        "s": 1000,

        "m": 60_000,

        "h": 3_600_000

    }

    duration = duration.lower()

    for unit, multiplier in units.items():

        if duration.endswith(unit):

            value = duration[:-len(unit)]

            return int(value) * multiplier

    return int(duration)