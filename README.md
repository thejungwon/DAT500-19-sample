# DAT500-19-sample
UiS DAT500 sample code

## Getting Started
### Initial Setting
```
cd <YOUR-GROUP-FOLDER>
git clone https://github.com/thejungwon/dat500-19-sample.git
cd dat500-19-sample
wget https://www.dropbox.com/s/vofyl0uryectfyt/actors.list?dl=0
```
### (Option #1) Runing with regular python
```
python word_cnt.py <ABSOLUTE_PATH>/dat500-19-sample/actors.list <ABSOLUTE_PATH>/dat500-19-sample/output01
```

### (Option #2) Runing with regular spark-submit
```
spark-submit --verbose word_cnt.py <ABSOLUTE_PATH>/dat500-19-sample/actors.list <ABSOLUTE_PATH>/dat500-19-sample/output01
```

### (Option #3) Runing with Jupyter Notebook
- [word_cnt.ipynb](https://github.com/thejungwon/dat500-19-sample/blob/master/word_cnt.ipynb)


## Available Cluster for Each Group 
### Updated: Mon Mar 18 15:53:16 CET 2019
| Group | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14 | G15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Status  | O | X | X | X | X | O | X | X | X | O | X | X | X | X | X |
| Jupyter | O | X | X | O | X | O | X | X | X | O | X | O | O | O | X |
| Spark   | O | X | O | X | O | O | X | O | X | O | X | X | X | X | X |

