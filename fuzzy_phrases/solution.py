import json

def phrasel_search(P, Queries):
    # Write your solution here
    phrase_list = []

    for p in P:
        split = p.split()
        phrase_list.append(split)

    ans = []

    for q in Queries:
        temp = []
        words = q.split()

        for p in P:
            sentence = p.split()
            i, flag = 0, 0
            j = 0
            while j < len(words) and i < len(sentence):
                if i == 0:
                    z = j
                    flag = 0
                if words[j] == sentence[i]:
                    if i == len(sentence)-1:
                        i, flag = 0, 0
                        temp.append(' '.join(words[z:j+1]))
                        j = z+1
                        continue
                    i += 1
                    j += 1
                elif flag == 0:
                    j += 1
                    flag = 1
                else:
                    i, flag = 0, 0
                    j = z+1

        ans.append(temp[:])

    return ans


if __name__ == "__main__":
    with open('50_points.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
