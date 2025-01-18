# Generated from RuleParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,29,
        8,2,10,2,12,2,32,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,0,0,4,0,
        2,4,6,0,0,38,0,8,1,0,0,0,2,11,1,0,0,0,4,26,1,0,0,0,6,33,1,0,0,0,
        8,9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,5,1,0,0,12,13,5,2,0,
        0,13,14,5,12,0,0,14,15,5,3,0,0,15,16,5,12,0,0,16,17,5,4,0,0,17,18,
        5,12,0,0,18,19,5,5,0,0,19,20,3,4,2,0,20,21,5,2,0,0,21,22,5,12,0,
        0,22,23,5,6,0,0,23,24,5,12,0,0,24,25,5,7,0,0,25,3,1,0,0,0,26,30,
        3,6,3,0,27,29,3,6,3,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,
        30,31,1,0,0,0,31,5,1,0,0,0,32,30,1,0,0,0,33,34,5,8,0,0,34,35,5,12,
        0,0,35,36,5,9,0,0,36,37,5,12,0,0,37,38,5,10,0,0,38,39,5,11,0,0,39,
        40,5,12,0,0,40,7,1,0,0,0,1,30
    ]

class RuleParserParser ( Parser ):

    grammarFileName = "RuleParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u9884\\u5B9A\\u4E49'", "'\\u6307\\u5B9A'", 
                     "'\\u4E3A\\u4E00\\u4E2A'", "'\\u6765\\u81EA(in)'", 
                     "'\\u7B26\\u5408\\u6761\\u4EF6\\uFF1A'", "'\\u4E3A'", 
                     "'\\u53D6\\u4E3A\\u5C5E\\u6027\\u53CC\\u7CBE\\u5EA6\\u503C;'", 
                     "'-'", "'\\u7684'", "'\\u662F'", "'#'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "WS" ]

    RULE_start = 0
    RULE_predefined_rules = 1
    RULE_conditions = 2
    RULE_condition = 3

    ruleNames =  [ "start", "predefined_rules", "conditions", "condition" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predefined_rules(self):
            return self.getTypedRuleContext(RuleParserParser.Predefined_rulesContext,0)


        def EOF(self):
            return self.getToken(RuleParserParser.EOF, 0)

        def getRuleIndex(self):
            return RuleParserParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = RuleParserParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.predefined_rules()
            self.state = 9
            self.match(RuleParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predefined_rulesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RuleParserParser.ID)
            else:
                return self.getToken(RuleParserParser.ID, i)

        def conditions(self):
            return self.getTypedRuleContext(RuleParserParser.ConditionsContext,0)


        def getRuleIndex(self):
            return RuleParserParser.RULE_predefined_rules

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredefined_rules" ):
                listener.enterPredefined_rules(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredefined_rules" ):
                listener.exitPredefined_rules(self)




    def predefined_rules(self):

        localctx = RuleParserParser.Predefined_rulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_predefined_rules)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(RuleParserParser.T__0)
            self.state = 12
            self.match(RuleParserParser.T__1)
            self.state = 13
            self.match(RuleParserParser.ID)
            self.state = 14
            self.match(RuleParserParser.T__2)
            self.state = 15
            self.match(RuleParserParser.ID)
            self.state = 16
            self.match(RuleParserParser.T__3)
            self.state = 17
            self.match(RuleParserParser.ID)
            self.state = 18
            self.match(RuleParserParser.T__4)
            self.state = 19
            self.conditions()
            self.state = 20
            self.match(RuleParserParser.T__1)
            self.state = 21
            self.match(RuleParserParser.ID)
            self.state = 22
            self.match(RuleParserParser.T__5)
            self.state = 23
            self.match(RuleParserParser.ID)
            self.state = 24
            self.match(RuleParserParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RuleParserParser.ConditionContext)
            else:
                return self.getTypedRuleContext(RuleParserParser.ConditionContext,i)


        def getRuleIndex(self):
            return RuleParserParser.RULE_conditions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditions" ):
                listener.enterConditions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditions" ):
                listener.exitConditions(self)




    def conditions(self):

        localctx = RuleParserParser.ConditionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conditions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.condition()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 27
                self.condition()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RuleParserParser.ID)
            else:
                return self.getToken(RuleParserParser.ID, i)

        def getRuleIndex(self):
            return RuleParserParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = RuleParserParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(RuleParserParser.T__7)
            self.state = 34
            self.match(RuleParserParser.ID)
            self.state = 35
            self.match(RuleParserParser.T__8)
            self.state = 36
            self.match(RuleParserParser.ID)
            self.state = 37
            self.match(RuleParserParser.T__9)
            self.state = 38
            self.match(RuleParserParser.T__10)
            self.state = 39
            self.match(RuleParserParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





