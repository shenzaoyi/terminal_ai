#! python
from zhipuai import ZhipuAI
from colorama import init, Fore, Back, Style


client = ZhipuAI(api_key="") # 填写APIKey

message_total = []

def output(dic):
    print(dic.get("content"),end="")

print(Fore.BLUE + "*" * 10)
print( Fore.BLUE + "ZHIPU AI: version : glm-4")
print(Fore.BLUE +  "Welcome, shenzaoyi!")
print(Fore.BLUE +  "Ask a great question, is the best way to learn something:")
print(Fore.RESET + "*" * 10)

while(1):
    msg = input("user : ")
    if (msg == "exit"):
        break
    msg = msg + "," + "请用中文回答我"
    dic = {"role":"user","content":msg}
    message_total.append(dic)
    response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=message_total,
    stream=True
    )
    print("assistant: ",end="")
    final_content = ""
    for chunk in response:
        temp_content = chunk.choices[0].delta.content
        print(temp_content,end="")
        final_content = final_content + temp_content
        
        # output(dic_temp)
    dic_temp = {"role":"assistant","content":final_content}
    print("\n")
    message_total.append(dic_temp)

print(Fore.GREEN + "System: " + "GoodBye! ")
print(Fore.GREEN + "But we are hackers and hackers have black terminals with green font colors")

