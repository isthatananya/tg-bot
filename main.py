from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

with open('token.txt', 'r') as f:
    TOKEN = f.read().strip()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! type /help to get started")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
The following commands are available:

/start   -> Welcome Message
/help    -> This Message
/content -> basic shit
/contact -> uwu
""")

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("i luv coffee and pizza")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("sus")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("content", content))
app.add_handler(CommandHandler("contact", contact))

app.run_polling()


