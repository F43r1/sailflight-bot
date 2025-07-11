from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🎟️ PONÉ TU TOKEN ACÁ
BOT_TOKEN = "7937313627:AAE1dMjSFgul25jmyyMHWc4scyjJhfI7kjs"

# 🎭 MENSAJE DE BIENVENIDA
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    welcome_text = f"""🎭 ¡Bienvenida, {user}! El mundo es tu escenario y los vuelos, tus entradas.
Yo soy SailFlight, tu compañero de gira.
Cada noche te soplaré al oído una oferta, y cuando quieras, me pedís más. ¿Lista para despegar?"""

    keyboard = [
        ["🎫 Buscar por destino"],
        ["💰 Buscar por precio"],
        ["📅 Buscar por fechas"],
        ["🎲 Sorpresa total"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# 🎬 MANEJADOR DE MENÚ
async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "destino" in text.lower():
        await update.message.reply_text("🎫 Decime el destino que tenés en mente, estrella.")
    elif "precio" in text.lower():
        await update.message.reply_text("💰 ¿Cuál es tu techo de dólares? Te consigo algo que brille.")
    elif "fechas" in text.lower():
        await update.message.reply_text("📅 Decime las fechas que manejás y veo qué hay en cartelera.")
    elif "sorpresa" in text.lower():
        await update.message.reply_text("🎲 ¡Amárrate el cinturón! Busco algo inesperado y barato.")
    else:
        await update.message.reply_text("🎭 No entendí, ¿querés intentar de nuevo con el menú?")

# 🎯 FUNCIÓN PRINCIPAL
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_menu))

    print("🎉 SailFlight está corriendo...")
    app.run_polling()

if __name__ == "__main__":
    main()
