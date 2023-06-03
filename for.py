list = [ 1, 2, 3, 4, 5]

def test( list ) :
    for i in range(len(list) - 1) : 
        for j in range(i+1, len(list)) :
            if list[i] + list[j] == 5:
                return True

    return False

result = test(list)
print(result)