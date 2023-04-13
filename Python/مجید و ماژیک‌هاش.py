n = int(input())
markers = [int(i) for i in input().split()]
markers_dic = dict()
for marker in markers:
    if marker in markers_dic.keys():
        markers_dic[marker] += 1
    else:
        markers_dic[marker] = 1
markers_dic = dict(
    sorted(markers_dic.items(), key=lambda item: item[0]))
markers_dic = sorted(markers_dic.items(), key=lambda item: item[1])
print(markers_dic[0][0])
