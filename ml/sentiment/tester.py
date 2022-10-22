import torch
from seq2seq import Seq2Seq

from load_data import *

train_iter, val_iter, test_iter, TEXT = load_data()
model = Seq2Seq(2827, 2, 256, 256).to("mps") #2827(small data) 71908(full data)
model.load_state_dict(torch.load('model.pt'))

def tensorize(field, text):
	return field.process([field.preprocess(text)], device='mps')

def polarity(tensor):
	return torch.exp(model(tensor,2)[-1:,:,0]).item()

def infer(text):
	print(text, '-> %.2f'%(polarity(tensorize(TEXT,text))))

a = infer("상품 정말 잘 받았구요")
a = infer("흠집 하나 없이 온전히 잘 왔어요. 만족도 높습니다.")
a = infer("배송 개느림. 다신 여기서 안 산다.")
a = infer("진심 인생 영화")
a = infer("커피 온도가 왜 이래요. 장난해요?")


ok_count = 0
for line in test_iter:
	if 2.5 < polarity(line.text) + line.label.item() < 3.5:
		ok_count += 1
print(100*ok_count/len(test_iter),"%")