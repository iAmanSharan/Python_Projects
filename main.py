email_id = input('enter your email_id ')
dot =  0
rate = 0
for i in range(len(email_id)):
  if email_id[i]==".":
    dot = i

  if email_id[i] =="@":
    rate = i
    break
username = email_id[dot+1:rate]
domain_name=email_id[rate+1:]
print(username," ",domain_name)

