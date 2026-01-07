
def total_people(connections: list) -> int:
    """Return the total number of distinct people."""
    
    return len(set(p for connection in connections for p in connection))

def n_unique_connections(connections: list) -> int:
    """Return the number of unique undirected connections."""
    
    return len(set((a,b) if a<=b else (b,a) for a, b in connections))


def connection_dict(connections: list) -> dict:
    """Returns a dictionary with people as key and set of connected people."""
    
    
    conn_dict = {}
    for a, b in connections:
        conn_dict.setdefault(a, set()).add(b)
        conn_dict.setdefault(b, set()).add(a)
    return conn_dict
    

def people_with_at_least_n_connections(connections: list, n:int) -> set:
    """Return a set of people having at least two distinct connections."""
    
    

    return {person for person, connection in connection_dict(connections).items() if len(connection) >= n}
    
# People Connection Analysis
# You are given a list of string pair tuples connections, where each tuple (P1, P2) represents a bidirectional connection between two people.
# The pair (a, b) and (b, a) describe the same connection and should be counted only once.

# Implement the following functions:

# total_people(connections) -> int
# Returns the total number of distinct people appearing in the list.
# n_unique_connections(connections) -> int
# Returns the number of unique connections, counting (a, b) and (b, a) as one.
# connection_dict(connections) -> dict[str,set[str]] - returns a dictionary with people names as keys and a set of people who they are connected to.
# people_with_at_least_n_connections(connections,n) -> set[str]
# Returns a set of people that have at least two distinct connections.
# All functions should treat the input as an undirected graph.

# Example

# connections = [
#     ('Anu', 'Biju'),
#     ('Biju', 'Chandru'),
#     ('Emma', 'David'),
#     ('David', 'Emma'),
#     ('Anu', 'Chandru'),
#     ('Chandru', 'Anu'),
#     ('Chandru','Ram'),
#     ('Ravi','Anna'),
#     ('Rahul', 'Anna'),
#     ('Anna', 'Rahul'),
# ]
# Explanation

# total_people(connections) -> 9
# the people are ('Anna','Anu','Biju','Chandru','Emma','David','Ram','Ravi','Rahul')
# n_unique_connections(connections) -> 7
# total connections 10, duplicate connections 3 ('David','Emma'), ('Chandru','Anu'), ('Anna','Rahul')
# connection_dict(connections)
# {
#     'Anna': {'Rahul', 'Ravi'},
#     'Anu': {'Biju', 'Chandru'}, 
#     'Biju': {'Anu', 'Chandru'}, 
#     'Chandru': {'Anu', 'Biju', 'Ram'},
#     'David': {'Emma'},
#     'Emma': {'David'},
#     'Rahul': {'Anna'},
#     'Ram': {'Chandru'},
#     'Ravi': {'Anna'}
# }
# people_with_at_least_n_connections(connections, 2)
# {'Anna', 'Anu', 'Biju', 'Chandru'}

