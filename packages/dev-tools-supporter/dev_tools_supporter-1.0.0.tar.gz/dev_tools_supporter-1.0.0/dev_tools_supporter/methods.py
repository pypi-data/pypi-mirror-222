import time


def sout(content, color='white', **kwargs):
    """
        This function redefines the print function of python, which allow you 
        to print line with particular color (red, green, yellow)

        Note that you just can see the file change in Normal Terminal (Git Bash does not work)
    """
    if 'end' in kwargs:
        kwargs['end'] = kwargs.get('end') + '\033[0m'
    else:
        kwargs['end'] = '\033[0m\n'

    if color == 'green':
        line_color = '\033[92m'
    elif color == 'red':
        line_color = '\033[91m'
    elif color == 'yellow':
        line_color = '\033[93m'
    else:
        line_color = '\033[0m'

    print(f'{line_color}{content}', **kwargs)


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    # Move cursor up one line
    print('\033[F', end='')
    print(f'\r{prefix} |{bar}| {percent}% | {iteration} over {total}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# if __name__ == '__main__':
#     max_iter = 100

#     # Initial call to print 0% progress
#     printProgressBar(
#         0, max_iter, prefix='Process:', suffix='completed', length=50)

#     for i in range(max_iter):
#         time.sleep(0.001)
#         # print('i = ', i)
#         printProgressBar(
#             i+1, max_iter, prefix='Process:', suffix='completed', length=50)
