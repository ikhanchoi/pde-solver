import torch
import torch.nn as nn
import torch.optim as optim

from seq2seq import Seq2Seq
from load_data import *
'''
class Sentiment(nn.Module):
	def __init__(self, n_vocab, embed_dim, hidden_dim):
		super(Sentiment, self).__init__()
		self.K = n_vocab
		self.E = embed_dim
		self.H = hidden_dim
		self.mlp = nn.Sequential(
				nn.Embedding(n_vocab, embed_dim), # [T,B,E]
				nn.Linear(embed_dim, hidden_dim), # [T,B,H]
				nn.Tanh(), # [T,B,H]
				nn.Linear(hidden_dim, hidden_dim), # [T,B,H]
				nn.Tanh(), # [T,B,H]
				nn.Linear(hidden_dim, hidden_dim), # [T,B,H]
				nn.Tanh(), # [T,B,H]
				nn.Linear(hidden_dim,1), # [T,B,1]
				)
	def forward(self, input): # [T,B]
		res = self.mlp(input) # [T,B,1]
		res = torch.sum(res, dim=0)/res.size(0) # [B,1]
		res = torch.sigmoid(res) # [B,1]
		res = torch.transpose(res, 0, 1) # [1,B]
		return res
'''


import time
start = time.time()

train_iter, val_iter, test_iter, TEXT = load_data()
n_vocab = len(TEXT.vocab)


print("TIME1: ", time.time()-start)
'''
class SentimentRNN(nn.Module):
	def __init__(self):
		super(SentimentRNN, self).__init__()
		self.K = n_vocab
		self.E = embed_dim
		self.H = hidden_dim
		self.rnn = nn.GRU(self.E, self.H, bidirectional=False)
	def forward(self, input):
		hidden = torch.tensor()
		outputs = torch.tensor()
		for i in range(input.size(0)):
			output, hidden = self.rnn(input[i], hidden)
			outputs.cat(output)
'''


model = Seq2Seq(n_vocab, 2, 256, 256).to("mps")
optim = optim.Adam(model.parameters(), lr = 1e-5)
lossf = nn.MSELoss()


print("TIME2: ", time.time()-start)

former_loss = 100000000
warn = 0
for e in range(30):
	print("epoch", e)
	for b, batch in enumerate(train_iter):
		optim.zero_grad()
		output = model(batch.text, 2)
		loss = lossf(torch.exp(output[-1:,:,0]), 3 - batch.label.float())
		loss.backward()
		optim.step()

		if b % 500 == 0:
			print(b," th data")
	
	eval_loss = 0
	for b, batch in enumerate(val_iter):
		output = model(batch.text, 2)
		loss = lossf(torch.exp(output[-1:,:,0]), 3 - batch.label.float())
		eval_loss += loss.item()
	print("EVAL_LOSS: ", eval_loss)
	if former_loss < eval_loss:
		warn += 1
	if warn == 2:
		break
	former_loss = eval_loss

print("TIME3: ", time.time()-start)

torch.save(model.state_dict(), 'model.pt')


