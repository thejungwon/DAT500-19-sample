from __future__ import print_function

import sys
from operator import add
import pyspark

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)
    sc = pyspark.SparkContext(appName="word-count33")
    text_file = sc.textFile("file://"+sys.argv[1])
    counts = text_file.flatMap(lambda line: line.split(" ")) \
                 .map(lambda word: (word, 1)) \
                 .reduceByKey(lambda a, b: a + b)
    counts.saveAsTextFile(sys.argv[2])
    sc.stop()
