# main.py

def has_duplicates(lst):
    """判断列表中是否存在重复元素，存在则返回True，否则返回False"""
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False


# 主程序：调用函数并输出测试结果
if __name__ == "__main__":
    # 测试用例（覆盖不同类型元素）
    test_cases = [
        [],          # 空列表
        [1],         # 单元素
        [1, 2, 3],   # 无重复
        [1, 2, 1],   # 数字重复
        ["a", "b", "a"],  # 字符串重复
        [1.0, 2.0, 1.0],  # 浮点数重复
        [True, False],    # 布尔值无重复
        [None, None]      # None值重复
    ]
    
    # 遍历测试并输出结果
    for case in test_cases:
        result = has_duplicates(case)
        if result:
            print(f"列表 {case} 存在重复元素")
        else:
            print(f"列表 {case} 没有重复元素")
