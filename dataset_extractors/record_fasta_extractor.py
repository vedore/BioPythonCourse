from Bio import SeqIO

human_genome_fasta = "C:\\Faculdade\\BioInformatica\\bio\\fasta_files\\human_genome.fasta"
record_list = []

with open(human_genome_fasta) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        record.seq = record.seq[1: 100000]
        record_list.append(record)
        break
    SeqIO.write(sequences=record_list, handle="fasta_files\\human_one_record_genome.fasta",format="fasta")