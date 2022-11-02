import torch
from seq2seq import Seq2Seq


device = torch.device("cpu")

vocab = torch.load("model/vocab.pt")
model = Seq2Seq(len(vocab), 2, 256, 256).to(device)
model.load_state_dict(torch.load('model/model.pt'))





def polarity(tensor):
	return torch.exp(model(tensor,2)[-1:,:,0]).item()

def infer(text):
	from konlpy.tag import Okt
	tokenizer = Okt()
	polarity = torch.exp(model(torch.tensor(vocab(tokenizer.morphs(text)), dtype = torch.long).unsqueeze(1),1))[0][0][1].item()
	print("  ", text, " -> {:.2%}".format(polarity))



infer("상품 정말 잘 받았구요")
infer("흠집 하나 없이 온전히 잘 왔어요. 만족도 높습니다.")
infer("배송 개느림. 다신 여기서 안 산다.")
infer("진심 인생 영화")
infer("커피 온도가 왜 이래요. 장난해요?")

while True:
	text = str(input("문장을 입력해주세요: "))
	infer(text)

'''
ok_count = 0
for line in test_iter:
	if 2.5 < polarity(line.text) + line.label.item() < 3.5:
		ok_count += 1
print(100*ok_count/len(test_iter),"%")
'''