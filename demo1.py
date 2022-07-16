db = [{'uname':'123','pwd':'12345'},{'uname':'1234','pwd':'123456'}]
zh = input('请输入账号：')
mm = input('请输入密码：')

a = 1 

for i in db:
    while a <= len(db):
        a = a + 1
        if zh == i.get('uname'):
            i['pwd'] = mm
            break
        else:
            db.append({'uname':zh,'pwd':mm})

print(db)