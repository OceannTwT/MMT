import time
import json
import logging
from gpt_predict import predict
from config import args
from utils import print_exp

if __name__ == '__main__':
    prompt = " "
    if args.read_from_file == False:
        prompt = args.input
    else :
        with open(args.input, "r", encoding = "UTF-8") as f:
            for idx, line in enumerate(f):
                prompt = prompt + line

    if args.need_series == False:
        print(prompt)
        print_exp(args)
        ans = predict(args, prompt)
        print(ans)
    else:
        lines = []
        ans_list = []
        with open(args.series, "r", encoding= "UTF-8") as f:
            for idx, line in enumerate(f):
                lines.append(line)
        original_prompt = prompt
        for idx, line in enumerate(lines):
            prompt_dict = json.loads(line)
            new_prompt = prompt_dict["question"]
            new_type = prompt_dict["type"]
            # print(new_prompt)
            if new_type == "normal":
                # print(prompt) 
                query = prompt + new_prompt
                ans = predict(args, query)
                ans_list.append(ans)
            else :
                prompt = original_prompt
                query = prompt + new_prompt
                ans = predict(args, query)
                ans_list.append(ans)
                prompt = prompt + ans


        with open(args.output_dir, "a", encoding = "UTF-8") as f:
            for idx, ans in enumerate(ans_list):
                f.write(ans + '\n')
            

