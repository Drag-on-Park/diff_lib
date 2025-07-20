from difflib import SequenceMatcher, context_diff,ndiff
###
"""
코드        뜻
'- '        시퀀스 1에만 있는 줄
'+ '        시퀀스 2에만 있는 줄
'  '        두 시퀀스에 공통인 줄
'? '        두 입력 시퀀스에 없는 줄
"""


# 유사도
def similar(a,b):
    return round(float(SequenceMatcher(None, a, b).ratio()),2) * 100

print(similar('서울시 도봉구', '서울시 성동구'))

with open('samplefile_1.txt', 'r') as f1:
          with open('samplefile_2.txt', 'r') as f2:
                 diff = context_diff(f1.readlines(),f2.readlines(), fromfile = 'f1', tofile = ('f2'))
                 for line in diff:
                        print(line)
def diff_word_file(file1_path:str, file2_path:str):
       # 파일읽기
        with open(file1_path, 'r', encoding='utf-8') as f1:
              text1 = f1.read()
        with open(file2_path, 'r', encoding='utf-8') as f2:
              text2 = f2.read()

        # 단어 단위로 나누기
        word1 = text1.split()
        word2 = text2.split()

        # 비교
        diff = ndiff(word1,word2)

        # 결과 정리
        added = []
        removed = []

        for word in diff:
                if word.startswith("+ "):
                      added.append(word[2:])
                elif word.startswith("- "):
                      removed.append(word[2:])
        print("_____________________추가된 단어:")
        print(added)
        print("\n_____________________삭제된 단어:")
        print(removed)

diff_word_file('word_1.word', 'word_2.word')


          
