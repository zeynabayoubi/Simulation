import matplotlib.pyplot as plt


def The_list_of_total_self_avoiding_tracks (N):

    if N==1:
        return [ [ [0,0] , [1,0] ] ]
    
    else:
        list_of_total_self_avoiding_tracks = []
        
        for i in The_list_of_total_self_avoiding_tracks (N-1) :
            
            for s in [ [1,0] , [0,-1] , [0,1] , [-1,0] ]:
                
                if len(i) == 2 and type( i[1] ) != type( [] ) :

                    m = [ i[0] + s[0]  ,  i[1] + s[1] ]
                    if m not in [i]:
                        list_of_total_self_avoiding_tracks . append ( [i] + [m] )

                else:
                    m = [ i[-1][0] + s[0]  ,  i[-1][1] + s[1] ]
                    if m not in i :
                        list_of_total_self_avoiding_tracks . append ( i + [m] )

        return list_of_total_self_avoiding_tracks


number_of_total_self_avoiding_tracks = []
self_avoiding_tracks_Ralative = []
N = list(range(1,11))
for i in range(1,11):
    s = 4 * len(The_list_of_total_self_avoiding_tracks(i))
    number_of_total_self_avoiding_tracks.append(s)
    self_avoiding_tracks_Ralative.append(s/(4**i))

print(number_of_total_self_avoiding_tracks)

plt.scatter(N , number_of_total_self_avoiding_tracks )
plt.plot(N , number_of_total_self_avoiding_tracks )
plt.xlabel('number of steps')
plt.ylabel('total number of self avoiding tracks ')
plt.xticks(N)
plt.show()

plt.scatter(N , self_avoiding_tracks_Ralative )
plt.plot(N , self_avoiding_tracks_Ralative )
plt.xlabel('number of steps')
plt.ylabel('number of SAW /number of NRW')
plt.xticks(N)
plt.show()

