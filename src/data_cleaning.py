def remove_star(string):
    if '*' in string:
        string = string.replace('*','')
    return string

def change_to_inches(num):
    num = round((num / 100000) * 39370 , 0)
    return num

def str_to_number(time_str):
    if not isinstance(time_str, str):
        return 0
    minutes, sec, *_ = [int(x) for x in time_str.split(':')]
    return minutes + sec / 60

def count_winning_pairs(sample_1, sample_2):
    sample_1, sample_2 = np.array(sample_1), np.array(sample_2)
    n_total_wins = 0
    for x in sample_1:
        n_wins = np.sum(x > sample_2) + 0.5*np.sum(x == sample_2)
        n_total_wins += n_wins
    return n_total_wins

def wins_losses_to_num(res):
    if res == 'W':
        return 1
    else:
        return 0
    
