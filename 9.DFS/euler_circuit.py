

adj = [
    [0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0]
]


def findRandomCircuit(here, circuit):
    for there in range(len(adj[here])):
        while adj[here][there] > 0:
            #양쪽 간선을 모두 지움
            adj[here][there] -= 1
            adj[there][here] -= 1
            findRandomCircuit(there, circuit)
    circuit.append(here)
    return circuit

new = findRandomCircuit(0, [])
new.reverse()
print(new)