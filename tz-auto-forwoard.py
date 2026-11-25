# ============================================================
#  SEND BY     : INSTANTWARE 💫
#  DEVELOPER   : INSTANTWARE
#  TELEGRAM    : @InstantWare_dev
#  PROJECT     : TZSMX TELEGRAM AUTO FILE FORWARDER
#  OPEN SOURCE SCRIPT
# ============================================================

import os
import sys
import json
import time
import asyncio
import logging
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

# ================= COLORS =================

C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_RED = "\033[91m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_BLUE = "\033[94m"
C_MAGENTA = "\033[95m"
C_CYAN = "\033[96m"
C_WHITE = "\033[97m"

# ================= CONFIG =================

CONFIG_FILE = "tzsmx_api_config.json"


def get_api_credentials():
    env_api_id = os.getenv("API_ID")
    env_api_hash = os.getenv("API_HASH")

    if (
        env_api_id
        and env_api_id.strip().isdigit()
        and env_api_hash
        and env_api_hash.strip()
    ):
        return int(env_api_id.strip()), env_api_hash.strip()

    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                saved_id = data.get("api_id")
                saved_hash = data.get("api_hash")

                if saved_id and saved_hash:
                    return int(saved_id), str(saved_hash)

        except Exception:
            pass

    print(f"\n{C_MAGENTA}{C_BOLD}" + "=" * 50)
    print("🔐 TZSMX API CREDENTIALS SETUP")
    print("=" * 50 + f"{C_RESET}")

    while True:
        raw_id = input(
            f"{C_YELLOW}{C_BOLD}➡️ Enter API_ID : {C_RESET}"
        ).strip()

        if raw_id.isdigit():
            api_id = int(raw_id)
            break

        print(f"{C_RED}❌ Invalid API_ID! Numbers only.{C_RESET}")

    while True:
        api_hash = input(
            f"{C_YELLOW}{C_BOLD}➡️ Enter API_HASH : {C_RESET}"
        ).strip()

        if api_hash:
            break

        print(f"{C_RED}❌ API_HASH cannot be empty!{C_RESET}")

    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(
                {"api_id": api_id, "api_hash": api_hash},
                f
            )
    except Exception:
        pass

    return api_id, api_hash


API_ID, API_HASH = get_api_credentials()

SESSION_NAME = os.getenv("SESSION_NAME", "my_session")

# ================= LOGGING =================

logging.basicConfig(
    level=logging.INFO,
    format=f"{C_CYAN}%(asctime)s{C_RESET} - "
           f"{C_MAGENTA}%(levelname)s{C_RESET} - %(message)s"
)

logger = logging.getLogger(__name__)

client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH,
    flood_sleep_threshold=60
)

# ================= TELEGRAM LINKS =================

def open_links():
    os.system("xdg-open https://t.me/InstantWare_dev")
    os.system("xdg-open https://t.me/InstantWare_dev")


# ================= LOADING ANIMATION =================

def loading_animation(text="Initializing TZSMX Engine", duration=1.5):

    frames = [
        "⠋", "⠙", "⠹", "⠸", "⠼",
        "⠴", "⠦", "⠧", "⠇", "⠏"
    ]

    end_time = time.time() + duration
    idx = 0

    while time.time() < end_time:

        sys.stdout.write(
            f"\r{C_YELLOW}{C_BOLD}"
            f"{frames[idx % len(frames)]} "
            f"{text}...{C_RESET}"
        )

        sys.stdout.flush()
        idx += 1
        time.sleep(0.08)

    sys.stdout.write(
        f"\r{C_GREEN}{C_BOLD}"
        f"💎 {text} - READY!{C_RESET}\n"
    )

    sys.stdout.flush()


# ================= TZSMX BANNER =================

def show_banner():

    os.system("clear" if os.name != "nt" else "cls")

    tzsmx_art = f"""{C_RED}{C_BOLD}
████████╗███████╗███████╗███╗   ███╗██╗  ██╗
╚══██╔══╝╚══███╔╝██╔════╝████╗ ████║╚██╗██╔╝
   ██║   ███╔╝  ███████╗██╔████╔██║ ╚███╔╝
   ██║  ███╔╝   ╚════██║██║╚██╔╝██║ ██╔██╗
   ██║ ███████╗███████║██║ ╚═╝ ██║██╔╝ ██╗
   ╚═╝ ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝
{C_RESET}"""

    print(tzsmx_art)

    print(
        f"{C_CYAN}{C_BOLD}"
        "========================================================="
        f"{C_RESET}"
    )

    print(
        f"{C_YELLOW}{C_BOLD}"
        "   👑 TELEGRAM AUTO FILE FORWARDER [TZSMX EDITION] 👑"
        f"{C_RESET}"
    )

    print(
        f"{C_CYAN}"
        "---------------------------------------------------------"
        f"{C_RESET}"
    )

    print(
        f"{C_GREEN}{C_BOLD}"
        "   ⚡ DEVELOPER : INSTANTWARE"
        f"{C_RESET}"
    )

    print(
        f"{C_MAGENTA}{C_BOLD}"
        "   📢 Telegram : @InstantWare_dev"
        f"{C_RESET}"
    )

    print(
        f"{C_BLUE}{C_BOLD}"
        "   🔥 Mode     : Old + New Files (Anti-Ban Fast)"
        f"{C_RESET}"
    )

    print(
        f"{C_CYAN}{C_BOLD}"
        "========================================================="
        f"{C_RESET}\n"
    )

    loading_animation("Loading TZSMX Cyber Modules", 1.4)

    open_links()


# ================= CHANNEL INPUT =================

def get_channel_input(prompt_text):

    while True:

        raw = input(
            f"{C_YELLOW}{C_BOLD}"
            f"{prompt_text}{C_RESET}"
        ).strip()

        if not raw:
            print(f"{C_RED}❌ Empty input! Try again.{C_RESET}")
            continue

        if raw.lstrip("-").isdigit():
            return int(raw)

        return raw


# ================= RESOLVE CHANNEL =================

async def resolve_channel(entity):

    try:

        channel = await client.get_entity(entity)

        title = getattr(channel, "title", str(entity))

        logger.info(
            f"{C_GREEN}✅ Resolved: {C_BOLD}"
            f"{title}{C_RESET} "
            f"{C_CYAN}(ID: {channel.id}){C_RESET}"
        )

        return channel

    except Exception as e:

        logger.error(
            f"{C_RED}❌ Cannot resolve {entity}: {e}{C_RESET}"
        )

        return None


# ================= LIVE FILE FORWARDER =================

async def forward_handler(event, destination):

    try:

        message = event.message

        if not (
            message.document
            or message.video
            or message.audio
            or message.photo
            or message.voice
        ):
            return

        await client.forward_messages(
            entity=destination,
            messages=message,
            from_peer=event.chat_id
        )

        file_name = (
            message.file.name
            if message.file and message.file.name
            else "File"
        )

        logger.info(
            f"{C_GREEN}⚡ LIVE FORWARDED: "
            f"{C_BOLD}{file_name}{C_RESET} "
            f"{C_YELLOW}(ID: {message.id}){C_RESET}"
        )

        await asyncio.sleep(1)

    except Exception as e:

        logger.error(
            f"{C_RED}❌ Live forward failed: {e}{C_RESET}"
        )


# ================= OLD FILE FORWARDER =================

async def backfill_old_files(source, destination):

    loading_animation(
        "Scanning & Forwarding Old Files",
        1.2
    )

    count = 0
    batch_messages = []
    BATCH_SIZE = 5

    async for message in client.iter_messages(
        source,
        reverse=True
    ):

        if (
            message.document
            or message.video
            or message.audio
            or message.photo
            or message.voice
        ):

            batch_messages.append(message.id)

            if len(batch_messages) >= BATCH_SIZE:

                try:

                    await client.forward_messages(
                        entity=destination,
                        messages=batch_messages,
                        from_peer=source
                    )

                    count += len(batch_messages)

                    logger.info(
                        f"{C_CYAN}📦 TZSMX BATCH SENT: "
                        f"{C_BOLD}{count}{C_RESET} "
                        f"{C_GREEN}files forwarded safely...{C_RESET}"
                    )

                    batch_messages = []

                    await asyncio.sleep(1.5)

                except Exception as e:

                    logger.error(
                        f"{C_RED}❌ Batch forward error: {e}{C_RESET}"
                    )

                    await asyncio.sleep(5)
                    batch_messages = []

    if batch_messages:

        try:

            await client.forward_messages(
                entity=destination,
                messages=batch_messages,
                from_peer=source
            )

            count += len(batch_messages)

        except Exception as e:

            logger.error(
                f"{C_RED}❌ Final batch error: {e}{C_RESET}"
            )

    logger.info(
        f"{C_GREEN}{C_BOLD}"
        f"👑 All {count} OLD files sent successfully!"
        f"{C_RESET}"
    )


# ================= MAIN FUNCTION =================

async def main():

    show_banner()

    await client.start()

    me = await client.get_me()

    logger.info(
        f"{C_GREEN}🚀 Logged in as: "
        f"{C_BOLD}{me.first_name}{C_RESET} "
        f"{C_CYAN}(@{me.username}){C_RESET}"
    )

    print(f"\n{C_MAGENTA}{C_BOLD}" + "=" * 50)
    print("📥 TZSMX CHANNEL SETUP")
    print("=" * 50 + f"{C_RESET}")

    source_input = get_channel_input(
        "➡️ Enter SOURCE channel ID : "
    )

    dest_input = get_channel_input(
        "➡️ Enter DESTINATION channel ID : "
    )

    if source_input == dest_input:

        logger.error(
            f"{C_RED}❌ Source and Destination cannot be the same!{C_RESET}"
        )

        return

    loading_animation("Resolving Channels", 1.0)

    source = await resolve_channel(source_input)
    destination = await resolve_channel(dest_input)

    if not source or not destination:

        logger.error(
            f"{C_RED}❌ Channel resolve failed. "
            f"Make sure you joined both channels.{C_RESET}"
        )

        return

    print(f"\n{C_CYAN}{C_BOLD}" + "=" * 50)

    print(
        f"📥 Source      : "
        f"{C_GREEN}{source.title}{C_CYAN}"
    )

    print(
        f"📤 Destination : "
        f"{C_YELLOW}{destination.title}{C_CYAN}"
    )

    print("=" * 50 + f"{C_RESET}")

    confirm = input(
        f"\n{C_GREEN}{C_BOLD}"
        "▶️ Start TZSMX Forwarding (Old + New)? (y/n): "
        f"{C_RESET}"
    ).strip().lower()

    if confirm != "y":

        logger.info(
            f"{C_YELLOW}⚠️ Cancelled by user.{C_RESET}"
        )

        return

    client.add_event_handler(
        lambda event: forward_handler(event, destination),
        events.NewMessage(chats=source)
    )

    await backfill_old_files(source, destination)

    logger.info(
        f"{C_GREEN}{C_BOLD}"
        "👀 Old files done. Now listening for NEW files... "
        "(Ctrl+C to stop)"
        f"{C_RESET}"
    )

    await client.run_until_disconnected()


# ================= START SCRIPT =================

if __name__ == "__main__":

    try:

        with client:
            client.loop.run_until_complete(main())

    except KeyboardInterrupt:

        print(
            f"\n{C_RED}{C_BOLD}"
            "👋 Stopped by user."
            f"{C_RESET}"
        )