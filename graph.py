import matplotlib.pyplot as plt

def graph(lst):
    seasons = len(lst)
    length = sum(len(row) for row in lst)
    x = 0
    
    for season in range(1, seasons+1):
        episodes = lst[season-1]
        x_list = []
        for i in range(1, len(episodes)+1):
            x_list.append(x+i)
        plt.bar(x_list, episodes)
        x = x + i
    plt.xlabel("Episodes")
    plt.ylabel("Ratings")
    # plt.xticks(range(1, length+1))
    plt.yticks(range(11))
    plt.legend()
    plt.show()

if __name__ == "__main__":
    xdd = [[5, 1, 3, 8, 9, 10], [9, 5, 6, 7, 8, 1, 2, 6, 4, 6, 5], [4, 5, 9, 7, 8, 6, 2, 4, 5, 9, 8, 4, 6, 7, 3, 2, 1], [5, 8, 6, 8, 9, 7, 5, 6, 1, 2, 3, 4, 5, 6, 8, 9, 10]]
    graph(xdd)
