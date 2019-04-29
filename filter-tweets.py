import os
import json

dir_ = os.fsencode("D:/Twitter")
FSLR = {}
CSIQ = {}
VWSYF = {}
file_count = 0

for file_ in os.listdir(dir_):
    filename = os.fsdecode(file_)
    filename = str(os.path.join(os.fsdecode(dir_), filename))
    filename = filename.replace('\\', "/")
    file_count += 1
    
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            try:
                line = json.loads(line)
                text = line["text"]
            except:
                f.readline()
                continue

            if "fslr" in text.lower() or "first solar" in text.lower():
                FSLR[line["timestamp_ms"]] = text
            if "csiq" in text.lower() or "canadian solar" in text.lower():
                CSIQ[line["timestamp_ms"]] = text
            if "vwsyf" in text.lower() or "vestas wind systems" in text.lower():
                VWSYF[line["timestamp_ms"]] = text

            #tweets are separated by an empty line
            f.readline()
    
    print(file_count, "file parsed")
    

with open("D:/FSLR.json", 'w', encoding="utf-8") as f:
    json.dump(FSLR, f)

with open("D:/CSIQ.json", 'w', encoding="utf-8") as f:
    json.dump(CSIQ, f)    

with open("D:/VWSYF.json", 'w', encoding="utf-8") as f:
    json.dump(VWSYF, f)