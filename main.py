from gui import GUI
from parser import parser, tokenizer
from data import Database



class Reminder:
    reminder_types = {"remind", "repeat"}

    def __init__(self, id) -> None:
        self.id = id
        self.type = None
        self.duration = None
        self.message = "" # Empty messages are allowed


    def set_reminder_type(self, reminder_type: str):
        if reminder_type not in self.reminder_types:
            raise ValueError(f"Invalid reminder type: {reminder_type}")
        self.type = reminder_type


    def set_message(self, message: str):
        self.message = message

    def set_duration(self, duration: int):
        self.duration = duration

    def validate(self):
        if self.duration is None:
            raise ValueError("Unspecified reminder duration. Use 'in' tag to specify the duration of reminder.\nUsage: 'in <duration>' Example: remind for \"Give Tom a massage\" in 5h")

        if self.type is None:
            raise ValueError("Unspecified reminder type. Use 'remind' or 'repeat' tag to specify the duration of reminder.\nEx: 'remind for \"Give Tom a massage\" in 1h'")



def main():

    gui = GUI()
    database = Database()

    reminders: list[Reminder] = []

    i=0

    while True:

        prompt: str = input("ANVReminder BETA...\nType 'exit' to exit\n")

        if not prompt:

            continue

        elif prompt == "exit":

            gui.destroy()

            break

        tokens = tokenizer(prompt)

        reminders.append(Reminder(i))

        parser(tokens, reminders[i])

        try:
            reminders[i].validate()
            database.add_reminder(reminders[i].type, reminders[i].message, reminders[i].duration) # type: ignore
            gui.set_reminder(reminders[i].message, reminders[i].duration)

        except ValueError as e:
            print("ValueError:", e)

            # *TODO make exit not quit the background reminder process*

        i+=1

    gui.run()



if __name__ == "__main__":

    main()