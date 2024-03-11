needed_jump = int(input())
minimal_jump = needed_jump - 30
jump_count = 0
fail_break = False
success_break = False

while True:
    current_jump = int(input())
    jump_count += 1
    if current_jump <= minimal_jump:

        for fails in range(2):
            current_jump = int(input())
            jump_count += 1

            if current_jump > minimal_jump:
                break
            else:
                if fails >= 1:
                    fail_break = True
                    break

    if fail_break:
        break

    if current_jump > needed_jump:
        success_break = True
        break

    minimal_jump += 5

if success_break:
    print(f'Tihomir succeeded, he jumped over {minimal_jump}cm after {jump_count} jumps.')

elif fail_break:
    print(f'Tihomir failed at {minimal_jump}cm after {jump_count} jumps.')


