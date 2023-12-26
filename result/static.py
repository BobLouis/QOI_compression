import os
import re


def read_and_analyze_files(directory):
    total_qoi_count = 0
    less_than_50_count = 0

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as file:
                data = file.read()
                # Remove the "Grand total" and "Total for images" sections
                data = re.sub(r'## Total for images.+\n(\s+.+\n)+',
                              '', data, flags=re.MULTILINE)
                data = re.sub(r'# Grand total for images.+\n(\s+.+\n)+',
                              '', data, flags=re.MULTILINE)

                # Find all qoi rate values
                qoi_rates = re.findall(
                    r'qoi:\s*(?:\S+\s+){5}(\d+\.\d+)%', data)

                print(qoi_rates)
                # Update counts
                total_qoi_count += len(qoi_rates)
                less_than_50_count += sum(
                    1 for rate in qoi_rates if float(rate) < 50)

    if total_qoi_count == 0:
        return 0

    proportion_less_than_50 = (less_than_50_count / total_qoi_count) * 100
    print(less_than_50_count, total_qoi_count)
    return proportion_less_than_50


# Replace 'your_directory_path' with the path of your directory
directory_path = '.'
proportion = read_and_analyze_files(directory_path)
print(f"Proportion of qoi rates less than 50%: {proportion}%")
