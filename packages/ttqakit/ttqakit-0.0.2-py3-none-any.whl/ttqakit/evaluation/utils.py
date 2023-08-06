import json
import re


def extract_single_expression(expression):
    parts = expression.split("(")
    operator = parts[0].strip()
    arguments = parts[1].split(")")[0].split(",")
    arguments = [arg.strip() for arg in arguments]
    return operator, arguments[0], arguments[1]


def program_to_expression(program):
    expressions = program.split("),")
    last_res = ""
    result_history = []
    for expression in expressions:
        op, arg1, arg2 = extract_single_expression(expression)
        if arg1[0] == "#":
            arg1_num = int(arg1[1:])
            arg1 = result_history[arg1_num]
        if arg2[0] == "#":
            arg2_num = int(arg2[1:])
            arg2 = result_history[arg2_num]

        if arg1.startswith("const_"):
            arg1 = arg1[6:]
        if arg2.startswith("const_"):
            arg2 = arg2[6:]

        this_res = ""
        if op == "add":
            this_res = arg1 + "+" + arg2
        elif op == "subtract":
            this_res = arg1 + "-" + arg2
        elif op == "multiply":
            this_res = arg1 + "*" + arg2
        elif op == "divide":
            this_res = arg1 + "/" + arg2
        elif op == "exp":
            this_res = arg1 + "**" + arg2

        last_res = "(" + this_res + ")"
        result_history.append(last_res)
    return last_res


def convert_percent_to_decimal(expression):
    expression = expression.replace("m1", "-1")

    def replace_percent(match):
        percent_number = float(match.group(1))
        return str(percent_number / 100)

    pattern = r"(\d+(\.\d*)?)%"
    result = re.sub(pattern, replace_percent, expression)

    return result


def eval_CompAQt_epression(result_path, gold_key, pred_key):
    same_answer_num = 0
    total_num = {"finqa": 0, "tatqa": 0, "hitab": 0, "multihiertt": 0}
    match_num = {"finqa": 0, "tatqa": 0, "hitab": 0, "multihiertt": 0}
    with open(result_path, 'r') as file:
        for line in file:
            source = data_dict["source"]
            total_num[source] += 1

            data_dict = json.loads(line)
            gold_program = data_dict[gold_key]
            gold_expression = program_to_expression(gold_program)
            pred_expression = data_dict[pred_key]

            if gold_expression == pred_expression:
                match_num[source] += 1

            try:
                gold_ans = eval(convert_percent_to_decimal(gold_expression))
            except:
                pass
            try:
                pred_ans = eval(convert_percent_to_decimal(pred_expression))
            except:
                print(pred_expression)
                pass
            if pred_ans == gold_ans:
                same_answer_num += 1
    for key in total_num.keys():
        print(key, match_num[key] / total_num[key])
    print("total accuracy", sum(match_num.values()) / sum(total_num.values()))
    print("答案预测正确数", same_answer_num)
    print("总样本数", sum(total_num.values()))
    print("total result accuracy", same_answer_num / sum(total_num.values()))


def same_result_program(gold_program, pred_program):
    if "table" in gold_program:
        return gold_program == pred_program
    gold_expression = program_to_expression(gold_program)
    pred_expression = program_to_expression(pred_program)
    gold_ans = eval(convert_percent_to_decimal(gold_expression))

    try:
        pred_ans = eval(convert_percent_to_decimal(pred_expression))
    except:
        print("Fake:", pred_program)
        return False
    if pred_ans == gold_ans:
        return True


def eval_CompAQt_program(result_path, gold_key, pred_key):
    with open(result_path, 'r') as file:
        match_num = 0
        total_num = 0
        for line in file:
            data_dict = json.loads(line)
            total_num += 1
            gold_program = data_dict[gold_key]
            pred_program = data_dict[pred_key]
            if same_result_program(gold_program, pred_program):
                match_num += 1

    print("accuracy", match_num / total_num)


def eval_full_match(result_path, gold_key, pred_key):
    with open(result_path, 'r') as file:
        match_num = 0
        total_num = 0
        for line in file:
            data_dict = json.loads(line)
            total_num += 1
            gold = data_dict[gold_key]
            pred = data_dict[pred_key]
            if gold == pred:
                match_num += 1

    print("accuracy", match_num / total_num)
