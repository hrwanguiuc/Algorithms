
import numpy as np 
import math


def solution(melons, boxes):
    if not melons or not boxes:
        return 0
    MAX = 0

    n = len(melons)
    m = len(boxes)
    for i in xrange(m):
        count = 0
        box_idx = i
        melon_idx = 0
        while box_idx < m and melon_idx < n:
            if boxes[box_idx] >= melons[melon_idx]:
                melon_idx += 1
                count += 1
            box_idx += 1
        MAX = max(MAX, count)
        if MAX == n:
            return MAX
    return MAX



def parseWords(input):
    # preprocessing for the invalid words
    #input = sys.stdin.readline()
    new_input = ''
    for char in input:
        if char.isalpha() or char == ' ':
            new_input += char

    new_input = new_input.lower()
    word_list = new_input.split()
    
    '''
    for i in xrange(len(tempstr)):
        s = tempstr[i]
        if not s.isalpha():
            new_s = ''
            for char in s:
                if char.isalpha():
                    new_s += char
            if new_s == '':
                tempstr.remove(s)
            else:
                tempstr[i] = new_s
    # 
    '''
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    print len(word_list)
    # word 'words'
    print word_dict['words'] if 'words' in word_dict else 0
    # each word with its counts
    for word in sorted(word_dict):
        print word + ' ' + str(word_dict[word])
    # word 'letters'
    print word_dict['letters'] if 'letters' in word_dict else 0
    # print a-z

    for word in word_list:
        temp_dict = dict.fromkeys([x for x in 'abcdefghijklmnopqrstuvwxyz'], 0)
        for char in word:
            temp_dict[char] += 1
        for char in sorted(temp_dict):
            print char + ' '+ str(temp_dict[char])


def eculidean(trainData, testData):

    return math.sqrt(sum((testData-trainData)**2))

def vote(k_idx, label_set, labels):
    temp = dict.fromkeys([label for label in label_set],0)

    for i in k_idx:
        temp[labels[i]] += 1
    return sorted(temp.items(), key = lambda x: x[1], reverse = True)[0][0]

def labelFinder(labels):
    res = set()
    for i in labels:
        res.add(i)
    return res


def knn(oldtrades, labels, newtrades):
    K = 3
    res = []
    oldtrades = np.array(oldtrades)
    newtrades = np.array(newtrades)
    label_set = labelFinder(labels)

    for i in xrange(len(newtrades)):
        distances = {}

        for j in xrange(len(oldtrades)):
            distances[j] = euclidean(oldtrades[j], newtrades[i])
        # find k-nearest neighbors' indices
        nearest_neighbors = sorted(neighbors_distance.items(),
                                       key = lambda x: x[1], reverse = False)[:K]
        k_idx = []
        for itm in nearest_neighbors:
            k_idx.append(itm[0])

        prediction = vote(k_idx, label_set, labels)
        res.append(prediction)

    return res


def drone_delivery(num_packages, delivery_sequence):
    if not delivery_sequence:
        return 0
    seq_array = []
    grid_names = []

    # find all names of the grid, store them at grid_names
    for i in xrange(num_packages):
        curr = delivery_sequence[i]
        temp = curr.split('-')
        grid_names.append(temp[0])
    # find all home number belongs to each grid, save the index of the home and its number in a tuple
    for i in xrange(len(grid_names)):
        grid_name = grid_names[i]
        temp_array = []
        for j in xrange(num_packages):
            curr = delivery_sequence[j]
            temp = curr.split('-')
            if temp[0] == grid_name:
                tup = (j, int(temp[1]))
                temp_array.append(tup)
        if temp_array in seq_array:
            continue
        seq_array.append(temp_array)
    res = 0
    print seq_array
    for seq in seq_array:
        time = calculation(seq)
        res += time

    return res+1


def calculation(array):
    time = 0
    n = len(array)
    prev_idx = 0
    prev_home = 1
    for tup in array:
        diff_idx = tup[0] - prev_idx
        diff_home = tup[1] - prev_home
        if diff_home + 1 > diff_idx:
            time += diff_home + 1 - diff_idx
        else: 
            time += 1

        prev_idx = tup[0]
        prev_home= tup[1]

    return time
def map():
    last = dict.fromkeys([name for name in grid_names], (0,1))
    


## Lamps
def lamp(grid_h,grid_w, x1,y1,x2,y2, start_x, start_y):
    
    h = grid_h
    w = grid_w
    grid = [['L' for x in xrange(w)] for y in xrange(h)]

    def helper(x, y):
        if x < 0 or x > m or y < 0 or y > n:
            return

        if grid[x][y] == 'L':
            grid[x][y] == 'X'
            if y+x1>=0 and y+x1 < w and x-y1>=0 and x-y1<h:
                helper(x,y-1)
            if y+x2>=0 and y+x2 < w and x-y2>=0 and x-y2<h:
                helper(x+1, y-1)

    helper(x, y)
    count = 0
    for i in xrange(h):
        for j in xrange(w):
            if grid[i][j] == 'L':
                count += 1
    return count

def calculation(matrix, start_share):
    prev = np.array(start_share)
    matrix = np.array(matrix)
    c = 0.000001
    diff = prev
    while not criteria(diff,c):
        curr = np.dot(prev, matrix)
        diff = abs(prev - curr)
        prev = curr
    res = prev
    for i in xrange(len(prev)):
        res[i] = round(prev[i],4)
    return res

def criteria(diff, c):
    for i in diff:
        if i > c:
            return False
    return True



def npdot(prev, switch_matrix):
    res = [0 for x in xrange(len(prev))]
    for i in xrange(len(switch_matrix[0])):
        temp_sum = 0
        for j in xrange(len(switch_matrix)):
            temp_sum += prev[j] * switch_matrix[j][i]
        res[i] = temp_sum
    return res

def difference(prev, curr):
    dif = [0 for x in xrange(len(prev))]
    for i in xrange(len(prev)):
        dif[i] = abs(prev[i] - curr[i])
    return dif


def main(share, matrix):
    prev = share 
    c = 0.000001
    diff = [1 for x in xrange(len(prev))]
    
    while not criteria(diff, c):
        curr = npdot(prev, matrix)
        diff = difference(prev, curr)
        prev = curr
    res = []
    for i in xrange(len(prev)):
        res.append(round(prev[i], 4))
    print res


    





if __name__ == '__main__':
    #melons = [1,3,2,5,2]
    #boxes = [1,1,1,2,5]
    #print solution(melons, boxes)
    #input = "This is !@a $#@!test,are%^@115you sure?!@# is this sure?"
    #parseWords(input)

    #delivery_sequence = ['1234-1','1235-1'] #['1234-1','1235-1', '1234-3', '1236-2', '1235-3', '1236-5']
    #['1234-1','1235-1', '1235-4', '1234-3']#['1234-1', '1235-1', '1236-2', '1235-3', '1234-2', '1236-3'] #['1234-1', '1235-1', '1235-3', '1234-2']
    #print drone_delivery(2, delivery_sequence)

    matrix = [[0.8,0.2],[0.1,0.9]]
    start_share = [0.4,0.6]
    #print calculation(matrix, start_share)
    main(start_share, matrix)



