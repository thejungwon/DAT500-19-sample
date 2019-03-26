# DAT500-19-sample
UiS DAT500 PySpark sample code.

Since the cluster is being deployed, if your cluster is not ready yet, you can practice in your local environment with following [this guide](https://github.com/thejungwon/dat500-19-sample/blob/master/pyspark-test.pdf).

## 1. Getting Started
### Installation
```
cd <YOUR-GROUP-FOLDER>
git clone https://github.com/thejungwon/dat500-19-sample.git
cd dat500-19-sample
wget https://www.dropbox.com/s/vofyl0uryectfyt/actors.list?dl=0
//or 
curl -L -o actors.list https://www.dropbox.com/s/vofyl0uryectfyt/actors.list\?dl\=1
```
### (Option #1) Running with regular Python
```
python word_cnt.py <ABSOLUTE_PATH>/dat500-19-sample/actors.list <ABSOLUTE_PATH>/dat500-19-sample/output01
```

### (Option #2) Running with spark-submit command

```
spark-submit --verbose word_cnt.py <ABSOLUTE_PATH>/dat500-19-sample/actors.list <ABSOLUTE_PATH>/dat500-19-sample/output01
```
You may want to set more configuration.
(Try this configuration later when you need performance analysis.)
```
spark-submit --verbose \
--executor-memory 1g \
--driver-memory 1g \
--conf spark.driver.memoryOverhead=1024m \
--conf spark.executor.memoryOverhead=1024m \
word_cnt.py <ABSOLUTE_PATH>/dat500-19-sample/actors.list <ABSOLUTE_PATH>/dat500-19-sample/output01
```

### (Option #3) Running with Jupyter Notebook
- [word_cnt.ipynb](https://github.com/thejungwon/dat500-19-sample/blob/master/word_cnt.ipynb)


## 2. Available Cluster for Each Group 
### Updated: Tue Mar 26 11:12:14 CET 2019
| Group | [G1](https://group1-jp.wiktorskit.sigma2.no) | [G2](https://group2-jp.wiktorskit.sigma2.no) | [G3](https://group3-jp.wiktorskit.sigma2.no) | [G4](https://group4-jp.wiktorskit.sigma2.no) | [G5](https://group5-jp.wiktorskit.sigma2.no) | [G6](https://group6-jp.wiktorskit.sigma2.no) | [G7](https://group7-jp.wiktorskit.sigma2.no) | [G8](https://group8-jp.wiktorskit.sigma2.no) | [G9](https://group9-jp.wiktorskit.sigma2.no) | [G10](https://group10-jp.wiktorskit.sigma2.no) | [G11](https://group11-jp.wiktorskit.sigma2.no) | [G12](https://group12-jp.wiktorskit.sigma2.no) | [G13](https://group13-jp.wiktorskit.sigma2.no) | [G14](https://group14-jp.wiktorskit.sigma2.no) | [G15](https://group15-jp.wiktorskit.sigma2.no) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Status  | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| Jupyter | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |
| Spark   | O | O | O | O | O | O | O | O | O | O | O | O | O | O | O |

## 3. Built With

* Python3
