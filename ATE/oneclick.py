import edit, os, removeComments


if __name__ == "__main__" :
    edit.main()
    removeComments.main()
    for each in ["", "2", "json"]:
        with open("Compress" + each + ".bat") as f:
            s = f.read().split("\n")
            print(s, os.system(s[0]), os.system(s[1]))
