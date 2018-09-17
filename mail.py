import yagmail
j=[]
for i in range(100000):
    j.append(str(i))
yag = yagmail.SMTP( user="", password="", host='smtp.163.com')
contents = j
yag.send('34', '测试', contents)

