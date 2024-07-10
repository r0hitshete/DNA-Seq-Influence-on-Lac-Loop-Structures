bases = ["A", "C", "G", "T"]
comp_bases = {"A":"T", "T":"A", "C":"G", "G":"C"}

#Read and store original p1f1
infile = open("bp_step.par","r")
p1f1 = infile.readlines()
infile.close()

count = 1 #Number the new files read in

tal_file = open("Tal_seq.txt", "r")

def createNewPar(seq_change, count):
    new_filename = f"p1f1_shift{count}"
    header = p1f1[0:3].copy() # constant header that each par file must have
    starting_frozen = p1f1[3:17].copy() #first 14 frozen
    new_model = p1f1[17:136].copy() # the parameter data we want to edit (taking out the first 14 and last 14)
    ending_frozen = p1f1[136: 150].copy() #last 14 frozen

    for j in range(len(new_model)):
        old_base_pair = new_model[j][:3] #the first three characters of each row, which has the base pair for replacing
        new_base_pair = seq_change[j] + "-" + comp_bases[seq_change[j]] # the replacement base pair
        new_model[j] = new_model[j].replace(old_base_pair, new_base_pair) # replacing the old base pair with the new
        del old_base_pair, new_base_pair
        
    outfile = open(new_filename+".par", "w")
    for line in header:
        outfile.write(line)
    for line in starting_frozen:
        outfile.write(line)
    for line in new_model:
        outfile.write(line)
    for line in ending_frozen:
        outfile.write(line)
        
    outfile.close()
    del new_filename, header, new_model

    return count+1
    
for seq in tal_file:
    createNewPar(seq.strip(), count)

