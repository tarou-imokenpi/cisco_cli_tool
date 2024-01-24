print("loading...")
from rich.markdown import Markdown
from rich.console import Console
from prompt_toolkit import prompt
from RouterCompleter import RouterCompleter
from SubnetCompleter import SubnetCompleter, subnet_mask_chenger
from rich.panel import Panel
import pyperclip
from prompt_toolkit.history import InMemoryHistory
import time

title = """
# Cisco Command AutoComplete Tool
## 使い方
1. コマンドを入力
2. 補完されたコマンドを Tabキーで選択できます。
3. 選択したコマンドをEnterキーで確定します。
4. 現在のコマンドリストが表示されます。
5. 1~4を繰り返します。

**終了するには、コマンド入力時に「cmd exit」と入力します。**
**終了時にコマンドリストがクリップボードにコピーされます。**


"""


def finish(select_list):
    for i in select_list:
        console.print(i, style="bold cyan underline")

    pyperclip.copy("\n".join(select_list) + "\n")

    console.print(
        Markdown(
            "# Copied to the clipboard ! You can paste it.",
            style="bold underline cyan",
        )
    )


def is_selectin_equal():
    try:
        if selection == select_list[-1]:
            return True
        else:
            return False
    except Exception:
        return False


if __name__ == "__main__":
    print("loading...")
    mode_history = InMemoryHistory()
    ip_history = InMemoryHistory()
    mask_history = InMemoryHistory()
    console = Console()
    tmp = ""
    count = 0
    select_list = []
    console.print(Markdown(title, style="bold underline green italic"))
    while True:
        # ユーザーに選択肢を表示し、選択を取得
        selection = prompt(
            "Please select a command: ",
            completer=RouterCompleter(),
            complete_in_thread=True,
            history=mode_history,
        )

        if is_selectin_equal():
            console.print("このコマンドは１つ前に入力されたコマンドと同じです。", style="bold RED")
            continue

        if selection == "" or selection == " ":
            continue
        elif selection == "cmd exit":
            finish(select_list)
            break
        elif selection == "cmd delete last command":
            try:
                console.print(f"DEL OK {select_list.pop()}", style="bold GREEN")
                tmp = tmp.split("\n")[:-2]
                tmp = "\n".join(tmp) + "\n"
                count -= 1
                select_command = Panel(tmp, title="Command list", expand=True)
                console.print(select_command)
            except IndexError:
                console.print("No command selected!")
            continue
        elif selection == "ip address [ip] [mask]":
            ip = prompt(
                "Please input IP address: ",
                complete_in_thread=True,
                history=ip_history,
            )
            mask = prompt(
                "Please input subnet mask: ",
                completer=SubnetCompleter(),
                complete_in_thread=True,
                history=mask_history,
            )
            mask = subnet_mask_chenger(mask)

            selection = selection.replace("[ip]", ip)
            selection = selection.replace("[mask]", mask)

        elif selection == "hostname [hostname]":
            hostname = prompt(
                "Please input hostname: ",
                complete_in_thread=True,
            )
            selection = selection.replace("[hostname]", hostname)

        select_list.append(selection)
        count += 1
        tmp += f"line[{count}] : {selection}\n"
        # 選択を表示
        select_command = Panel(tmp, title="Command list", expand=True)
        console.print(select_command)

    time.sleep(3)
