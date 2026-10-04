from reminder import set_reminder

def main():

    tags = {"-d", "-m", "-s"}

    reminder_settings = {
        "duration": 0,
        "message": ""
    }

    context = "none"

    prompt: str = input("ANVReminder BETA...\n")

    tokens: list = prompt.split()

    for token in tokens:

        if context == "none" and token == "exit":
            print("Exiting...")
            break

        if token in tags:

            match token:

                case "-m":
                    context = "message"
                    continue

                case "-d":
                    context = "duration"
                    continue

                case "-s":
                    context = "none"

                    converted_duration = convert_duration(reminder_settings["duration"])
                    set_reminder(reminder_settings["message"], converted_duration)
                    break

        match context:

            case "none":
                raise ValueError("Argument given for an unknown context type.\nDid you miss a tag?")

            case "message":
                reminder_settings[context] += token + " "

                if token[-1] == "\"":
                    reminder_settings[context] = reminder_settings[context].strip().strip('"\'')
                    print("Set message to", reminder_settings[context])
                    context="none"
                pass

            case "duration":
                reminder_settings[context] = token
                print("Set duration to", reminder_settings[context])
                context="none"
                pass

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










if __name__ == "__main__":

    main()