n, x, k = map(int, input().split())
networks = [input() for _ in range(n)]

#current_network = x - 1
#for _ in range(k):
#    current_network = (current_network + 1) % n
#final_network = networks[current_network]
#print(final_network)

print(networks[(x+(k%n))%n-1])
