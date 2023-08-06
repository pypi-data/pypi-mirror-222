import os
from collections import defaultdict
class frequenciesOfItems:

    def __init__(self, file_name, separator='\t'):
        self.file_path = os.path.join('statistics', file_name)
        self.separator = separator
        self.frequencies = defaultdict(int)
        self.calculate_frequencies()

    def calculate_frequencies(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                # split the line on comma to get a list of points
                points = line.strip().split(',')
                for point in points:
                    # make sure to strip any quotes and whitespace from the points
                    point = point.strip('\'" ')
                    self.frequencies[point] += 1

    def getFrequencies(self):
        return dict(self.frequencies)

# usage
def main():
    itemsFrequencies = frequenciesOfItems('PM24HeavyPollutionRecordingSensors.csv', ',')
    itemsFreqDictionary = itemsFrequencies.getFrequencies()
        
if __name__ == "__main__":
    main()
