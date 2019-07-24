1a2b遊戲
===
遊戲方式
---
- 遊戲開始時程式會直接亂數出一個答案

- 玩家接著開始猜答案,每輸入一次後,都會有提示

- 猜對答案(4A)則結束遊戲

程式邏輯
---

- 一開始先作一個數字list,選四次,每次選一個數,並在每選完一個數後刪掉該數,確保不會選到重複數字

```python
num=(['1','2','3','4','5','6','7','8','9'])
ans=[]
for i in range(4):
    ans.append(choice(num))
    num.remove(ans[i])

```

- 進入while迴圈,由玩家輸入答案,並存成list
```python
while GameSet==0:
    
    Reply_A=0 #幾a
    Reply_B=0 #幾b
    
    usernum = input('input : ')
```

- 判斷幾a幾b,因為有數字不重複的限制,直接確認玩家答案中的各數字是否存在於電腦選號,再判斷是否在同個位置,是則為A,否則為B

```python
    for i in range(4):
        if usernum[i] in ans:
            if usernum[i]==ans[i]:
                Reply_A+=1
            else:
                Reply_B+=1
```

- 如果沒有達成成4A,則GameSet變數不變,繼續循環,有則將GameSet變數設為1,跳出迴圈,並提示遊戲結束

```python
        if Reply_A==4:
            GameSet=1
            
        else:
            exit
print("恭喜答對!!")
```


![image](1a2b_result.png)
