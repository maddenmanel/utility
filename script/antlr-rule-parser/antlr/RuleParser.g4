grammar RuleParser;

start : predefined_rules EOF;

predefined_rules : '预定义' '指定' ID '为一个' ID '来自(in)' ID '符合条件：' conditions '指定' ID '为' ID '取为属性双精度值;' ;

conditions : condition (condition)* ;

condition : '-' ID '的' ID '是' '#' ID ;

ID : [a-zA-Z0-9_]+ ;
WS : [ \t\r\n]+ -> skip ;