import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import torchtext
import time


device = torch.device("cpu")


class Trainer(object):
	'''

	Args:
		model: our model.
		optim: optimizer.
		lossf: must be `nn.CrossEntropyLoss` or `nn.NLLLoss`.
	'''
	def __init__(self, model, optim, lossf):
		self.model = model
		self.optim = optim
		self.lossf = lossf
		self.best_valid_loss = 1e+300

	def learn(self, train_data, valid_data, test_data, n_epoch):
		'''
		Learns by training, validations, and tests.

		Args:
			data (triple(list[tuple(tensors)])): train, valid, test data.
			  The size of each tuple is same with the number of fields
			  like languages or lables.
			n_epoch (int): the number of epochs.

		Examples::

			>>> model = Seq2Seq(Kx, Ky, E, H)
			>>> optim = torch.optim.Adam(model.parameters())
			>>> lossf = torch.nn.NLLLoss()
			>>> trainer = ExampleTrainer(model, optim, lossf)
			>>> trainer.learn((train_data, valid_data, test_data), n_epoch)

		'''
		print("[!] learing...")
		for e in range(n_epoch):
			print("\n[Epoch %3d]"%e)
			self.train(train_data)
			self.validate(valid_data)
			self.test(test_data)
		print("[!] learning finised!")

	def train(self, train_data):
		print("[!] training model...")
		batch_loss = 0
		start = time.time()
		for b, batch in enumerate(train_data):
			sources = batch[0].to(device) # [Tx,B]
			targets = batch[1].to(device) # [Ty,B]
			# Compute loss
			outputs = self.model(sources, targets.size(0))
			loss = self.lossf(
				outputs.view(-1, outputs.size(2)), # [Ty*B;Ky]<-[Ty,B;Ky]
				targets.view(-1) # [Ty*B]<-[Ty,B]
			)
			# Back propagation
			self.optim.zero_grad()
			loss.backward()
			torch.nn.utils.clip_grad_norm_(self.model.parameters(), 10.0)
			self.optim.step()
			#
			batch_loss += loss.item() # loss is [1]-shape tensor
			if (b+1) % 40 == 0:
				print("[Batch : %4d/%4d] "%(b+1, len(train_data)),
					  "[Avg Loss : %5.6f]"%(batch_loss/40))
				batch_loss = 0
		print("[Time : %.2f]"%(time.time()-start))

	def validate(self, valid_data):
		print("[!] validating model...")
		valid_loss = 0
		with torch.no_grad(): # does not compute grad in validation or evaluation
			for batch in valid_data:
				sources = batch[0].to(device)
				targets = batch[1].to(device)
				#
				outputs = self.model(sources, targets.size(0)) # [Ty,B;Ky]<-[Tx,B],Ty
				loss = self.lossf(
					outputs.view(-1, outputs.size(2)), # [Ty*B;Kx]<-[Ty,B;Kx]
					targets.view(-1) # [Ty*B]<-[Ty,B]
				)
				#
				valid_loss += loss.item()
		avg_valid_loss = valid_loss/len(valid_data)
		print("[Avg Loss : %5.6f]"%(avg_valid_loss))

		if self.best_valid_loss > avg_valid_loss:
			self.best_valid_loss = avg_valid_loss
			self.checkpoint()

	def test(self, test_data):
		'''
		Prints loss.
		'''
		print("[!] testing model...")
		test_loss = 0
		with torch.no_grad(): # does not compute grad in validation or evaluation
			for batch in test_data:
				sources = batch[0].to(device)
				targets = batch[1].to(device)
				#
				outputs = self.model(sources, targets.size(0)) # [Ty,B;Ky]<-[Tx,B],Ty
				loss = self.lossf(
					outputs.view(-1, outputs.size(2)), # [Ty*B;Kx]<-[Ty,B;Kx]
					targets.view(-1) # [Ty*B]<-[Ty,B]
				)
				#
				test_loss += loss.item()
		print("[Test Avg Loss : %5.6f]"%(test_loss/len(test_data)))

		# Although I did not implement, you may add BLEU score or perplexity calculator here.

	def checkpoint(self):
		'''
		Saves the model
		'''
		print("[!] saving model...")
		import os
		from datetime import datetime
		
		# the path ".save" is called in main function
		if not os.path.isdir(".save"):
			os.makedirs(".save")
		torch.save(self.model.state_dict(),
			"model/seq2seq-%s-loss-%.2f.pt"
			%(datetime.now().strftime('%m%d-%H%M'), self.best_valid_loss))



# Field 사용함, 옛날 버전만 가능
class Inferer(object):
	'''
	
	.. note ::
		You may see a poor result of this translater since torchtext package
		incompletely supports the "de-embedding" process which transforms
		vector to text. The target language should be declared with
		`ReversibleField`.

	Examples::

		>>>	model = Seq2Seq(Kx, Ky, E, H)
		>>> model.load_state_dict(torch.load('.save/<model_state_dict_name>.pt'))
		>>> inferer = ExampleTranslater(model, ENGLISH, DEUTSCH)
		>>> inferer.infer("Let f be a continuous function on a compact space.")
		... <a german sentence will be printed>.
	'''
	def __init__(self, model, input_field, output_field):
		self.model = model
		self.input_field = input_field
		self.output_field = output_field

	def infer(self, text):
		toks = self.input_field.preprocess(text)
		input_tensor = self.input_field.process([toks], device=device) # [Tx,1]
		output_tensor = self.model(input_tensor, len(input_tensor)*2)
		inferred_tensor = output_tensor.max(2)[1] # [2Tx,1]
		output = self.output_field.reverse(inferred_tensor)[0]
		return output
