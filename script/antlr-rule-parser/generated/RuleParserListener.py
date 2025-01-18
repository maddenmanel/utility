# Generated from RuleParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RuleParserParser import RuleParserParser
else:
    from RuleParserParser import RuleParserParser

# This class defines a complete listener for a parse tree produced by RuleParserParser.
class RuleParserListener(ParseTreeListener):

    # Enter a parse tree produced by RuleParserParser#start.
    def enterStart(self, ctx:RuleParserParser.StartContext):
        pass

    # Exit a parse tree produced by RuleParserParser#start.
    def exitStart(self, ctx:RuleParserParser.StartContext):
        pass


    # Enter a parse tree produced by RuleParserParser#predefined_rules.
    def enterPredefined_rules(self, ctx:RuleParserParser.Predefined_rulesContext):
        pass

    # Exit a parse tree produced by RuleParserParser#predefined_rules.
    def exitPredefined_rules(self, ctx:RuleParserParser.Predefined_rulesContext):
        pass


    # Enter a parse tree produced by RuleParserParser#conditions.
    def enterConditions(self, ctx:RuleParserParser.ConditionsContext):
        pass

    # Exit a parse tree produced by RuleParserParser#conditions.
    def exitConditions(self, ctx:RuleParserParser.ConditionsContext):
        pass


    # Enter a parse tree produced by RuleParserParser#condition.
    def enterCondition(self, ctx:RuleParserParser.ConditionContext):
        pass

    # Exit a parse tree produced by RuleParserParser#condition.
    def exitCondition(self, ctx:RuleParserParser.ConditionContext):
        pass



del RuleParserParser