import hmm
import util
import time

# load from DMT/data/
model = util.load_model("phonemic_hmm202210181715(2358.05s)") 
#model = util.load_model("phonemic_hmm201907041722(2112.78s)")

text = input("사투리 문장을 입력해주세요:  ")
starttime = time.time()

text = model.translate(text)
print("번역 완료: ", text)

print("번역 시간: ", time.time()-starttime)
