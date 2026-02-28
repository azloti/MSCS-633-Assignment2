from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = ChatBot(
            "AssignmentBot",
            storage_adapter="chatterbot.storage.DjangoStorageAdapter",
        )

        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train("chatterbot.corpus.english")

        self.stdout.write("Ready!\n")

        while True:
            try:
                user_input = input("user: ")
            except (KeyboardInterrupt, EOFError):
                self.stdout.write("\nBye!")
                break

            response = bot.get_response(user_input)
            self.stdout.write(f"bot: {response}\n")
