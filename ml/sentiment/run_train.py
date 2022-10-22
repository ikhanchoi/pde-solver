import torch
from torch.utils.data import Dataset, DataLoader
import seq2seq, util, time


device = torch.device("mps")

# loading data
embed_dim = 256
hidden_dim = 256

# batchifying data
batch_size = 64

# traing model
n_epoch = 30



print("[!] loading data...")
import pandas as pd
class NaverMovieRatingDataset(Dataset):
	def __init__(self, file):
		self.data = pd.read_table(file)
	def __len__(self):
		return len(self.data)
	def __getitem__(self, index):
		return self.data.iloc[index, 1], self.data.iloc[index, 2]
train_data = NaverMovieRatingDataset("data/ratings_train_small.tsv")
valid_data = NaverMovieRatingDataset("data/ratings_test_small.tsv")
test_data = NaverMovieRatingDataset("data/ratings_test_small.tsv")



print("[!] processing data...")
from konlpy.tag import Okt
from torchtext.vocab import build_vocab_from_iterator
tokenizer = Okt()
def yield_tokens(data):
	for text, _ in data:
		yield tokenizer.morphs(text)
vocab = build_vocab_from_iterator(yield_tokens(train_data), specials=['<unk>'])
vocab.set_default_index(vocab['<unk>'])
def process(data):
	data = [(torch.tensor(vocab(tokenizer.morphs(text)), dtype=torch.long), label) for text, label in data]
	return data
train_data = process(train_data)
valid_data = process(valid_data)
test_data = process(test_data)



print("[!] batchifying data...")

train_data = iter(DataLoader(train_data, batch_size = batch_size))
print(next(train_data)[0].shape)
print(next(train_data)[1])
print(next(train_data)[0].shape)
print(next(train_data)[1])
def batchify_(data, batch_size):
	seq_len = data.size(0) // batch_size
	data = data[:seq_len * batch_size]
	data = data.view(batch_size, seq_len).t().contiguous()
	return data.to(device)
#train_data = batchify(train_data, batch_size)
#valid_data = batchify(valid_data, batch_size)
#test_data = batchify(test_data, batch_size)

print(next(train_data).shape)
#print(next(train_data))

'''

# Learning ...
model = Seq2Seq(len(vocab), 2, embed_dim, hidden_dim).to("mps")
optim = optim.Adam(model.parameters(), lr = 1e-5)
lossf = nn.MSELoss()

trainer = util.Trainer(model, optim, lossf)
trainer.learn(train_data, valid_data, test_data, n_epoch)





# Inferring tests!

inferer = util.Inferer()
'''