queries = ['ab', 'a', 'abc']
strings = ['ab', 'ab', 'a', 'a', 'abc']


def sparseArray(queries, strings):
    # newArr = []
    # for i in range(len(queries)):
    #     newArr.append(0)
    # for string in strings:
    #     for index, query in enumerate(queries, 0):
    #         if(query == string):
    #             newArr[index] = newArr[index]+1
    # return newArr

    #Alternate solution
    results = []
    for item in queries:
        results.append(strings.count(item))
    return results


print(sparseArray(queries, strings))
