from reminder import set_reminder

class Reminder:

    def __init__(self) -> None:
        self.type = None
        self.duration = None
        self.message = ""


def main():

    tags = {"in", "for"}


    reminders = []

    i=0
    

    while True:
        prompt: str = input("ANVReminder BETA...\nType 'exit' to exit\n")

        context = "none"

        reminders.append(Reminder())
        tokens: list = prompt.split()

        for token in tokens:

            if context == "none" and token == "exit":
                print("Exiting...")
                context = "exit"
                break

            if context!="message" and token in tags:

                match token:

                    case "for":
                        context = "message"
                        continue

                    case "in":
                        context = "duration"
                        continue

            match context:

                case "none":
                    raise ValueError("Argument given for an unknown context type.\nDid you miss a tag?")

                case "message":
                    reminders[i].message += token + " "

                    if token[-1] == "\"":
                        reminders[i].message = reminders[i].message.strip().strip('"\'')
                        print("Set message to", reminders[i].message)
                        context="none"
                    

                case "duration":
                    reminders[i].duration = token
                    print("Set duration to", reminders[i].duration)
                    context="none"

        if context == "exit":
            break 
                    

        converted_duration = convert_duration(reminders[i].duration)
        set_reminder(reminders[i].message, converted_duration)
        i+=1

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