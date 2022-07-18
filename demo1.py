db = [{'name':'ayi','pwd':'123'},{'name':'xinxin','pwd':'1233'},{'name':'ayi','pwd':'123'}]
zh = input('请输入姓名：')
mm = input('请输入密码：')
a = 0

for i in db:
    a = a + 1
    if i.get('name') == zh:
            i['pwd'] = mm
            break
    else:
        if a == len(db):
            db.append({'name':zh,'pwd':mm})
print(db)