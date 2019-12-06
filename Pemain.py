class Pemain :
    def __init__(self ,pemain):
        self.pemain = pemain

    def bubbleSort(self , rating,nama):
        for passnum in range(len(rating)-1,0,-1):
            for i in range(passnum):
                if rating[i]>rating[i+1]:
                    temp = rating[i]
                    rating[i] = rating[i+1]
                    rating[i+1] = temp
                    temp1 = nama[i]
                    nama[i] = nama[i+1]
                    nama[i+1] = temp1
    def proses(self):
     c = []
     d = []
     for i in range(len(self.pemain)) :
        for j in self.pemain[i][0] :
            d.append(j)
            c.append(self.pemain[i][0][j][2])
     self.bubbleSort(c , d)
     self.nama = d

    def show(self):
        self.proses()
        for i in self.nama :
         print(i)