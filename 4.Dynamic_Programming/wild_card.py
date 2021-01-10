"""
다양한 운영체제에서 파일 이름의 일부만으로 파일 이름을 지정하는 방법이다.
패턴은 일반적인 팡리명과 비슷하지만 특수문자를 포함할 수 있는 문자열이다.
와일드카드 패턴은 앞에서 한 글자씩 파일명과 비교해서 모든 글자가 일치했을 때
해당 와일드카드 패턴이 파일명과 대응된다고 말합니다.
단, 패턴에 포함된 ?는 어떤 글자가와도 대응된다고 가정하며, *는 0글자 이상의
어떤 문자열에도 대응된다고 가정한다.
ex) help = he?p / *p* = help, papa
와일드 카드 패턴과 함께 파일명의 집합이 주어질 때, 그중 패턴에 대응되는
파일명들을 찾아내는 프로그램을 작성하라.

첫 줄에는 와일드카드 패턴 W가 주어진다.
그다음 줄에는 파일명의 수 n이 주어지고,
그 후 n줄에 하나씩 파일명이 주어진다.

출력에는 주어진 패턴에 대응되는 파일들의 이름을 한 줄에 하나씩 알파벳 순서대로 나열한다.
"""
cache = [[-1]*101]*101
pattern = str(input())
num_file = int(input())
file_list = []
for _ in range(num_file):
    file_list.append(str(input()))

"""
?는 모든 문자와 대응
*가 존재한다면 그 전까지 모든 글자와는 비교 안해도 돼
"""
def match(w, s):
    pos = 0
    # position이 와일드카드와 문자열의 길이보다 작고, 그 위치에서 와일드카드의 글자가 ?이거나 문자열의 글자가 대응되면 True
    # while문을 벗어나게 되면 fail
    while (pos < len(s) and pos < len(w) and (w[pos] == '?' or w[pos]==s[pos])):
        pos += 1
    
    #while문이 종료된 이유에 대해 판단

    #패턴의 끝에 도달한 경우 문자열도 끝났어야 대응된다
    if pos == len(w):
        return pos==len(s)
    
    #*를 만나서 끝난 경우, *에 몇 글자를 대응해야 할지 재귀호출하면서 확인한다.
    if w[pos]=='*':
        for i in range(pos, len(s)):
            if match(w[pos+1:], s[i+pos:]):
                return True
    # 그 외 모두 False
    return False

def match2(w, s, W, S):
    ret = cache[w][s]
    if ret != -1 : return ret
    while (w < len(W[w]) and s < len(S[s]) and (W[w]=='?' or W[w]==S[s])):
        w += 1
        s += 1
    
    if(w==len(W)) :
        ret = len(S)
        return ret
    
    if W[w]=='*':
        for i in range(s, len(S)):
            if(match2(w+1, s+i, W, S)):
                ret = 1
                return ret
    ret = 0
    return ret 