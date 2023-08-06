import os
import textwrap
from DjTbot.models import TBotUser, TBotGroup
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from telegram.ext import Updater


def get_user(chat_id):
    user = TBotUser.objects.get(chat_id=chat_id)
    return user


def get_user_id(username):
    return TBotUser.objects.get(name=username).id


def get_user_groups(chat_id):
    try:
        return [x for x in TBotUser.objects.get(pk=chat_id).groups.all().values_list('name', flat=True)] + ['*']
    except TBotUser.DoesNotExist:
        return []


def get_group(group_name):
    try:
        return TBotGroup.objects.get(name=group_name)
    except ObjectDoesNotExist:
        return TBotGroup.objects.create(name=group_name)


def create_user(telegram_id, name):
    try:
        return TBotUser.objects.get(id=telegram_id)
    except ObjectDoesNotExist:
        return TBotUser.objects.create(id=telegram_id, name=name)


def get_all_ids():
    return TBotUser.objects.all().values_list('id', flat=True)


def get_group_members(group_name):
    group = get_group(group_name=group_name)
    return group.tbotuser_set.all().values_list('id', flat=True)


def addgroup(telegram_id, group_name):
    user = TBotUser.objects.get(id=telegram_id)
    group = TBotGroup.objects.get(name=group_name)
    user.groups.add(group)


def send_message(telegram_id, message, http_proxy=None):
    if http_proxy:
        updater = Updater(token=settings.API_KEY, use_context=True, request_kwargs={'proxy_url': http_proxy})
    else:
        updater = Updater(token=settings.API_KEY, use_context=True)
    updater.bot.sendMessage(chat_id=telegram_id, text=message)


def split(message, width=4096, break_on_hyphens=False, replace_whitespace=False):
    return textwrap.wrap(message, width=width, break_on_hyphens=break_on_hyphens, replace_whitespace=replace_whitespace)


def setting_or_env(setting, default=None):
    try:
        return getattr(settings, setting)
    except AttributeError:
        try:
            return os.environ[setting]
        except KeyError:
            return default
