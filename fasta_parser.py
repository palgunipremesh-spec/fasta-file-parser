from Bio import SeqIO


def calculate_gc_content(sequence):
    """Calculate GC content as a percentage."""
    sequence = str(sequence).upper()

    if len(sequence) == 0:
        return 0.0

    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100


def parse_fasta(filename):
    """Parse a FASTA file and display ID, length and GC content."""

    for record in SeqIO.parse(filename, "fasta"):
        sequence_id = record.id
        sequence_length = len(record.seq)
        gc_content = calculate_gc_content(record.seq)

        print(f"ID: {sequence_id}")
        print(f"Length: {sequence_length}")
        print(f"GC Content: {gc_content:.2f}%")
        print()


if __name__ == "__main__":
    parse_fasta("example.fasta")
