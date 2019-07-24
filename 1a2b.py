#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import choice
GameSet=0

num=(['1','2','3','4','5','6','7','8','9'])
ans=[]
for i in range(4):
    ans.append(choice(num))
    num.remove(ans[i])

usernum=[]
print(ans)

print("請輸入一串不重複的四位數字")

while GameSet==0:
    
    Reply_A=0  #幾a
    Reply_B=0  #幾b
    
    usernum = input('input : ')
    for i in range(4):
        if usernum[i] in ans:
            if usernum[i]==ans[i]:
                Reply_A+=1
            else:
                Reply_B+=1
        if Reply_A==4:
            GameSet=1
            
        else:
            exit
    print('%dA%dB' % (Reply_A,Reply_B))
    
print("恭喜答對!!")





