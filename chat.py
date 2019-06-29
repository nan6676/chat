import os
#讀取檔案
chat = []
with open('input.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		chat1 = line.strip()
		print(chat1)
		chat.append(chat1)
print(chat)
#寫入檔案
bef = 'Allen: '
with open('output.txt', 'w', encoding='utf-8') as a:
	for ch in chat:
		if ch == 'Allen':
			bef ='Allen: '
			continue
		elif ch == 'Tom':
			bef ='Tom: '
			continue
		else:
			a.write(bef + ch + '\n')