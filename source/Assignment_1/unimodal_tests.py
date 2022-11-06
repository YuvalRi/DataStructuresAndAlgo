from UnimodalArray import unimodal_index

if __name__ == "__main__":
    print(unimodal_index(A=[1,2,3], n = 3) == 2)
    print(unimodal_index(A=[3,2,1], n=len([3,2,1])) == 0)
    print(unimodal_index(A=[1,3,7,10,8,5,3], n=len([1,3,7,10,8,5,3])) == 3)
    print(unimodal_index(A=[1,3,5,4,2], n=len([1,3,5,4,2])) == 2)
    print(unimodal_index(A=[1,6], n=len([1,6])) == 1)
    print(unimodal_index(A=[3], n=len([3])) == 0)
    print(unimodal_index(A=[8,6,4,2,1], n=len([8,6,4,2,1])) == 0)
    print(unimodal_index(A=[9,2,14,13,12,10], n=len([8,6,4,2,1])) == 2)





