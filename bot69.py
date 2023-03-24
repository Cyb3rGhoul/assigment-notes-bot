from pyrogram import Client, filters

# Replace the following with your own bot token
API_ID = 12915780
API_HASH = "fd435050d78fde73cbccf05cba4d02dc"
BOT_TOKEN = "6182579305:AAG46FormdqW5wZ_zKjht8SEF8_38aV5xdA"

# Replace the following with the path to your PDF files
ASSIGNMENTS_FILE = "https://drive.google.com/file/d/10j_jOvT41ga2XaX9VmAD9blfj-K0W2Ed/view"
NOTES_FILE = "https://docs.google.com/document/d/1J5pT21QnjQjc9nF99DvK4SJ07C7OhIly/view"

# Create a Pyrogram client instance
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define a handler function for the /start command
@app.on_message(filters.command("start"))
async def start_command_handler(client, message):
    reply_text = "Welcome to the bot! Here are the available commands:\n\n"
    reply_text += "/assignments - Get the assignments PDF\n"
    reply_text += "/notes - Get the notes PDF"
    await message.reply_text(reply_text)

# Define a handler function for the /assignments command
@app.on_message(filters.command("assignments"))
async def assignments_command_handler(client, message):
    chat_id = message.chat.id
    with open(ASSIGNMENTS_FILE, "rb") as f:
        await app.send_document(chat_id, f)

# Define a handler function for the /notes command
@app.on_message(filters.command("notes"))
async def notes_command_handler(client, message):
    chat_id = message.chat.id
    with open(NOTES_FILE, "rb") as f:
        await app.send_document(chat_id, f)

# Start the Pyrogram client
if __name__ == "_main_":
    app.run()