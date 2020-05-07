def switch_to(to_argument, from_argument, item):
    # Dùng thay switch case từ điển key value
    switch_to = {
        1:
            ['To 1', item],
        2:
            _10_to_stuff(to_argument, _stuff_to_10(from_argument, item)),
        3:
            _10_to_stuff(to_argument, _stuff_to_10(from_argument, item)),
        4:
            _10_to_stuff(to_argument, _stuff_to_10(from_argument, item)),
        5:
            _10_to_stuff(to_argument, _stuff_to_10(from_argument, item)),
        6:
            _10_to_stuff(to_argument, _stuff_to_10(from_argument, item)),
        7:
            _10_to_stuff(to_argument, _stuff_to_10(from_argument, item)),
        8:
            _10_to_stuff(to_argument, _stuff_to_10(from_argument, item)),
        9:
            _10_to_stuff(to_argument, _stuff_to_10(from_argument, item)),
        10:
            _stuff_to_10(from_argument, item),
        16:
            _10_to_stuff(to_argument, _stuff_to_10(from_argument, item))
    }
    return switch_to.get(to_argument, 'Invalid input! ')


def _stuff_to_10(base, item):
    res = 0
    length = len(item)

    try:
        for i in range(length):
            _addStuff = {
                'A': 10,
                'B': 11,
                'C': 12,
                'D': 13,
                'E': 14,
                'F': 15
            }
            if item[i] in _addStuff:
                res += (_addStuff[item[i]] * (base**(length-i-1)))
            else:
                res += (int(item[i]) * (base**(length-i-1)))
    except:
        print('Found an incorrect correct input in _stuff_to_10!')
    return int(res)


def _10_to_stuff(base, item):
    inputNum = item

    try:
        _addStuff = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }

        # Mảng chuỗi output
        outStr = ''

        # Chia lấy dư và đưa phần tử vào đầu mảng
        while inputNum != 0:
            remainder = inputNum % base
            # Nếu hệ trên 10
            if remainder in _addStuff:
                outStr = str(_addStuff[remainder]) + outStr
            # outStr = outStr + str(remainder) là cộng vào cuối str dưới là cộng vào đầu
            else:
                outStr = str(remainder) + outStr
            inputNum = int(inputNum // base)

    except:
        print('Found an incorrect correct input in _10_to_stuff!')
    return outStr


def main():
    # Đọc file và trả về lỗi nếu không tìm thấy file
    try:
        filein = 'input.txt'
        fin = open(filein, 'r')

        # Parse input theo hàng
        lines = fin.read().splitlines()

        # Mảng chứa input
        numbers = []

        # Parse input theo dấu cách
        for item in lines:
            numbers.append(item.split(' '))

        fileout = '1_1712267.txt'
        fout = open(fileout, 'w+')

        for item in numbers:
            _from = int(item[1])
            _to = int(item[2])
            fout.write(str(switch_to(_to, _from, item[0]))+'\n')

    except:
        print('Cannot find ' + filein + ' or ' + fileout +
              '! Please try rename file or put file in source code folder!')


if __name__ == "__main__":
    main()
