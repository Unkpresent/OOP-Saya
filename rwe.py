def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(idx + 1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

def find_median(input_list):
    sorted_list = sorted(input_list)
    n = len(sorted_list)
    if n % 2 == 0:
        return (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
    else:
        return sorted_list[n//2]

def find_mean(input_list):
    return sum(input_list) / len(input_list)

def find_mode(input_list):
    freq_dict = {}
    for num in input_list:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    max_freq = max(freq_dict.values())
    mode = [num for num, freq in freq_dict.items() if freq == max_freq]
    return mode


input_list = []
for i in range(10):
    nilai = int(input(f"Masukkan nilai ke-{i+1}: "))
    input_list.append(nilai)


selection_sort(input_list)

median = find_median(input_list)
print("Nilai tengah:", median)

mean = find_mean(input_list)
print("Nilai rata-rata:", mean)

mode = find_mode(input_list)
print("Modus:", mode)

