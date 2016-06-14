from Transporbot.views import StartCommandView, HelpCommandView
from telegrambot.handlers import command, unknown_command

urlpatterns = [command('start', StartCommandView.as_command_view()),
           command('help', HelpCommandView.as_command_view()),
           #regex(r'(?P<org>\w+)_(?P<dst>\w+)', AuthorName.as_command_view()),
          ]
