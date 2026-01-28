def hex_to_coordinates(hex_input):
    # 1. 将十六进制转换为二进制
    binary_str = bin(int(hex_input, 16))[2:].zfill(24)
    
    # 2. 顺序取13位数作为X坐标
    x_binary = binary_str[:13]
    
    # 3. 倒序取10位数作为Y坐标
    reversed_binary = binary_str[::-1]
    y_binary = reversed_binary[:10]
    
    # 4. 二进制转十进制
    x_decimal = int(x_binary, 2)
    y_decimal = int(y_binary, 2)
    
    # 5. 坐标计算
    x_result = x_decimal * 0.2 - 500
    y_result = y_decimal * 0.2 - 102.3

    # 6. 浮点数转整数后再转二进制
    x_int = int(round(x_result))
    y_int = int(round(y_result))
    x_result_binary = bin(x_int)  
    y_result_binary = bin(y_int)
    
    return x_result, y_result, x_result_binary, y_result_binary

def main():
    print(f"Radar Calculator [Version 1.0]\n(c) Akira Amatsume. All rights reserved.\n您好，欢迎使用我们全新设计的毫米波雷达计算器")
    # 获取用户输入
    hex_input = input("\n在这里导入您需要计算的数值\n它应该是个6位数的十六进制\n").strip().upper()
    
    # 验证输入是否为有效的6位十六进制数
    if len(hex_input) != 6:
        print("错误：请输入6位十六进制数！")
        return
    
    try:
        int(hex_input, 16)
    except ValueError:
        print("错误：请输入有效的十六进制数！")
        return
    
    x_result, y_result, x_result_binary, y_result_binary = hex_to_coordinates(hex_input)
    
    # 输出结果
    print(f"\n转换中……\n转换成功！")
    print("\n" + "="*50)
    print(f"您输入的是: {hex_input}")
    print(f"这是个有效的毫米波坐标")
    print("-"*30)
    print(f"X坐标: {x_result:.2f}")
    print(f"二进制: {x_result_binary}") 
    print("-"*30)
    print(f"Y坐标: {y_result:.2f}")
    print(f"二进制: {y_result_binary}")
    print("="*50)

# 运行主函数
if __name__ == "__main__":
    main()