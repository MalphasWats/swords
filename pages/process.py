

with open('items.markdown', 'r') as f:
    text = f.read();
    
lines = text.splitlines()

max_len_name = 0
max_len_stat = 0
max_len_price = 0
with open('items_.markdown', 'w') as f:
    for l in lines:
        cells = l.split('|')
        len_name = len(cells[1])
        len_stat = len(cells[2])
        len_price = len(cells[3])
        if len_name > max_len_name:
            max_len_name = len_name
        if len_stat > max_len_stat:
            max_len_stat = len_stat
        if len_price > max_len_price:
            max_len_price = len_price

    for l in lines:
        cells = l.split('|')
        f.write("|%s|%s|%s|\n" % (cells[1].ljust(max_len_name), cells[2].center(max_len_stat), cells[3].center(max_len_price) ))