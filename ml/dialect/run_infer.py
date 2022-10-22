import hmm
import util
import time

# load from DMT/data/
model = util.load_model("phonemic_hmm202210181715(2358.05s)") 
#model = util.load_model("phonemic_hmm201907041722(2112.78s)")
starttime = time.time()
text = model.translate("마이 좀 주이소")
print("번역 완료: ", text)

print("번역 시간: ", time.time()-starttime)
