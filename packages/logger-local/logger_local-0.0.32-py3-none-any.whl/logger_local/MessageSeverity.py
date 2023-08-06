from aenum import Enum, NoAlias


class MessageSeverity(Enum, settings=NoAlias):
    Debug = 100
    Verbose = 200
    Init = 300
    Start = 400
    End = 400
    Information = 500
    Critical = 600
    Warning = 700
    Error = 800
    Exception = 900
