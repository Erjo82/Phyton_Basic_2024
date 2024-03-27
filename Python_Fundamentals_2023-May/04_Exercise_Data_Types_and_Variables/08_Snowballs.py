snowballs = int(input())
weight = 0
time = 0
quality = 0
result = 0
for current_snowball in range(snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_result = int((current_weight / current_time) ** current_quality)
    if current_result > result:
        result = current_result
        weight = current_weight
        time = current_time
        quality = current_quality
print(f'{weight} : {time} = {result} ({quality})')
