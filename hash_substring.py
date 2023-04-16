# python3
global B, Q
B=13
Q=256
def read_input():
    tekstaievade = input()
    if tekstaievade.__contains__("I"):
        pattern = str(input())
        text = str(input())
        return (pattern, text)
        
        
    elif tekstaievade.__contains__("F"):
        
        fails = "tests/06"
        with open(fails,"r") as f:
            pattern = str(f.readline().rstrip())
            text = str(f.readline().rstrip())
            return (pattern, text)
                

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_hash(pattern):
    n = len(pattern)
    hash_res = 0
    for i in range(n):
        hash_res = (Q * hash_res + ord(pattern[i])) % B
    return hash_res

def get_occurrences(pattern, text):
     
    pattern_len = len(pattern)
    text_len = len(text)
    multip = 1
    pattern_hash = 0
    text_hash = 0

    for f in range(pattern_len-1):
        multip = (multip*Q) % B
     
    result = []
    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_len])
    for i in range(text_len-pattern_len+1):
        if pattern_hash == text_hash:
            for k in range(pattern_len):
                if pattern[k] != text[i+k]:
                    break
          
            if k+1 == pattern_len:
                    result.append(i)
        
        if i < text_len-pattern_len:

            text_hash = (Q*(text_hash-ord(text[i])*multip)+ord(text[i+pattern_len])) % B
            if text_hash < 0:
                text_hash = text_hash + B

    return result
           
# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

