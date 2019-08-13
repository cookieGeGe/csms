user = [
    {"username": "root", "password": "123"},
    {"username": "admin", "password": "111"}
]

i = 1
while i <= 4:
    name = input('请输入用户名：')
    passwd = input('请输入密码：')
    username_list = []
    password_list = []
    for item in user:
        username_list.append(item['username'])
        password_list.append(item['password'])
    if name in username_list:
        index = username_list.index(name)
        # print('索引为：', index)
        if passwd == password_list[index]:
            # print('登录成功！')
            break
    i += 1
