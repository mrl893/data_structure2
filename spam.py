
import glob 
import os


e_mails = []
labels = [] # [], []


"""
file_path = "mining/enron1/spam/0058.2003-12-21.GP.spam.txt" # ham/0007.1999-12-14.farmer.ham.txt"
with open(file_path, "r") as infile:
    # ham_sample 
    spam_sample = infile.read()
print(spam_sample)

"""
file_path = "mining/enron1/spam/"

for filename in glob.glob(os.path.join(file_path, "*.txt")):
    with open(filename, "r", encoding="ISO-8859-1") as infile:
        e_mails.append(infile.read())
        labels.append(0)
print(len(e_mails))
print(len(labels))
    
