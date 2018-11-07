#!/usr/bin/env python3

import argparse
import os
import extractor
args_parser = argparse.ArgumentParser(
    prog=extractor,
    description="A script to dump out Youdao dict or Youdao\
                recite word 's wordbook.",
    usage="app.py PATH-TO-WORDBOOK-DB-FILE [OPTIONS]"
)

args_parser.add_argument("source",
                        help="The path to your wordbook database file")

#args_parser.add_argument("d", "dest", help="Destination path to the output directory")

args = args_parser.parse_args()
input_db = os.path.abspath(args.source)
def check_file(db_path):
    print("Judging the input file...")
    cmd = "file " + db_path
    os.system(cmd)

def writeout(wordlist):
    work_dir = os.path.abspath("./")
    out_path = os.path.join(work_dir, "out")
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    out_file = os.path.join(out_path, "output.txt")
    try:
        print("Writing file...Please wait...")
        with open(out_file, "w", encoding="utf-8") as f:
            for word in wordlist:
                f.write(word + os.linesep)
        print("Done. Go to `out` dir and see your output file.")
    except IOError as ioe:
        print(ioe)

if __name__ == "__main__":
    check_file(input_db)
    wordlist = extractor.extract(input_db)
    writeout(wordlist)
