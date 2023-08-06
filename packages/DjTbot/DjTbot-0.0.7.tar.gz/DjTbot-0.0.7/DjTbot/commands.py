import logging
from .core.commands import Command, HELP, CommandWithArgumentsMixin
from .arguments import TBotArgumentParser
from DjTbot.utils import get_group_members, create_user, addgroup, get_user
from DjTbot.models import TBotUser


logger = logging.getLogger("DjTbot")
# Todo: Refactor with CommandWithArgumentsMixin
# Todo: Delete user
# Todo: Remove user from group


# Todo: Refactor with TBotCommandWithArgumentsMixin
class TBotCommandWithArgumentsMixin(CommandWithArgumentsMixin):
    argument_parser_factory_class = TBotArgumentParser


# Todo: Refactor with TBotCommandWithArgumentsMixin
class HelpCommand(Command):
    command = ['help', 'h']
    help_text = 'Display this help.'
    allowed_groups = ['*']

    def run(self, update, context):
        text = 'Bot help\n'
        for cmd, info in HELP.items():
            if self.is_allowed_command(update, info):
                text += "{cmds}: {description}\n".format(cmds=cmd, description=info['help'])
        context.bot.sendMessage(chat_id=update.message.chat_id, text=text)

    def is_allowed_command(self, update, info):
        user_groups = self.get_user_groups(update)
        for group in user_groups:
            if group in info['groups'] or group == 'Admins':
                return True
        return False


# Todo: Refactor with TBotCommandWithArgumentsMixin
class AddUserCommand(Command):
    command = ['adduser']
    help_text = 'Create new user.'
    usage = '/adduser telegram_id user_name'

    def run(self, update, context):
        try:
            telegram_id = context.args[0]
            user_name = ' '.join(context.args[1:])
            create_user(telegram_id, user_name)
            self.admin_broadcast(context.bot, 'New User Added {} ({})'.format(user_name, telegram_id))
        except Exception as e:
            self.admin_broadcast(context.bot, str(e))
            self.send_ussage(context.bot, update)


# Todo: Refactor with TBotCommandWithArgumentsMixin
class ListUsersCommand(Command):
    command = ['listusers']
    help_text = 'List users.'
    usage = '/listusers'
    allowed_groups = ['*']

    def run(self, update, context):
        try:
            message = ''
            users = TBotUser.objects.all()
            for user in users:
                user_groups = ', '.join(user.groups.all().values_list('name', flat=True))
                message += f'{user.name} ({user.id}) groups: {user_groups}\n'
            # TODO: Text splitter
            context.bot.sendMessage(chat_id=update.message.chat_id, text=message)
        except Exception as e:
            self.admin_broadcast(context.bot, str(e))
            self.send_ussage(context.bot, update)


class AddGroupCommand(TBotCommandWithArgumentsMixin, Command):
    command = ['addgroup']
    help_text = 'Add user to group'
    usage = '/addgroup telegram_id group_name'
    allowed_groups = ['Admins']

    def command_call(self, arguments, update, context):
        try:
            addgroup(arguments.telegram_id, arguments.group)
        except Exception as e:
            self.admin_broadcast(context.bot, str(e))
            self.send_ussage(context.bot, update)
