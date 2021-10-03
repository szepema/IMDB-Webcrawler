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