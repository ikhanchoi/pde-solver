import hmm
import util
import time


starttime = time.time()

model = hmm.PhonemicHMM()
model.train(corpus = "jiyeogeo/jiyeogeo_parallel_corpus(all)") # /data/에 small.tsv 파일이 있어야 함
util.save_model(model, time = time.time()-starttime) # saved at /model/

print("훈련 시간: ", time.time()-starttime)
