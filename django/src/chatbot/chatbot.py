import torch
from transformers import PreTrainedTokenizerFast
from recommend_cosmetics import Recommend


class Chatbot:
    def __init__(self) -> None:
        self.Q_TKN = "<usr>"
        self.A_TKN = "<sys>"
        self.BOS = '</s>'
        self.EOS = '</s>'
        self.MASK = '<unused0>'
        self.SENT = '<unused1>'
        self.PAD = '<pad>'
        self.model_path = 'c:/PersonalColor/src/chatbot/model'

    def chatbot(self):
        Q_TKN = self.Q_TKN
        SENT = self.SENT
        A_TKN = self.A_TKN
        BOS = self.BOS
        EOS = self.BOS
        PAD = self.PAD 
        MASK = self.MASK
        device = torch.device("cpu")
        koGPT2_TOKENIZER = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2", bos_token=BOS, eos_token=EOS, unk_token="<unk>", pad_token=PAD, mask_token=MASK)
        model = torch.load(f'{self.model_path}/model.pt', map_location=device)
        r = Recommend()
        with torch.no_grad():
            intro = "안녕하세요"
            print(f"Chatbot > {intro}")
            while 1:
                q = input("user > ").strip()
                if q == "종료":
                    break
                elif '화장품' in q:
                    if '봄' in q:
                        print(f'{r.spring()} 을(를) 추천해드려요.')
                        continue
                    elif '여름' in q:
                        print(f'{r.summer()} 을(를) 추천해드려요.')
                        continue
                    elif '가을' in q:
                        print(f'{r.fall()} 을(를) 추천해드려요.')
                        continue
                    elif '겨울' in q:
                        print(f'{r.winter()} 을(를) 추천해드려요.')
                        continue
                a = ""
                while 1:
                    input_ids = torch.LongTensor(koGPT2_TOKENIZER.encode(Q_TKN + q + SENT + A_TKN + a)).unsqueeze(dim=0)
                    pred = model(input_ids)
                    pred = pred.logits
                    gen = koGPT2_TOKENIZER.convert_ids_to_tokens(torch.argmax(pred, dim=-1).squeeze().numpy().tolist())[-1]
                    if gen == EOS:
                        break
                    a += gen.replace("▁", " ")
                print("Chatbot > {}".format(a.strip()))


if __name__ == '__main__':
    Chatbot().chatbot()
