#!/usr/bin/env python3

# Satellite features 
# @author: Maxfield Wang (moposx)
# @date Nov 7, 2018

import argparse
import logging
import os
import extractor
args_parser = argparse.ArgumentParser(
    prog=extractor,
    description="A script to dump out Youdao dict or Youdao\
                recite word 's wordbook.",
    usage="app.py PATH-TO-WORDBOOK-DB-FILE [OPTIONS]\nType `-h` or `--help` to see more help"
)

args_parser.add_argument("source",
                         help="The path to your wordbook database file")

#args_parser.add_argument("d", "dest", help="Destination path to the output directory")
args = args_parser.parse_args()


def check_file(db_path):
    print("Judging the input file...")
    cmd = "file " + db_path
    os.system(cmd)


def writeout(filename, wordlist):
    work_dir = os.path.abspath("./")
    out_path = os.path.join(work_dir, "out")
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    out_file = os.path.join(out_path, filename)

    try:
        print("Writing file...Please wait...")
        with open(out_file, "w", encoding="utf-8", errors="ignore") as f:
            for word in wordlist:
                f.write(word + os.linesep)
        print("Done! Go to `out` dir and see your output file(s).")
    except IOError as ioe:
        logging.exception(ioe)


if __name__ == "__main__":
    input_db = os.path.abspath(args.source)
    check_file(input_db)
    extractor_obj = extractor.Extractor()
    extracted_wordlist = extractor_obj.extract(input_db)
    writeout("output.txt", extracted_wordlist)
    writeout("normalwords.txt", sorted(extractor_obj.normal_words))