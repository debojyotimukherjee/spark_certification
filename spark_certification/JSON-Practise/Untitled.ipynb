{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pyspark.sql import SparkSession\n",
    "spark = SparkSession.builder.getOrCreate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "read_File = spark.sparkContext.wholeTextFiles(\"example_2.json\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'file:/C:/Users/DMUKHERJEE/Documents/Debojyoti/Certification/JSON-Practise/example_2.json']"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "read_File.keys().collect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'{\\n    \"quiz\": {\\n        \"sport\": {\\n            \"q1\": {\\n                \"question\": \"Which one is correct team name in NBA?\",\\n                \"options\": [\\n                    \"New York Bulls\",\\n                    \"Los Angeles Kings\",\\n                    \"Golden State Warriros\",\\n                    \"Huston Rocket\"\\n                ],\\n                \"answer\": \"Huston Rocket\"\\n            }\\n        },\\n        \"sport\": {\\n            \"q1\": {\\n                \"question\": \"5 + 7 = ?\",\\n                \"options\": [\\n                    \"10\",\\n                    \"11\",\\n                    \"12\",\\n                    \"13\"\\n                ],\\n                \"answer\": \"12\"\\n            },\\n            \"q2\": {\\n                \"question\": \"12 - 8 = ?\",\\n                \"options\": [\\n                    \"1\",\\n                    \"2\",\\n                    \"3\",\\n                    \"4\"\\n                ],\\n                \"answer\": \"4\"\\n            }\\n        }\\n    }\\n}']"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "read_File.values().collect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "read_File_AsDF = spark.read.json(read_File.values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_json = spark.read.json(\"example_2.json\",multiLine=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- quiz: struct (nullable = true)\n",
      " |    |-- maths: struct (nullable = true)\n",
      " |    |    |-- q1: struct (nullable = true)\n",
      " |    |    |    |-- answer: string (nullable = true)\n",
      " |    |    |    |-- options: array (nullable = true)\n",
      " |    |    |    |    |-- element: string (containsNull = true)\n",
      " |    |    |    |-- question: string (nullable = true)\n",
      " |    |    |-- q2: struct (nullable = true)\n",
      " |    |    |    |-- answer: string (nullable = true)\n",
      " |    |    |    |-- options: array (nullable = true)\n",
      " |    |    |    |    |-- element: string (containsNull = true)\n",
      " |    |    |    |-- question: string (nullable = true)\n",
      " |    |-- sport: struct (nullable = true)\n",
      " |    |    |-- q1: struct (nullable = true)\n",
      " |    |    |    |-- answer: string (nullable = true)\n",
      " |    |    |    |-- options: array (nullable = true)\n",
      " |    |    |    |    |-- element: string (containsNull = true)\n",
      " |    |    |    |-- question: string (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_json.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_sport = df_json.select(\"quiz.maths.q1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- q1: struct (nullable = true)\n",
      " |    |-- answer: string (nullable = true)\n",
      " |    |-- options: array (nullable = true)\n",
      " |    |    |-- element: string (containsNull = true)\n",
      " |    |-- question: string (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_sport.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+---------+\n",
      "| question|\n",
      "+---------+\n",
      "|5 + 7 = ?|\n",
      "+---------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_sport.select(\"q1.question\").show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_movies = spark.read.format(\"com.databricks.spark.csv\").\\\n",
    "                           option(\"header\",\"true\").\\\n",
    "                           option(\"inferSchema\",\"true\").\\\n",
    "                           option(\"delimiter\",\"~\").\\\n",
    "                           load(\"movies.dat\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- movieID: integer (nullable = true)\n",
      " |-- movieName: string (nullable = true)\n",
      " |-- genres: string (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_movies.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_movies.createOrReplaceTempView(\"movies\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_movies_3_gen = spark.sql(\"select * from movies where \\\n",
    "                             length(genres) - length(replace(genres,'|',''))=2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+--------------------+\n",
      "|           movieName|              genres|\n",
      "+--------------------+--------------------+\n",
      "|Surviving the Gam...|Action|Adventure|...|\n",
      "|Back to the Futur...|Comedy|Sci-Fi|Wes...|\n",
      "|        Ronin (1998)|Action|Crime|Thri...|\n",
      "|Austin Powers: Th...|Action|Adventure|...|\n",
      "|       D.O.A. (1988)|Film-Noir|Mystery...|\n",
      "|War and Peace (1956)|   Drama|Romance|War|\n",
      "|Flight of the Pho...|Action|Adventure|...|\n",
      "|Same Old Song (On...|Comedy|Drama|Musical|\n",
      "| Matador, The (2005)|Comedy|Drama|Thri...|\n",
      "|Sense and Sensibi...|Comedy|Drama|Romance|\n",
      "|So I Married an A...|Comedy|Romance|Th...|\n",
      "|  Peeping Tom (1960)|Drama|Horror|Thri...|\n",
      "|Gold Rush, The (1...|Adventure|Comedy|...|\n",
      "| For the Boys (1991)|Comedy|Drama|Musical|\n",
      "|Jurassic Park III...|Action|Adventure|...|\n",
      "| Split Second (1992)|Action|Sci-Fi|Thr...|\n",
      "|Man of La Mancha ...|Adventure|Comedy|...|\n",
      "|Before the Devil ...|Crime|Drama|Thriller|\n",
      "|Apocalypse Now (1...|    Action|Drama|War|\n",
      "|     Twilight (1998)|Crime|Drama|Thriller|\n",
      "+--------------------+--------------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_movies_3_gen.select(\"movieName\",\"genres\").distinct().show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_movies_3_gen.select(df_movies_3_gen[\"movieName\"].alias(\"MOVIE NAME\"),\"genres\").write.mode(\"overwrite\").json(\"movies_3_gen\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
