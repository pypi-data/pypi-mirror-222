from pathlib import Path
from loguru import logger
from .utils.settings import set_package, get_package

import nonebot

try:
    driver = nonebot.get_driver()
    set_package("nonebot2")
except ValueError:
    set_package("qqguild")

from .utils.utils import version

import logging
import sys

DEBUG = False
current_dir = Path(__file__).resolve().parent
mode = "scp"
package = get_package()

if package == "nonebot2":
    from .coc.investigator import Investigator
    from .coc.coccards import cards, cache_cards, sa_handler
    from .coc.cocutils import sc, st, at, dam, en, rd0, ra, ti, li, rb, rp

    from .scp.agent import Agent
    from .scp.scpcards import scp_cards, scp_cache_cards
    from .scp.scputils import sra, scp_dam, at as sat

    from .dnd.adventurer import Adventurer
    from .dnd.dndcards import dnd_cards, dnd_cache_cards
    from .dnd.dndutils import dra

    from .utils.decorators import Commands
    from .utils.messages import help_message, version
    from .utils.utils import logger, init, is_super_user, add_super_user, rm_super_user, su_uuid, format_msg, format_str, get_handlers, get_config, modes
    from .utils.handlers import scp_set_handler, scp_show_handler, scp_del_handler, coc_set_handler, coc_show_handler, coc_del_handler, dnd_set_handler, dnd_show_handler, dnd_del_handler
    from .utils.chat import chat

    from nonebot.rule import Rule
    from nonebot.matcher import Matcher
    from nonebot.plugin import on_startswith
    from nonebot.adapters import Bot as Bot
    from nonebot.adapters.onebot.v11 import Bot as V11Bot
    from nonebot.adapters.onebot.v12 import Bot as V12Bot

    if driver._adapters.get("OneBot V12"):
        from nonebot.adapters.onebot.v12 import MessageEvent, GroupMessageEvent
    else:
        from nonebot.adapters.onebot.v11 import MessageEvent, GroupMessageEvent

    testcommand = on_startswith(".test", priority=2, block=True)
    debugcommand = on_startswith(".debug", priority=2, block=True)
    superusercommand = on_startswith(".su", priority=2, block=True)# | on_startswith(".sudo", priority=2, block=True)
    botcommand = on_startswith(".bot", priority=1, block=True)
    coccommand = on_startswith(".coc", priority=1, block=True)
    scpcommand = on_startswith(".scp", priority=1, block=True)
    dndcommand = on_startswith(".dnd", priority=1, block=True)
    showcommand = on_startswith(".show", priority=2, block=True)# | on_startswith(".display", priority=2, block=True)
    setcommand = on_startswith(".set", priority=2, block=True)
    helpcommand = on_startswith(".help", priority=2, block=True)# | on_startswith(".h", priority=2, block=True)
    modecommand = on_startswith(".mode", priority=2, block=True)# | on_startswith(".m", priority=2, block=True)
    stcommand = on_startswith(".sht", priority=2, block=True)
    attackcommand = on_startswith(".at", priority=2, block=True)# | on_startswith(".attack", priority=2, block=True)
    damcommand = on_startswith(".dam", priority=2, block=True)# | on_startswith(".damage", priority=2, block=True)
    encommand = on_startswith(".en", priority=2, block=True)
    racommand = on_startswith(".ra", priority=2, block=True)
    rhcommand = on_startswith(".rh", priority=2, block=True)
    rhacommand = on_startswith(".rha", priority=1, block=True)
    rcommand = on_startswith(".r", priority=3, block=True)
    ticommand = on_startswith(".ti", priority=2, block=True)
    licommand = on_startswith(".li", priority=2, block=True)
    sccommand = on_startswith(".sc", priority=2, block=True)
    sacommand = on_startswith(".sa", priority=2, block=True)
    delcommand = on_startswith(".del", priority=2, block=True)# | on_startswith(".delete", priority=2, block=True)
    chatcommand = on_startswith(".chat", priority=2, block=True)
    versioncommand = on_startswith(".version", priority=2, block=True)# | on_startswith(".v", priority=2, block=True)

    @driver.on_startup
    async def _():
        global DEBUG
        logger.info("欧若可骰娘初始化中...")
        if DEBUG:
            logging.getLogger().setLevel(logging.DEBUG)
            logger.remove()
            logger.add(
                sys.stdout,
                level = "DEBUG"
            )
            logger.info("DEBUG 模式已启动.")
        cards.load()
        scp_cards.load()
        logger.success("欧若可骰娘初始化完毕.")

    def is_group_message() -> Rule:
        async def _is_group_message(bot: Bot, event: MessageEvent) -> bool:
            return True if type(event) is GroupMessageEvent else False
        return Rule(_is_group_message)

    @testcommand.handle()
    async def testhandler(matcher: Matcher, event: GroupMessageEvent):
        if not is_super_user(event):
            await matcher.send("[Oracle] 权限不足, 拒绝执行指令.")
            return
        logger.info("发送消息:" + str(event.get_message()))
        logger.info(event.get_message().__repr__())
        msg = format_msg(event.get_message())
        if not msg:
            msg = "[]"
        if msg[-1] == "markdown":
            mp = ""
            await matcher.send(group_id=event.group_id, message=mp)
            return

        await matcher.finish(str(msg))


    @debugcommand.handle()
    async def debughandler(matcher: Matcher, event: GroupMessageEvent):
        global DEBUG
        args = format_msg(event.get_message(), begin=".debug")
        if not is_super_user(event):
            await matcher.send("[Oracle] 权限不足, 拒绝执行指令.")
            return

        if args:
            logger.debug(args)
            if args[0] == "off":
                DEBUG = False
                logging.getLogger().setLevel(logging.INFO)
                logger.remove()
                logger.add(
                    sys.stdout,
                    level = "INFO"
                )
                logger.info("[cocdicer] 输出等级设置为 INFO.")
                await matcher.send("[Oracle] DEBUG 模式已关闭.")
                return
        else:
            DEBUG = True
            logging.getLogger().setLevel(logging.DEBUG)
            logger.remove()
            logger.add(
                sys.stdout,
                level = "INFO"
            )
            logger.info("[cocdicer] 输出等级设置为 DEBUG.")
            await matcher.send("[Oracle] DEBUG 模式已启动.")
            return

        if args[0] == "on":
            DEBUG = True
            logging.getLogger().setLevel(logging.DEBUG)
            logger.remove()
            logger.add(
                sys.stdout,
                level = "INFO"
            )
            logger.info("[cocdicer] 输出等级设置为 DEBUG.")
            await matcher.send("[Oracle] DEBUG 模式已启动.")
        else:
            await matcher.send("[Oracle] 错误, 我无法解析你的指令.")

    @superusercommand.handle()
    async def superuser_handler(matcher: Matcher, event: GroupMessageEvent):
        args = format_str(event.get_message(), begin=(".su", ".sudo"))
        arg = list(filter(None, args.split(" ")))

        if len(arg) >= 1:
            if arg[0].lower() == "exit":
                if not rm_super_user(event):
                    await matcher.send("[Oracle] 你还不是超级管理员, 无法撤销超级管理员身份.")
                    return
                await matcher.send("[Oracle] 你已撤销超级管理员身份.")
                return

        if is_super_user(event):
            await matcher.send("[Oracle] 你已经是超级管理员.")
            return

        if not args:
            logger.critical(f"超级令牌: {su_uuid}")
            await matcher.send("[Oracle] 启动超级管理员鉴权, 鉴权令牌已在控制终端展示.")
        else:
            if not args == su_uuid:
                await matcher.send("[Oracle] 鉴权失败!")
            else:
                add_super_user(event)
                await matcher.send("[Oracle] 你取得了管理员权限.")

    @botcommand.handle()
    async def bothandler(bot: V11Bot, matcher: Matcher, event: GroupMessageEvent):
        args = format_msg(event.get_message(), begin=".bot")
        if not is_super_user(event):
            await matcher.send("[Oracle] 你没有管理员权限, 请先执行`.su`开启权限鉴定.")
            return
        if len(args) == 1:
            if args[0] in ["exit", "out", "leave"]:
                print("退出群聊.")
                await matcher.send("[Oracle] 欧若可离开群聊.")
                await bot.set_group_leave(group_id=event.group_id)
            elif args[0] in ["on", "run", "start"]:
                await matcher.send("[Oracle] 我运行在非 systemd 平台上, 我将保持启动.")
            elif args[0] in ["off", "down", "shutdown"]:
                await matcher.send("[Oracle] 我运行在非 systemd 平台上, 我将保持启动.")
            else:
                await matcher.send("[Oracle] 错误的指令.")
        else:
            await matcher.send(help_message("bot"))

    @coccommand.handle()
    async def cochandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_msg(event.get_message(), begin=".coc")
        if len(args) > 1:
            logger.info("指令错误, 驳回.")
            await matcher.send("[Oracle] 错误: 参数超出预计(1需要 但 %d传入), 指令驳回." % len(args))
            return False

        try:
            if len(args) == 0:
                raise ValueError
            args = int(args[0])
        except ValueError:
            await matcher.send(f'警告: 参数 {args} 不合法, 使用默认值 20 替代.')
            args = 20

        inv = Investigator()
        await matcher.send(inv.age_change(args))

        if 15 <= args and args < 90:
            cache_cards.update(event, inv.__dict__, save=False)
            await matcher.send(str(inv.output()))

    @scpcommand.handle()
    async def scp_handler(matcher: Matcher, event: GroupMessageEvent):
        args = format_msg(event.get_message(), begin=".scp")
        if len(args) > 1:
            logger.info("指令错误, 驳回.")
            await matcher.send("[Oracle] 错误: 参数超出预计(1需要 但 %d传入), 指令驳回." % len(args))
            return

        try:
            if len(args) == 0:
                raise ValueError
            args = int(args[0])
        except ValueError:
            await matcher.send(f'警告: 参数 {args} 不合法, 使用默认值 20 替代.')
            args = 20

        agt = Agent()
        agt.age_check(args)
        agt.init()

        if 15 <= args and args < 90:
            scp_cache_cards.update(event, agt.__dict__, save=False)
            await matcher.send(str(agt.output()))

    @dndcommand.handle()
    async def dnd_handler(matcher: Matcher, event: GroupMessageEvent):
        args = format_msg(event.get_message(), begin=".dnd")
        if len(args) > 1:
            logger.info("指令错误, 驳回.")
            await matcher.send("[Oracle] 错误: 参数超出预计(1需要 但 %d传入), 指令驳回." % len(args))
            return True

        try:
            if len(args) == 0:
                raise ValueError
            args = int(args[0])
        except ValueError:
            await matcher.send(f'警告: 参数 {args} 不合法, 使用默认值 20 替代.')
            args = 20

        adv = Adventurer()
        adv.age_check(args)
        adv.init()
        
        if adv.int[0] <= 8:
            await matcher.send("[Orcale] 很遗憾, 检定新的冒险者智力不足, 弱智是不允许成为冒险者的, 请重新进行车卡检定.")
            return True

        if 15 <= args and args < 90:
            dnd_cache_cards.update(event, adv.__dict__, save=False)
            await matcher.send(str(adv.output()))
        return True

    @showcommand.handle()
    async def showhandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_msg(event.get_message(), begin=(".show", ".display"))
        if not args:
            if mode in modes:
                try:
                    sh = eval(f"{mode}_show_handler(event, args)")
                except:
                    sh = [f"[Oracle] 错误: 执行指令失败, 疑似该模式不存在该指令."]
            else:
                await matcher.send("未知的跑团模式.")
                return True

            for msg in sh:
                await matcher.send(str(msg))
            return True

        if args[0] in modes:
            args.remove(args[0])
            sh = eval(f"{args[0]}_show_handler(event, args)")
        else:
            try:
                sh = eval(f"{mode}_show_handler(event, args)")
            except:
                sh = [f"[Oracle] 错误: 执行指令失败, 疑似该模式不存在该指令."]

        for msg in sh:
            await matcher.send(str(msg))
        return

    @setcommand.handle()
    async def sethandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_msg(event.get_message(), begin=".set")
        try:
            now = mode
            sh = eval(f"{mode}_set_handler(event, args)")
        except:
            sh = [f"[Oracle] 错误: 执行指令失败, 疑似模式 {mode} 不存在该指令."]

        await matcher.send(sh)
        return


    @helpcommand.handle()
    async def rdhelphandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_msg(str(event.get_message()), begin=(".help", ".h"))
        if args:
            arg = args[0]
        else:
            arg = ""
        print(arg)
        await matcher.send(help_message(arg))


    @modecommand.handle()
    async def modehandler(matcher: Matcher, event: GroupMessageEvent):
        global mode
        args = format_msg(event.get_message(), begin=(".mode", ".m"))
        if args:
            if args[0].lower() in modes:
                mode = args[0].lower()
                await matcher.send(f"[Oracle] 已切换到 {mode.upper()} 跑团模式.")
                return True
            else:
                await matcher.send("[Oracle] 未知的跑团模式, 忽略.")
                await matcher.send(help_message("mode"))
                return True
        else:
            await matcher.send(f"[Oracle] 当前的跑团模式为 {mode.upper()}.")

    @stcommand.handle()
    async def stcommandhandler(matcher: Matcher, event: GroupMessageEvent):
        try:
            await matcher.send(st())
        except:
            await matcher.send(help_message("st"))


    @attackcommand.handle()
    async def attackhandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_str(event.get_message(), begin=(".at", ".attack"))
        if mode == "coc":
            await matcher.send(at(args, event))
        elif mode == "scp":
            await matcher.send(sat(args, event))


    @damcommand.handle()
    async def damhandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_msg(event.get_message(), begin=(".dam", ".damage"))
        if mode == "scp":
            sd = scp_dam(args, event)
        elif mode == "coc":
            sd = dam(args, event)
        else:
            await matcher.send("未知的跑团模式.")
            return

        await matcher.send(sd)


    @encommand.handle()
    async def enhandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_str(event.get_message(), begin=".en")
        await matcher.send(en(args, event.get_message()))


    @racommand.handle()
    async def rahandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_msg(event.get_message(), begin=".ra")
        if mode in ["coc", "scp", "dnd"]:
            if mode == "scp":
                await matcher.send(sra(args, event))
            elif mode == "coc":
                await matcher.send(ra(args, event))
            elif mode == "dnd":
                await matcher.send(dra(args, event))
        return

    @rhcommand.handle()
    async def rhhandler(bot: Bot, matcher: Matcher, event: GroupMessageEvent):
        args = format_str(event.get_message(), begin=".rh")
        await matcher.send("[Oracle] 暗骰: 命运的骰子在滚动.")
        await bot.send_private_msg(user_id=event.get_user_id(), message=rd0(args))

    @rhacommand.handle()
    async def rhahandler(bot: Bot, matcher: Matcher, event: GroupMessageEvent):
        args = format_msg(event.get_message(), begin=".rha")
        await matcher.send("[Oracle] 暗骰: 命运的骰子在滚动.")
        await bot.send_private_msg(user_id=event.get_user_id(), message=ra(args, event))

    @rcommand.handle()
    async def rdcommandhandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_str(event.get_message(), begin=".r")
        if not args:
            await matcher.send(rd0(args))
        if args[0] == "b":
            args = args[1:]
            await matcher.send(rb(args))
            return
        if args[0] == "p":
            args = args[1:]
            await matcher.send(rp(args))
            return
        try:
            await matcher.send(rd0(args))
        except:
            await matcher.send(help_message("r"))


    @ticommand.handle()
    async def ticommandhandler(matcher: Matcher, event: GroupMessageEvent):
        try:
            await matcher.send(ti())
        except:
            await matcher.send(help_message("ti"))


    @licommand.handle()
    async def licommandhandler(matcher: Matcher, event: GroupMessageEvent):
        try:
            await matcher.send(li())
        except:
            await matcher.send(help_message("li"))


    @sccommand.handle()
    async def schandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_str(event.get_message(), begin=".sc")
        scrs = sc(args, event)

        if isinstance(scrs, list):
            for scr in scrs:
                await matcher.send(scr)
        else:
            await matcher.send(scrs)


    @sacommand.handle()
    async def sahandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_str(event.get_message(), begin=".sa")
        await matcher.send(sa_handler(event, args))


    @delcommand.handle()
    async def delhandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_str(event, begin=(".del", ".delete"))
        if mode in modes:
            for msg in eval(f"{mode}_del_handler(event, args)"):
                await matcher.send(msg)
        return

    @chatcommand.handle()
    async def chathandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_str(event.get_message(), begin=".chat")
        if not args:
            await matcher.send("[Oracle] 空消息是不被允许的.")
            return
        await matcher.send(chat(args))


    @versioncommand.handle()
    async def versionhandler(matcher: Matcher, event: GroupMessageEvent):
        args = format_str(event.get_message(), begin=(".version", ".v"))
        await matcher.send(f"欧若可骰娘 版本 {version}, 未知访客版权所有.\nCopyright © 2011-2023 Unknown Visitor. All Rights Reserved.")
        return
elif package == "qqguild":
    pass
else:
    logger.critical(f"未知的包模式: {package}!")
    sys.exit()
