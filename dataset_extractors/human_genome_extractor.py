from Bio import SeqIO

human_genome_fasta = "datasets\\the_human_genome_project\\ncbi_dataset\\data\\GCA_000001405.29\\GCA_000001405.29_GRCh38.p14_genomic.fna"
record_list = []

with open(human_genome_fasta) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        record.seq = record.seq[1: 100000]
        record_list.append(record)
    SeqIO.write(sequences=record_list, handle="fasta_files\\human_genome.fasta",format="fasta")
