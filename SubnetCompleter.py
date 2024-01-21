from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.completion import Completion


class SubnetCompleter(Completer):
    def get_completions(self, document, _):
        commands = {
            "/8": "255.0.0.0 MAX[16,777,216]",
            "/9": "255.128.0.0 MAX[8,388,608]",
            "/10": "255.192.0.0 MAX[4,194,304]",
            "/11": "255.224.0.0 MAX[2,097,152]",
            "/12": "255.240.0.0 MAX[1,048,576]",
            "/13": "255.248.0.0 MAX[524,288]",
            "/14": "255.252.0.0 MAX[262,144]",
            "/15": "255.254.0.0 MAX[131,072]",
            "/16": "255.255.0.0 MAX[65,536]",
            "/17": "255.255.128.0 MAX[32,768]",
            "/18": "255.255.192.0 MAX[16,384]",
            "/19": "255.255.224.0 MAX[8,192]",
            "/20": "255.255.240.0 MAX[4,096]",
            "/21": "255.255.248.0 MAX[2,048]",
            "/22": "255.255.252.0 MAX[1,024]",
            "/23": "255.255.254.0 MAX[512]",
            "/24": "255.255.255.0 MAX[256]",
            "/25": "255.255.255.128 MAX[128]",
            "/26": "255.255.255.192 MAX[64]",
            "/27": "255.255.255.224 MAX[32]",
            "/28": "255.255.255.240 MAX[16]",
            "/29": "255.255.255.248 MAX[8]",
            "/30": "255.255.255.252 MAX[4]",
            "/31": "255.255.255.254 MAX[2]",
            "/32": "255.255.255.255 MAX[1]",
            "255.0.0.0": "/8 MAX[16,777,216]",
            "255.128.0.0": "/9 MAX[8,388,608]",
            "255.192.0.0": "/10 MAX[4,194,304]",
            "255.224.0.0": "/11 MAX[2,097,152]",
            "255.240.0.0": "/12 MAX[1,048,576]",
            "255.248.0.0": "/13 MAX[524,288]",
            "255.252.0.0": "/14 MAX[262,144]",
            "255.254.0.0": "/15 MAX[131,072]",
            "255.255.0.0": "/16 MAX[65,536]",
            "255.255.128.0": "/17 MAX[32,768]",
            "255.255.192.0": "/18 MAX[16,384]",
            "255.255.224.0": "/19 MAX[8,192]",
            "255.255.240.0": "/20 MAX[4,096]",
            "255.255.248.0": "/21 MAX[2,048]",
            "255.255.252.0": "/22 MAX[1,024]",
            "255.255.254.0": "/23 MAX[512]",
            "255.255.255.0": "/24 MAX[256]",
            "255.255.255.128": "/25 MAX[128]",
            "255.255.255.192": "/26 MAX[64]",
            "255.255.255.224": "/27 MAX[32]",
            "255.255.255.240": "/28 MAX[16]",
            "255.255.255.248": "/29 MAX[8]",
            "255.255.255.252": "/30 MAX[4]",
            "255.255.255.254": "/31 MAX[2]",
            "255.255.255.255": "/32 MAX[1]",
        }

        word = document.text_before_cursor.lstrip()
        for command, description in commands.items():
            if command.startswith(word):
                yield Completion(command, -len(word), display_meta=description)


def subnet_mask_chenger(mask):
    commands = {
        "/8": "",
        "/9": "255.128.0.0",
        "/10": "255.192.0.0",
        "/11": "255.224.0.0",
        "/12": "255.240.0.0",
        "/13": "255.248.0.0",
        "/14": "255.252.0.0",
        "/15": "255.254.0.0",
        "/16": "255.255.0.0",
        "/17": "255.255.128.0",
        "/18": "255.255.192.0",
        "/19": "255.255.224.0",
        "/20": "255.255.240.0",
        "/21": "255.255.248.0",
        "/22": "255.255.252.0",
        "/23": "255.255.254.0",
        "/24": "255.255.255.0",
        "/25": "255.255.255.128",
        "/26": "255.255.255.192",
        "/27": "255.255.255.224",
        "/28": "255.255.255.240",
        "/29": "255.255.255.248",
        "/30": "255.255.255.252",
        "/31": "255.255.255.254",
        "/32": "255.255.255.255",
    }

    return commands.get(mask, mask)
