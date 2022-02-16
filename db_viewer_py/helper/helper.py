import os


def find_dbs() -> dict:
    # print(f"CWD = {os.getcwd()}")
    dbs = {}
    for root, dirs, files in os.walk(os.getcwd()):
        # print(f"ROOT - {root}")
        # print(f"DIRS - {dirs}")
        # print(f"ROOT - {files}")
        for file in files:
            if file.endswith(".db"):
                dbname = os.path.splitext(file)[0]
                dbs[dbname] = os.path.join(root, file)
    return dbs


def main():
    for dbname in find_dbs():
        print(dbname)
    print("DBs listed")


if __name__ == '__main__':
    main()
