def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Running DNA analysis....")
        result = func(*args, **kwargs)
        print("Analysis complete!")
        return result
    return wrapper

@log_function_call
def analyze_dna(seq):
    def gc_content():
        sum = 0
        for i in seq.upper():
            if i in ["G", "C"]: sum+=1
        return sum
    gc=(gc_content()/len(seq))*100
    if gc > 50: kind = "GC rich"
    elif gc < 50: kind = "AT rich"
    else: kind = "balanced, 50% GC"
    print(f"The GC content is {gc:.2f}% and hence the sequence is {kind}")
    return gc

analyze_dna(input("Enter DNA sequence to be analyzed: "))