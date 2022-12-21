"""
1.英制单位英寸与公制单位厘米互换。
"""
# value = float(input("请输入长度："))
# unit = input("请输入单位：")

# if unit == "in" or unit == "英寸":
#     print(f"{value}英寸 -> {value * 2.54}厘米")
# elif unit == "cm" or unit == "厘米":
#     print(f"{value}厘米 -> {value / 2.54}英寸")
# else:
#     print("请输入有效单位")


"""
2.百分制成绩转换为等级制成绩。
要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
"""
# scope = float(input("请输入成绩："))
# if scope >= 90:
#     grade = "A"
# elif 80 <= scope < 90:
#     grade = "B"
# elif 70 <= scope < 80:
#     grade = "C"
# elif 60 <= scope < 70:
#     grade = "D"
# else:
#     grade = "E"
# print(f"成绩等级为{grade}")


"""
3.输入三条边长，如果能构成三角形就计算周长和面积。
提示：两边之和大于第三条边
海伦公式：通过边长能够计算三角形面积
"""
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

if a + b > c and a + c > b and b + c > a:
    周长 = a + b + c
    print(f"周长：{周长}")
    p = 周长 / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"面积：{area}")
else:
    print("不构成三角形")
