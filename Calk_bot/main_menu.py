from Bot_comand import *

updater = Updater('5619947590:AAFUKycHv5j8O9ZEkdLkrzl_-aGE7wcNJVg')

updater.dispatcher.add_handler(CommandHandler('start', hi_command))
updater.dispatcher.add_handler(CommandHandler('1', sum_command))
updater.dispatcher.add_handler(CommandHandler('2', sub_command))
updater.dispatcher.add_handler(CommandHandler('3', mult_command))
updater.dispatcher.add_handler(CommandHandler('4', div_command))
updater.dispatcher.add_handler(CommandHandler('0', ret_command))

updater.start_polling()
updater.idle()