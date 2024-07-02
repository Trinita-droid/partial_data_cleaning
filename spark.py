from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

def main():
    # Create a Spark session
    spark = SparkSession.builder.appName("WordCount").getOrCreate()

    # Define the file path
    file_path = r"C:\Users\TJO1COB\Documents\2_sprints.txt"  # Change this to your text file path
    # Read the text file
    text_rdd = spark.sparkContext.textFile(file_path)

    # Split lines into words and count each word
    word_counts = text_rdd.flatMap(lambda line: line.split()) \
                        .map(lambda word: (word, 1)) \
                        .reduceByKey(lambda a, b: a + b)

    # Sort word counts in descending order
    sorted_word_counts = word_counts.sortBy(lambda x: x[1], ascending=False)

    # Collect the top 10 words and print them
    top_10_words = sorted_word_counts.take(10)
    for word, count in top_10_words:
        print(f"{word}: {count}")

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()

# --------------

from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

def main():
    # Create a Spark session
    spark = SparkSession.builder.appName("WordCount").getOrCreate()

    # Define the file path
    file_path = r"C:\Users\TJO1COB\Documents\2_sprints.txt"  # Change this to your text file path
    # Read the text file
    text_rdd = spark.sparkContext.textFile(file_path)

    # Split lines into words and count each word
    word_counts = text_rdd.flatMap(lambda line: line.split()) \
                        .map(lambda word: (word, 1)) \
                        .reduceByKey(lambda a, b: a + b)

    # Sort word counts in descending order
    sorted_word_counts = word_counts.sortBy(lambda x: x[1], ascending=False)

    # Collect the top 10 words and print them
    top_10_words = sorted_word_counts.take(10)
    for word, count in top_10_words:
        print(f"{word}: {count}")

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()
