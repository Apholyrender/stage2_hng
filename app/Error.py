class Error:
    msg: str
    code: int

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code