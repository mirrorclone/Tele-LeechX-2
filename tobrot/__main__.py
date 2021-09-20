#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52 | @MysterySD 

import io
import logging
import os
import sys
import traceback

from pyrogram import Client, filters, idle
from pyrogram.raw import functions, types
from pyrogram.handlers import CallbackQueryHandler, MessageHandler

from tobrot import app, bot, dispatcher 
from tobrot import (
    AUTH_CHANNEL,
    CANCEL_COMMAND_G,
    CLEAR_THUMBNAIL,
    CLONE_COMMAND_G,
    DOWNLOAD_LOCATION,
    GET_SIZE_G,
    GLEECH_COMMAND,
    GLEECH_UNZIP_COMMAND,
    GLEECH_ZIP_COMMAND,
    LEECH_COMMAND,
    LEECH_UNZIP_COMMAND,
    LEECH_ZIP_COMMAND,
    LOG_COMMAND,
    LOGGER,
    PYTDL_COMMAND,
    RENEWME_COMMAND,
    RENAME_COMMAND,
    SAVE_THUMBNAIL,
    STATUS_COMMAND,
    TELEGRAM_LEECH_UNZIP_COMMAND,
    TELEGRAM_LEECH_COMMAND,
    UPLOAD_COMMAND,
    YTDL_COMMAND,
    GYTDL_COMMAND,
    GPYTDL_COMMAND,
    TOGGLE_VID,
    RCLONE_COMMAND,
    TOGGLE_DOC,
    HELP_COMMAND,
    SPEEDTEST,
    TSEARCH_COMMAND
)
from tobrot.helper_funcs.download import down_load_media_f
from tobrot.plugins.call_back_button_handler import button
# the logging things
from tobrot.plugins.torrent_search import searchhelp, sendMessage
from tobrot.helper_funcs.bot_commands import BotCommands
from tobrot.plugins.choose_rclone_config import rclone_command_f
from tobrot.plugins.custom_thumbnail import clear_thumb_nail, save_thumb_nail
from tobrot.plugins.incoming_message_fn import (g_clonee, g_yt_playlist,
                                                incoming_message_f,
                                                incoming_purge_message_f,
                                                incoming_youtube_dl_f,
                                                rename_tg_file)
from tobrot.plugins.new_join_fn import help_message_f, new_join_f
from tobrot.plugins.speedtest import get_speed
from tobrot.plugins.rclone_size import check_size_g, g_clearme
from tobrot.plugins.status_message_fn import (
    cancel_message_f,
    eval_message_f,
    exec_message_f,
    status_message_f,
    upload_document_f,
    upload_log_file,
    upload_as_doc,
    upload_as_video
)

botcmds = [
        (f'{BotCommands.LeechCommand}','📨 [Reply] Leech any Torrent/ Magnet/ Direct Link '),
        (f'{BotCommands.ExtractCommand}', '🔐 Unarchive items . .'),
        (f'{BotCommands.ArchiveCommand}','🗜 Archive as .tar.gz acrhive... '),
        (f'{BotCommands.ToggleDocCommand}','📂 Toggle to Document Upload '),
        (f'{BotCommands.ToggleVidCommand}','🎞 Toggle to Streamable Upload '),
        (f'{BotCommands.SaveCommand}','🖼 Save Thumbnail For Uploads'),
        (f'{BotCommands.ClearCommand}','🕹 Clear Thumbnail '),
        (f'{BotCommands.RenameCommand}','♻️ [Reply] Rename Telegram File '),
        (f'{BotCommands.StatusCommand}','🖲 Show Bot stats and concurrent Downloads'),
        (f'{BotCommands.SpeedCommand}','📡 Get Current Server Speed of Your Bot'),
        (f'{BotCommands.YtdlCommand}','🧲 [Reply] YT-DL Links for Uploading...'),
        (f'{BotCommands.PytdlCommand}','🧧 [Reply] YT-DL Playlists Links for Uploading...'),
        (f'{BotCommands.HelpCommand}','🆘 Get Help, How to Use and What to Do. . .'),
        (f'{BotCommands.LogCommand}','🔀 Get the Bot Log [Owner Only]'),
        (f'{BotCommands.TsHelpCommand}','🌐 Get help for Torrent Search Module'),
    ]

if __name__ == "__main__":
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    bot.set_my_commands(botcmds)

    #now=datetime.now(pytz.timezone('Asia/Kolkata'))
    #current = now.strftime('%Y/%m/%d %I:%M:%P')
    LOG_GROUP = -1001280533370
    dispatcher.bot.sendMessage(f'{LOG_GROUP}', f"Bot is Successfully Restarted By Heroku !! ")

    # Starting The Bot
    app.start()
    dispatcher.bot.sendMessage(1978774817, f"Bot is Successfully Restarted By Heroku !! ")
    ##############################################################################
    incoming_message_handler = MessageHandler(
        incoming_message_f,
        filters=filters.command(
            [
                f"{LEECH_COMMAND}", f"{LEECH_COMMAND}@{bot.username}",
                LEECH_ZIP_COMMAND, f"{LEECH_ZIP_COMMAND}@{bot.username}",
                LEECH_UNZIP_COMMAND, f"{LEECH_UNZIP_COMMAND}@{bot.username}",
                GLEECH_COMMAND,
                GLEECH_UNZIP_COMMAND,
                GLEECH_ZIP_COMMAND,
            ]
        )
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_message_handler)
    ##############################################################################
    incoming_telegram_download_handler = MessageHandler(
        down_load_media_f,
        filters=filters.command([TELEGRAM_LEECH_COMMAND, TELEGRAM_LEECH_UNZIP_COMMAND])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_telegram_download_handler)
    ##############################################################################
    incoming_purge_message_handler = MessageHandler(
        incoming_purge_message_f,
        filters=filters.command(["purge"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_purge_message_handler)
    ##############################################################################
    incoming_clone_handler = MessageHandler(
        g_clonee,
        filters=filters.command([f"{CLONE_COMMAND_G}", f"{CLONE_COMMAND_G}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_clone_handler)
    ##############################################################################
    incoming_size_checker_handler = MessageHandler(
        check_size_g,
        filters=filters.command([f"{GET_SIZE_G}"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_size_checker_handler)
    ##############################################################################
    incoming_g_clear_handler = MessageHandler(
        g_clearme,
        filters=filters.command([f"{RENEWME_COMMAND}", f"{RENEWME_COMMAND}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_g_clear_handler)
    ##############################################################################
    incoming_youtube_dl_handler = MessageHandler(
        incoming_youtube_dl_f,
        filters=filters.command([f"{YTDL_COMMAND}", f"{YTDL_COMMAND}@{bot.username}", f"{GYTDL_COMMAND}", f"{GYTDL_COMMAND}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_youtube_dl_handler)
    ##############################################################################
    incoming_youtube_playlist_dl_handler = MessageHandler(
        g_yt_playlist,
        filters=filters.command([f"{PYTDL_COMMAND}", f"{PYTDL_COMMAND}@{bot.username}", GPYTDL_COMMAND])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_youtube_playlist_dl_handler)
    ##############################################################################
    status_message_handler = MessageHandler(
        status_message_f,
        filters=filters.command([f"{STATUS_COMMAND}", f"{STATUS_COMMAND}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(status_message_handler)
    ##############################################################################
    cancel_message_handler = MessageHandler(
        cancel_message_f,
        filters=filters.command([f"{CANCEL_COMMAND_G}", f"{CANCEL_COMMAND_G}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(cancel_message_handler)
    ##############################################################################
    exec_message_handler = MessageHandler(
        exec_message_f,
        filters=filters.command(["exec"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(exec_message_handler)
    ##############################################################################
    eval_message_handler = MessageHandler(
        eval_message_f,
        filters=filters.command(["eval"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(eval_message_handler)
    ##############################################################################
    rename_message_handler = MessageHandler(
        rename_tg_file,
        filters=filters.command([f"{RENAME_COMMAND}", f"{RENAME_COMMAND}@{bot.username}"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(rename_message_handler)
    ##############################################################################
    upload_document_handler = MessageHandler(
        upload_document_f,
        filters=filters.command([f"{UPLOAD_COMMAND}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(upload_document_handler)
    ##############################################################################
    upload_log_handler = MessageHandler(
        upload_log_file,
        filters=filters.command([f"{LOG_COMMAND}", f"{LOG_COMMAND}@{bot.username}"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(upload_log_handler)
    ##############################################################################
    help_text_handler = MessageHandler(
        help_message_f,
        filters=filters.command([f"{HELP_COMMAND}", f"{HELP_COMMAND}@{bot.username}"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(help_text_handler)
    ##############################################################################
    new_join_handler = MessageHandler(
        new_join_f, filters=~filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(new_join_handler)
    ##############################################################################
    '''
    group_new_join_handler = MessageHandler(
        help_message_f,
        filters=filters.chat(chats=AUTH_CHANNEL) & filters.new_chat_members,
    )
    app.add_handler(group_new_join_handler)
    '''
    ##############################################################################
    call_back_button_handler = CallbackQueryHandler(button)
    app.add_handler(call_back_button_handler)
    ##############################################################################
    save_thumb_nail_handler = MessageHandler(
        save_thumb_nail,
        filters=filters.command([f"{SAVE_THUMBNAIL}", f"{SAVE_THUMBNAIL}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(save_thumb_nail_handler)
    ##############################################################################
    clear_thumb_nail_handler = MessageHandler(
        clear_thumb_nail,
        filters=filters.command([f"{CLEAR_THUMBNAIL}", f"{CLEAR_THUMBNAIL}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(clear_thumb_nail_handler)
    ##############################################################################
    rclone_config_handler = MessageHandler(
        rclone_command_f, filters=filters.command([f"{RCLONE_COMMAND}"])
    )
    app.add_handler(rclone_config_handler)
    ##############################################################################
    upload_as_doc_handler = MessageHandler(
        upload_as_doc,
        filters=filters.command([f"{TOGGLE_DOC}", f"{TOGGLE_DOC}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(upload_as_doc_handler)
    ##############################################################################
    upload_as_video_handler = MessageHandler(
        upload_as_video,
        filters=filters.command([f"{TOGGLE_VID}", f"{TOGGLE_VID}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(upload_as_video_handler)
    ##############################################################################
    get_speed_handler = MessageHandler(
        get_speed,
        filters=filters.command([f"{SPEEDTEST}", f"{SPEEDTEST}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(get_speed_handler)
    ##############################################################################
    searchhelp_handler = MessageHandler(
        searchhelp,
        filters=filters.command([f"{TSEARCH_COMMAND}", f"{TSEARCH_COMMAND}@{bot.username}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(searchhelp_handler)
    ##############################################################################


    logging.info(f"@{(app.get_me()).username} Has Started Running...🏃💨💨")
    
    idle()
    
    app.stop()
