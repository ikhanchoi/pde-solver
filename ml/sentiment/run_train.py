import torch
import util, time


device = torch.device("cpu")


batch_size = 64

embed_dim = 256
hidden_dim = 256


n_epoch = 30





print("[!] loading dataset...")

import pandas as pd
from torch.utils.data import Dataset

class NSMC(Dataset):
	def __init__(self, file):
		self.data = pd.read_table(file)
	def __len__(self):
		return len(self.data)
	def __getitem__(self, index):
		return self.data.iloc[index, 1], self.data.iloc[index, 2]

train_data = NSMC("data/ratings_train.tsv")
valid_data = NSMC("data/ratings_test.tsv")
test_data = NSMC("data/ratings_test.tsv")
# list of pairs of a text and its label



print("[!] processing dataset...")

# we need tokenizer and vocabulary
from konlpy.tag import Okt
from torchtext.vocab import build_vocab_from_iterator
import os

tokenizer = Okt()

if not os.path.isfile("model/vocab.pt"):
	print("  [!] building vocabulary...")
	def yield_text_tokens(data):
		for text, _ in data:
			yield tokenizer.morphs(text)

	text_vocab = build_vocab_from_iterator(yield_text_tokens(train_data), specials=['<unk>', '<pad>'])
	text_vocab.set_default_index(text_vocab['<unk>'])
	torch.save(text_vocab, "model/vocab.pt")
else:
	text_vocab = torch.load("model/vocab.pt")
	print("  [!] loaded vocabulary...")

# now we process data
def process(data):
	return [(torch.tensor(text_vocab(tokenizer.morphs(text)), dtype = torch.long), label) for text, label in data]

train_data = process(train_data)
valid_data = process(valid_data)
test_data = process(test_data)



print("[!] batchifying dataset...")

from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence

def collate_fn(batch):
	# batch: list of pairs of a text tensor and its label
	texts, labels = zip(*batch)
	texts = pad_sequence(texts, batch_first = True, padding_value = text_vocab['<pad>']).transpose(0,1)
	labels = torch.tensor(labels).unsqueeze(0)

	return texts, labels

train_data = DataLoader(train_data, batch_size = batch_size, collate_fn = collate_fn)
valid_data = DataLoader(valid_data, batch_size = batch_size, collate_fn = collate_fn)
test_data = DataLoader(test_data, batch_size = batch_size, collate_fn = collate_fn)





# Learning ...



import torch.nn as nn
import torch.optim as optim
from seq2seq import Seq2Seq

model = Seq2Seq(len(text_vocab), 2, embed_dim, hidden_dim).to(device)
optim = optim.Adam(model.parameters(), lr = 1e-5)
lossf = nn.CrossEntropyLoss()

trainer = util.Trainer(model, optim, lossf)
trainer.learn(train_data, valid_data, test_data, n_epoch)



torch.save(model.state_dict(), "model/model.pt")
