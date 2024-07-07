from Bio import SeqIO


corona_genome_fasta = "datasets\\severe_acute_respiratory_syndrome_coronavirus_2\\ncbi_dataset\\data\\GCA_009858895.3\\GCA_009858895.3_ASM985889v3_genomic.fna"
record_list = []

with open(corona_genome_fasta) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        record_list.append(record)
    SeqIO.write(sequences=record_list, handle="fasta_files\\corona_genome.fasta",format="fasta")