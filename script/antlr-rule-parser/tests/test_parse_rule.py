import unittest
from app.main import parse_rule

rule = """
A属性 is not empty
A属性 equals xxx
A属性 equals yyy
"""

expected_response = {
    "Rule": {
        "Name": "服务费用计算规则",
        "Predefined": [
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
        ],
        "Conditions": [
            {"field": "A属性", "operator": "is_not_empty", "value": ""},
            {"field": "A费项", "operator": "is_not_empty", "value": ""}
        ],
        "Action": {
            "name": "初始化服务费用",
            "rule_name": "计算服务费",
            "amount": "服务费 * 100"
        }
    }
}

class TestParseRule(unittest.TestCase):

    def test_parse_rule(self):
        print("Testing parse_rule \n" + rule)
        print("Expected response: \n" + str(expected_response))
        result = parse_rule(rule)
        print(f"The fact result:\n {result}")
        self.assertEqual(result, expected_response, f"Expected {expected_response} but got {result}")

if __name__ == '__main__':
    unittest.main()