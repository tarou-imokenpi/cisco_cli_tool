from prompt_toolkit.completion import Completer, Completion


class RouterCompleter(Completer):
    def get_completions(self, document, _):
        commands = {
            "cmd exit": "CLIツールを終了する",
            "cmd delete last command": "最後に入力されたコマンドをリストから削除する",
            "enable": "特権モードへ移動する",
            "enable password": "特権パスワードを設定する",
            "enable secret": "特権パスワードを暗号化する",
            "show running-config": "設定を表示する",
            "show startup-config": "起動設定を表示する",
            "show version": "バージョン情報を表示する",
            "copy running-config startup-config": "設定を保存する",
            "show ip route": "ルーティングテーブルを表示する",
            "show clock": "時刻を表示する",
            "show version": "バージョン情報を表示する",
            "show logging": "ログを表示する",
            "show arp": "ARPテーブルを表示する",
            "dir flash:": "フラッシュメモリの内容を表示する",
            "show environment": "ルータの置かれた環境を表示",
            "show processes cpu": "各プロセスのcpu使用率を表示",
            "show processes memory": "各プロセスのメモリを表示",
            "show diagnostic status": "モジュール情報を表示",
            "show tech support": "ルータのシステム情報を表示",
            "show cdp neighbors": "CDPを利用して隣接ルータの情報を確認",
            "show interfaces": "インターフェースの状態を表示",
            "show ip interface brief": "インターフェイスの状態をシンプルに表示",
            "show history": "コマンド履歴を表示",
            "no shutdown": "インターフェイスを有効化",
            "configure terminal": "グローバルコンフィグレーションモードへ移動",
            "reload": "ルータを再起動する",
            "ip nat inside source ": "NATの設定",
            "router rip": "リップを設定する",
            "version 2": "RIPv2を設定する",
            "clear ip route ＊": "ルーティングテーブルをクリアする",
            "no cdp run": "CDPを無効化する",
            "ip address [ip] [mask]": "インターフェイスにIPアドレスを設定する",
            "hostname [hostname]": "ホスト名を設定する",
        }

        word = document.text_before_cursor.lstrip()
        for command, description in commands.items():
            if command.startswith(word):
                yield Completion(command, -len(word), display_meta=description)
