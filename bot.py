import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8033917249:AAFp_s3kjPB2vqW2AlMdS17M1OBNY2o_CVU"
PROFILE_BASE = os.path.join(os.getcwd(), "profiles")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 សួស្ដី! ប្រើ /newprofile <ឈ្មោះ> ដើម្បីបង្កើត Chrome Profile")

async def new_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("❗ Usage: /newprofile <profile_name>")
        return

    profile_name = context.args[0]
    profile_path = os.path.join(PROFILE_BASE, profile_name)

    try:
        os.makedirs(profile_path, exist_ok=True)
        await update.message.reply_text(f"✅ Profile '{profile_name}' created successfully.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("newprofile", new_profile))
app.run_polling()
