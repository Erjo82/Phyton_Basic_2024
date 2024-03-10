v = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

debit_pipe1 = pipe_1 * hours
debit_pipe2 = pipe_2 * hours
all_debit = debit_pipe1 + debit_pipe2
percent_debit_pipe1 = (debit_pipe1 / all_debit) * 100
percent_debit_pipe2 = (debit_pipe2 / all_debit) * 100
full_pool_percent = (all_debit / v) * 100

if v < all_debit:
    litre_after_full = all_debit - v
    print(f'For {hours} hours the pool overflows with {litre_after_full:.2f} liters.')

else:
    print(
        f'The pool is {full_pool_percent:.2f}% full. '
        f'Pipe 1: {percent_debit_pipe1:.2f}%. '
        f'Pipe 2: {percent_debit_pipe2:.2f}%.')
