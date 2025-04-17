from telegram.ext import Application, CommandHandler, MessageHandler, filters

# 定义 /start 命令的处理函数
async def start(update, context):
    await update.message.reply_text("欢迎使用我的机器人！发送 /help 查看帮助。")

# 定义 /help 命令的处理函数
async def help_command(update, context):
    await update.message.reply_text("可用命令：\n/start - 开始使用\n/help - 查看帮助")

# 定义处理普通消息的函数
async def echo(update, context):
    await update.message.reply_text(f"你说了：{update.message.text}")

def main():
    # 替换为你的机器人 API 令牌
    token = ":"
    
    # 创建应用实例
    app = Application.builder().token(token).build()
    
    # 注册命令处理器
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    # 注册消息处理器（非命令消息）
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # 启动机器人
    print("机器人已启动...")
    app.run_polling()

if __name__ == "__main__":
    main()
