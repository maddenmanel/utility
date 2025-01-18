# Generated from RuleParser.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,83,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,4,11,73,8,11,
        11,11,12,11,74,1,12,4,12,78,8,12,11,12,12,12,79,1,12,1,12,0,0,13,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        1,0,2,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,84,0,1,1,
        0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,
        0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,
        0,0,23,1,0,0,0,0,25,1,0,0,0,1,27,1,0,0,0,3,31,1,0,0,0,5,34,1,0,0,
        0,7,38,1,0,0,0,9,45,1,0,0,0,11,51,1,0,0,0,13,53,1,0,0,0,15,63,1,
        0,0,0,17,65,1,0,0,0,19,67,1,0,0,0,21,69,1,0,0,0,23,72,1,0,0,0,25,
        77,1,0,0,0,27,28,5,39044,0,0,28,29,5,23450,0,0,29,30,5,20041,0,0,
        30,2,1,0,0,0,31,32,5,25351,0,0,32,33,5,23450,0,0,33,4,1,0,0,0,34,
        35,5,20026,0,0,35,36,5,19968,0,0,36,37,5,20010,0,0,37,6,1,0,0,0,
        38,39,5,26469,0,0,39,40,5,33258,0,0,40,41,5,40,0,0,41,42,5,105,0,
        0,42,43,5,110,0,0,43,44,5,41,0,0,44,8,1,0,0,0,45,46,5,31526,0,0,
        46,47,5,21512,0,0,47,48,5,26465,0,0,48,49,5,20214,0,0,49,50,5,65306,
        0,0,50,10,1,0,0,0,51,52,5,20026,0,0,52,12,1,0,0,0,53,54,5,21462,
        0,0,54,55,5,20026,0,0,55,56,5,23646,0,0,56,57,5,24615,0,0,57,58,
        5,21452,0,0,58,59,5,31934,0,0,59,60,5,24230,0,0,60,61,5,20540,0,
        0,61,62,5,59,0,0,62,14,1,0,0,0,63,64,5,45,0,0,64,16,1,0,0,0,65,66,
        5,30340,0,0,66,18,1,0,0,0,67,68,5,26159,0,0,68,20,1,0,0,0,69,70,
        5,35,0,0,70,22,1,0,0,0,71,73,7,0,0,0,72,71,1,0,0,0,73,74,1,0,0,0,
        74,72,1,0,0,0,74,75,1,0,0,0,75,24,1,0,0,0,76,78,7,1,0,0,77,76,1,
        0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,
        82,6,12,0,0,82,26,1,0,0,0,3,0,74,79,1,6,0,0
    ]

class RuleParserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    ID = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\u9884\\u5B9A\\u4E49'", "'\\u6307\\u5B9A'", "'\\u4E3A\\u4E00\\u4E2A'", 
            "'\\u6765\\u81EA(in)'", "'\\u7B26\\u5408\\u6761\\u4EF6\\uFF1A'", 
            "'\\u4E3A'", "'\\u53D6\\u4E3A\\u5C5E\\u6027\\u53CC\\u7CBE\\u5EA6\\u503C;'", 
            "'-'", "'\\u7684'", "'\\u662F'", "'#'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "ID", "WS" ]

    grammarFileName = "RuleParser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


