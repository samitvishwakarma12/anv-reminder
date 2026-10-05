from reminder import set_reminder
import tkinter as tk

class Reminder:

    def __init__(self) -> None:
        self.type = None
        self.duration = None
        self.message = ""


def main():

    root = tk.Tk()
    root.withdraw()

    tags = {"in", "for", "remind"}


    reminders = []

    i=0
    

    while True:
        prompt: str = input("ANVReminder BETA...\nType 'exit' to exit\n")

        context: None | str = None

        reminders.append(Reminder())
        tokens: list = prompt.split()

        for token in tokens:

            if context == None and token == "exit":
                print("Exiting...")
                context = "exit"
                break

            if context!="message" and token in tags:

                match token:

                    case "remind":

                        if context == None:
                            if reminders[i].type == None:
                                reminders[i].type = "nonce" # One-off
                                continue
                            else:
                                raise SyntaxError("Repeated reminder type declaration. Remind must only be of a single type.")

                        else:
                            raise ValueError("Cannot use 'remind' for a context of", context)

                    case "for":
                        context = "message"
                        continue

                    case "in":
                        context = "duration"
                        continue

            match context:

                case None:
                    raise ValueError("Argument given for an unknown context type.\nDid you miss a tag?")

                case "message":
                    reminders[i].message += token + " "

                    if token[-1] == "\"":
                        reminders[i].message = reminders[i].message.strip().strip('"\'')
                        print("Set message to", reminders[i].message)
                        context=None
                    

                case "duration":
                    reminders[i].duration = token
                    print("Set duration to", reminders[i].duration)
                    context=None

        if context == "exit":
            root.destroy()
            break 
                    

        converted_duration = convert_duration(reminders[i].duration)
        set_reminder(root, reminders[i].message, converted_duration)
        i+=1
    root.mainloop()

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