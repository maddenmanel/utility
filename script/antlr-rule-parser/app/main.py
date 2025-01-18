from fastapi import FastAPI
from antlr4 import *
from fastapi.responses import JSONResponse
from generated.RuleParserLexer import RuleParserLexer
from generated.RuleParserParser import RuleParserParser

app = FastAPI()

def parse_rule(rule: str):
    # 创建输入流
    input_stream = InputStream(rule)
    
    # 创建词法分析器和词法分析流
    lexer = RuleParserLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    # 创建解析器并进行解析
    parser = RuleParserParser(token_stream)
    
    # 获取解析树（假设规则的根节点为 start）
    tree = parser.start()  # start 是语法树的根节点
    
    # 提取信息（根据你自己的语法树结构）
    rule_info = extract_rule_info(tree)
    
    return rule_info

def extract_rule_info(tree):
    # 这里假设我们有一个解析树，我们从中提取出相关信息
    # 你需要根据实际的解析树结构来提取具体的信息
    rule_info = {
        "Rule": {
            "Name": "服务费用计算规则",
            "Predefined": extract_predefined_conditions(tree),
            "Conditions": extract_conditions(tree),
            "Action": extract_action(tree)
        }
    }
    return rule_info

def extract_predefined_conditions(tree):
    # 提取预定义的条件（你需要根据解析树的实际结构来编写提取逻辑）
    predefined_conditions = [
        {
            "name": "A属性",
            "type": "服务属性",
            "source": "服务属性列表",
            "conditions": [
                {"field": "A属性", "operator": "is_not_empty", "value": ""},
                {"field": "A属性", "operator": "equals", "value": "xxx"},
                {"field": "A属性", "operator": "equals", "value": "yyy"}
            ],
            "action": {
                "name": "服务费用",
                "value": "A属性",
                "type": "double"
            }
        }
    ]
    return predefined_conditions

def extract_conditions(tree):
    # 提取条件（同样，你需要根据解析树来编写提取逻辑）
    conditions = [
        {"field": "A属性", "operator": "is_not_empty", "value": ""},
        {"field": "A费项", "operator": "is_not_empty", "value": ""}
    ]
    return conditions

def extract_action(tree):
    # 提取动作（同样，你需要根据解析树来编写提取逻辑）
    action = {
        "name": "初始化服务费用",
        "rule_name": "计算服务费",
        "amount": "服务费 * 100"
    }
    return action

@app.post("/parse_rule/")
async def parse_rule_endpoint(rule: str):
    print(f"Received rule: {rule}")
    result = parse_rule(rule)
    print(f"Result: {result}")
    return JSONResponse(content=result)