import os.path
import glob


def getCodeLength(dir):
    length = lines = 0
    for path in glob.glob(dir + "/**", recursive=True):
        if(os.path.isfile(path) and path.split(".")[-1] in ["html", "js", "css", "php"]):
            with open(path, "r", encoding="utf8") as f:
                for line in f.readlines():
                    length += len(line.strip())
                    lines += 1
    return {
        "dir": os.path.abspath(dir),
        "length": length,
        "lines": lines,
    }


if __name__ == "__main__":
    res = getCodeLength(input("input Directory: "))
    print(f"""dir: {res["dir"]}\nlength: {res["length"]}\nlines: {res["lines"]}""")
