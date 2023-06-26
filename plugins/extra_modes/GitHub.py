import logging
import os
import requests
import aiohttp
from pyrogram import Client, filters


mod_name = "Github"


@Client.on_message(filters.command("githubusr"))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("Wrong Syntax 🚫\nTry Like:\n/github Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                caption = f"""Info Of {name}
👤 ᴜsᴇʀɴᴀᴍᴇ: {username}
📑 ʙɪᴏ: {bio}
🔗 ᴘʀᴏғɪʟᴇ ʟɪɴᴋ: [Here]({url})
👥 ᴄᴏᴍᴘᴀɴʏ: {company}
💫 ᴄʀᴇᴀᴛᴇᴅ ᴏɴ: {created_at}
🌝 ʀᴇᴘᴏsɪᴛᴏʀɪᴇs: {repositories}
🍭 ʙʟᴏɢ: {blog}
🗺 ʟᴏᴄᴀᴛɪᴏɴ: {location}
🫰 ғᴏʟʟᴏᴡᴇʀs: {followers}
🤞 ғᴏʟʟᴏᴡɪɴɢ: {following}
"""
            except Exception as e:
                print(str(e))
    await message.reply_photo(photo=avatar_url, caption=caption)

@Client.on_message(filters.command('repo'))
async def git(Kashmira, message):
    pablo = await message.reply_text("Processing...")
    args = message.text.split(None, 1)[1]
    if len(message.command) == 1:
        await pablo.edit("No input found")
        return
    r = requests.get("https://api.github.com/search/repositories", params={"q": args})
    lool = r.json()
    if lool.get("total_count") == 0:
        await pablo.edit("File not found")
        return
    else:
        lol = lool.get("items")
        qw = lol[0]
        txt = f"""
<b>Name :</b> <i>{qw.get("name")}</i>

<b>Full Name :</b> <i>{qw.get("full_name")}</i>

<b>Link :</b> {qw.get("html_url")}

<b>Fork Count :</b> <i>{qw.get("forks_count")}</i>

<b>Open Issues :</b> <i>{qw.get("open_issues")}</i>
"""
        if qw.get("description"):
            txt += f'<b>Description :</b> <code>{qw.get("description")}</code>'

        if qw.get("language"):
            txt += f'<b>Language :</b> <code>{qw.get("language")}</code>'

        if qw.get("size"):
            txt += f'<b>Size :</b> <code>{qw.get("size")}</code>'

        if qw.get("score"):
            txt += f'<b>Score :</b> <code>{qw.get("score")}</code>'

        if qw.get("created_at"):
            txt += f'<b>Created At :</b> <code>{qw.get("created_at")}</code>'

        if qw.get("archived") == True:
            txt += f"<b>This Project is Archived</b>"
        await pablo.edit(txt, disable_web_page_preview=True)
