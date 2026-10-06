from gui import GUI
from parser import parser, tokenizer
from data import Database



class Reminder:
    reminder_types = {"remind", "repeat"}

    def __init__(self) -> None:
        self.id = id
        self.type = None
        self.duration = None
        self.message = "" # Empty messages are allowed


    def set_reminder_type(self, reminder_type: str):
        if reminder_type not in self.reminder_types:
            raise ValueError(f"Invalid reminder type: {reminder_type}")
        self.type = reminder_type

    def set_id(self, id: int):
            self.id = int

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

    while True:
        reminder = Reminder()

        prompt: str = input("ANVReminder BETA...\nType 'exit' to exit\n")

        if not prompt:

            continue

        elif prompt == "exit":

            gui.destroy()

            break


        tokens = tokenizer(prompt)

        parser(tokens, reminder)

        try:
            reminder.validate()
            reminder.set_id = database.add_reminder(reminder.type, reminder.message, reminder.duration) # type: ignore
            gui.set_reminder(reminder.message, reminder.duration)

        except ValueError as e:
            print("ValueError:", e)

            # *TODO make exit not quit the background reminder process*

    gui.run()



if __name__ == "__main__":

    main()