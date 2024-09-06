import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googleapiclient.discovery import build
from telegram import ParseMode

# Dados do bot
# script async src="https://cse.google.com/cse.js?cx=46baa85e7b33e4b03">
# </script>
# <div class="gcse-search"></div> 
# https://chatgpt.com/share/757e18ec-34aa-4535-a5c6-298823fbb372
BOT_TOKEN = '7445994394:AAEUkcb7dJxDofhTZ6bbwlzP9g6IOTUJ-yY'
API_KEY = 'AIzaSyCUfCjcTx35Hjs4vcAImh_ZvgPSseEsOgc'
SEARCH_ENGINE_ID = '46baa85e7b33e4b03'

# Funções de busca

def buscar_google(query, num_results=5):
    service = build("customsearch", "v1", developerKey=API_KEY)
    try:
        res = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=num_results).execute()
        search_items = res.get("items", [])
    except Exception as e:
        return f"Erro ao buscar resultados: {str(e)}"

    if not search_items:
        return "Nenhum resultado encontrado para sua pesquisa."

    result = "*Aqui estão os resultados mais relevantes:*\n\n"
    for index, item in enumerate(search_items, start=1):
        title = item.get("title")
        link = item.get("link")
        snippet = item.get("snippet")
        result += f"*{index}.* [{title}]({link})\n_{snippet}_\n\n"
    return result

  def start(update, context):
    welcome_message = (
        "Olá! Eu sou o MegaAutobot, estou aqui para ajudá-lo a encontrar informações sobre veículos.\n\n"
        "Use /search para fazer uma pesquisa ou /help para ver todos os comandos disponíveis."
    )
    update.message.reply_text(welcome_message, parse_mode=ParseMode.MARKDOWN)

  def help_command(update, context):
    help_message = (
        "*Comandos disponíveis:*\n\n"
        "/start - Iniciar o bot\n"
        "/help - Ver os comandos disponíveis\n"
        "/about - Saber mais sobre o bot\n"
        "/search [termo] - Fazer uma pesquisa geral\n"
        "/top [termo] - Pesquisar com um número limitado de resultados\n"
        "/search_car [tipo] - Pesquisar por tipos específicos de veículos (ex: 'carro elétrico', 'SUV')"
    )
    update.message.reply_text(help_message, parse_mode=ParseMode.MARKDOWN)

