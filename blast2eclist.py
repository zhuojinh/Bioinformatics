import sys

argr = sys.argv
ec_uniprot = []

class ec:
    def __init__(self, number, content):
        self._ec = number
        self._content = content
    def __repr__(self):
        return self._ec
    def content(self):
        return self._content
    def name(self):
        return self._ec

with open(argr[2],'r') as ecfile:
    for eline in ecfile:
        ec_uniprot.append(ec(eline.strip().split('\t')[0], '\t'.join(eline.strip().split('\t')[1:])))

with open(argr[1],'r') as tblfile:
    for line in tblfile:
        line=line.strip()
        target=line.split('\t')[1].split('|')[1]
        for single_ec in ec_uniprot:
            if target in single_ec.content():
                print(single_ec.name())
                break
