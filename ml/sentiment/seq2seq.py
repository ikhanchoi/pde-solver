'''
Word tensors are named singular, and a sentence tensor is named
plural, even if the batch size is > 1.

Indices in tensor shape representation before semicolon specify
a word token, and dimension after the semicolon means the dimension
of the word token vector: for a batch tensor of shape [T,B;H],
index t indicates word position and index b specify a sentence in
the batch, each word is vectorized into H-dim vector.

This version of implementation does not handle OOV; the vocabulary
is already loaded so that it contains all words in the dataset.

Paper link: https://arxiv.org/abs/1409.0473
'''

import torch
import torch.nn as nn
device = torch.device("cpu")


class Seq2Seq(nn.Module):
	''' Seq2Seq with attention.
	When instantiating the class, all attributes and their learnable
	paramters are automatically drawn in the given device, if available.

	Args:
		n_enc_vocab (int): the size of source language vocabulary.
		n_dec_vocab (int): the size of target language vocabulary.
		embed_dim (int): dimension of embedding vector.
		hidden_dim (int): dimension of hidden state vector.

	Inputs:
		intputs (tensor[Tx,B]): one-hot encoded source sentence; each
		  component is an integer in the interval [0:Kx].
		trg_len (int): length of target sentence.

	Outputs:
		outputs (tensor[Ty,B;Ky]): log-probability distribution of
		  output sentence.

	Attributes:
		encoder (Encoder): bidirectional GRU cells.
		decoder (Decoder): GRU cell with attention mechanism.
		init_hidden (nn.Sequential): Initializes hidden vector for
		  decoding. Gets last hidden vector on reverse direction obtained
		  from encoder, and returns initial hidden vector for decoding.
		  **Input Type:** last_hidden (tensor[B;H]).
		  **Output Type:** init_hidden (tensor[B;H]).
		
	'''

	def __init__(self, n_enc_vocab, n_dec_vocab, embed_dim, hidden_dim):
		super().__init__()
		self.encoder = Encoder(n_enc_vocab, embed_dim, hidden_dim).to(device)
		self.decoder = Decoder(n_dec_vocab, embed_dim, hidden_dim).to(device)
		self.init_hidden = nn.Sequential(
				nn.Linear(hidden_dim, hidden_dim),
				nn.Tanh()
			).to(device)

	def forward(self, inputs, trg_len): # [Tx,B],Ty
		Ty = trg_len
		B = inputs.size(1)
		Ky = self.decoder.Ky
		outputs = torch.zeros(Ty, B, Ky).to(device)

		# encoding
		enc_output, hidden = self.encoder(inputs) # [Tx,B;2H],[2,B;H]<-[Tx,B]

		# initialize inputs for decoder
		input = torch.ones(B).long().to(device) # [B] SOS
		hidden = self.init_hidden(hidden[-1]) # [B;H]<-[2,B;H]

		# decoding
		for t in range(Ty):
			output, hidden = self.decoder(input, hidden, enc_output)
			outputs[t] = output
			input = output.max(1)[1]
		return outputs

class Encoder(nn.Module):
	'''
	Args:
		n_vocab (int): size of source language vocabulary.
		embed_dim (int): dimension of embedding vector.
		hidden_dim (int): dimension of hidden state vector.

	Inputs:
		inputs (tensor[Tx,B]): one-hot encoded sentences in a batch
		  in which maximal length has `Tx`.

	Outputs:
		outputs (tensor[Tx,B;2H]): output vectors obtained from each
		  cell that will be used to make context vectors in alignment
		  model.
		hidden (tensor[2,B;H]): last hidden vector that will be used
		  to make initial hidden vector of decoder.

	Attributes:
		Kx (int): n_vocab.
		E (int): embed_dim. Shared with decoder.
		H (int): hidden_dim. Shared with decoder.
		emb (nn.Embedding): Returns embedded word vectors.
		  **Input Type:** inputs (tensor[Tx,B]).
		  **Output Type:** embeds (tensor[Tx,B;E]).
		gru (nn.GRU): bidirectional GRU cell.
		  **Input Type:** embeds (tensor[Tx,B;E]), hidden (tensor[2,B;H]).
		  **Output Type:** outputs (tensor[Tx,B;2H]), hidden (tensor[2,B;H]).

	.. note::
		By calling self.gru only once, tensors propagate the circuit
		consisting of linearly connected `Tx` GRU cells.
	.. note::
		The number `2` in `outputs` and `hidden` is due to the encoder
		cell is set to be bidirectional.
	'''
	def __init__(self, n_vocab, embed_dim, hidden_dim):
		super().__init__()
		self.Kx = n_vocab
		self.E = embed_dim
		self.H = hidden_dim
		self.emb = nn.Embedding(self.Kx, self.E)
		self.gru = nn.GRU(self.E, self.H, bidirectional=True)
			
	def forward(self, inputs, hidden=None): # [Tx,B]
		embeds = self.emb(inputs) # [Tx,B;E]<-[Tx,B]
		outputs, hidden = self.gru(embeds, hidden) #: [Tx,B;2H],[2,B;H]<-[Tx,B;E],[2,B;H]
		return outputs, hidden # [Tx,B;2H],[2,B;H]

class Decoder(nn.Module):
	'''
	Args:
		n_vocab (int): the number of words in target language vocabulary.
		embed_dim (int): dimension of embedding vector.
		hidden_dim (int): dimension of hidden state vector.

	Inputs:
		input (tensor[B]): most probable output at the last decoding
		  cell
		hidden (tensor[B;H])
		enc_output (tensor[Tx,B;2H]): condition to force alignment.

	Outputs:
		output (tensor[B;Ky]): log-probability of index of target words.
		hidden (tensor[B;H])
		
	Attributes:
		Ky (int): n_vocab
		E (int): embed_dim. Shared with decoder.
		H (int): hidden_dim. Shared with decoder.
		emb (nn.Embedding): Transforms one-hot encoded input or output
		  vectors to embedded vector before GRU cell.
		  **Input Type:** input (tensor[B]).
		  **Output Type:** embed (tensor[B;E]).
		gru (nn.GRU): This GRU cell should not be bidirectional. Unlike
		  encoder, `self.gru` go through only one GRU cell. It will be
		  called when running a for loop of length `Ty` in `Seq2Seq.forward`.
		  The size of input embed vector is added by `2H` because context
		  vector was attached.
		  **Input Type:** embed (tensor[1,B;E+2H]), hidden (tensor[1,B;H]).
		  **Output Type:** output (tensor[1,B;H]), hidden (tensor[1,B;H]).
		lsm (nn.Sequential): Takes logsoftmax for de-embedding and to get
		  a log-probability distribution that the RNN output vector is
		  corresponded to each taget language word.
		  **Input Type:** rnn_output (tensor[B;H]) + context (tensor[B;2H]).
		  **Output Type:** output (tensor[B,Ky]).
		attn (nn.Sequential): Referring to hidden vector and the full-
		  length output from encoder, returns attention weights at each
		  decoding time `ty`. Note that the input length is `Tx`, not
		  `Ty`. The intput hidden vector is made by repeating the
		  original decoder hidden of shape `[B;H]`, `Tx` times. The
		  encoder output is universally used at all decoding time `ty`
		  wihtout modification. Since the time `ty` is fixed in
		  `decoder.forward`, the attention weights are not given by a
		  matrix, but a `Tx`-dimensional real vector.
		  **Input Type:** hidden (tensor[Tx,B;H]) + enc_output (tensor[Tx,B;2H]).
		  **Output Type:** attn_weight (tensor[Tx,B;1]).

	'''
	def __init__(self, n_vocab, embed_dim, hidden_dim):
		super(Decoder, self).__init__()
		self.Ky = n_vocab
		self.E = embed_dim
		self.H = hidden_dim
		self.emb = nn.Embedding(self.Ky, self.E)
		self.gru = nn.GRU(self.E + 2*self.H, self.H) # must be bidirectional=False
		self.lsm = nn.Sequential(
						nn.Linear(3*self.H, self.Ky),
						nn.LogSoftmax(dim=-1)
					)
		self.attn = nn.Sequential(
						nn.Linear(3*self.H, self.H), # [Tx,B;H]<-[Tx,B;3H]
						nn.Tanh(), # [Tx,B;H]<-[Tx,B;H]
						nn.Linear(self.H, 1), # [Tx,B;1]<-[Tx,B;H]
						nn.Softmax(dim=0) # [Tx,B;1]<-[Tx,B;1]
					)

	def forward(self, input, hidden, enc_output): # [B],[B;H],[Tx,B;2H]
		context = self.alignment(hidden, enc_output) # [B,2H]<-[B;H],[Tx,B;2H]
		embed = self.emb(input) # [B;E]<-[B]
		rnn_input = torch.cat([embed, context],1) # [B;E+2H]<-[B;E],Context
		rnn_input = rnn_input.unsqueeze(0) # [1,B;E+2H]<-[B;E+2H]
		hidden = hidden.unsqueeze(0)

		# >> rnn_in[1,B;E+2H], hidden[1,B;H]
		rnn_output, hidden = self.gru(rnn_input, hidden)
		rnn_output = rnn_output.squeeze(0) # [B;H]<-[1,B;H]
		# << rnn_out[B;H], hidden[1,B;H]

		output = torch.cat([rnn_output, context],1) # [B;3H]<-[B;H],Context
		output = self.lsm(output) # [B;Ky]<-[B;3H]
		return output, hidden[-1] # [B;Ky],[B;H]

	def alignment(self, hidden, enc_output): # [B;H],[Tx,B;2H]
		'''Alignment model

		Args:
			hidden (tensor[B;H]): hidden state vector.
			enc_output (tensor[Tx,B;2H]): the whole output of encoder.
		Returns:
			tensor[B,2H]: context vector that contains information that
			which word in source sentence mainly acts.
		'''
		Tx = enc_output.size(0)
		hidden = hidden.repeat(Tx,1,1) # [Tx,B;H]<-[B;H]
		attn_input = torch.cat([hidden, enc_output],2)
		attnw = self.attn(attn_input) # [Tx,B;1]<-[Tx,B;3H]

		attnw = attnw.transpose(0,1).transpose(1,2) # [B,1,Tx]<-[Tx,B,1]
		enc_output = enc_output.transpose(0,1) # [B,Tx,2H]<-[Tx,B,2H]
		context = torch.bmm(attnw, enc_output).squeeze(1) # [B,2H]<-[B,1,2H]<-[B,1,Tx],[B,Tx,2H]
		return context # [B,2H]





