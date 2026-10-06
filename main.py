from gui import set_reminder

import tkinter as tk



class Reminder:
    reminder_types = {"remind", "repeat"}

    def __init__(self) -> None:
        self.type = None
        self.duration = None
        self.message = "" # Empty messages are allowed


    def set_reminder_type(self, reminder_type: str):
        if reminder_type not in self.reminder_types:
            raise ValueError(f"Invalid reminder type: {reminder_type}")
        self.type = reminder_type


    def set_reminder_message(self, message: str):
        self.message = message

    def set_reminder_duration(self, duration: int):
        self.duration = duration

    def validate_reminder(self):
        if self.duration is None:
            raise ValueError("Unspecified reminder duration. Use 'in' tag to specify the duration of reminder.\nUsage: 'in <duration>' Example: remind for \"Give Tom a massage\" in 5h")

        if self.type is None:
            raise ValueError("Unspecified reminder type. Use 'remind' or 'repeat' tag to specify the duration of reminder.\nEx: 'remind for \"Give Tom a massage\" in 1h'")
    




def tokenizer(input: str) -> list:

    tokens = input.split()

    return tokens



def parser(tokens: list[str], reminder: Reminder) -> str | None:

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

                        reminder.set_reminder_message(message)

                        print("Set message to", reminder.message)

                        context=None



                case "duration":

                    duration = token

                    converted_duration = convert_duration(duration)

                    reminder.set_reminder_duration(converted_duration)

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



def main():

    root = tk.Tk()

    root.withdraw()

    reminders: list[Reminder] = []

    i=0

    while True:

        prompt: str = input("ANVReminder BETA...\nType 'exit' to exit\n")

        if not prompt:

            continue

        if prompt == "exit":

            root.destroy()

            break

        tokens = tokenizer(prompt)

        reminders.append(Reminder())

        action: str | None = parser(tokens, reminders[i])

        try:
            reminders[i].validate_reminder()
            set_reminder(root, reminders[i].message, reminders[i].duration) # type: ignore

        except ValueError as e:
            print("ValueError:", e)


        if action == "exit":

            root.destroy()

            break

            # *TODO make exit not quit the background reminder process*

        

        i+=1

    root.mainloop()



if __name__ == "__main__":

    main()