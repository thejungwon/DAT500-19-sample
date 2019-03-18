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
| Group | [G1](https://group1-jp.wiktorskit.sigma2.no) | [G2](https://group2-jp.wiktorskit.sigma2.no) | [G3](https://group3-jp.wiktorskit.sigma2.no) | [G4](https://group4-jp.wiktorskit.sigma2.no) | [G5](https://group5-jp.wiktorskit.sigma2.no) | [G6](https://group6-jp.wiktorskit.sigma2.no) | [G7](https://group7-jp.wiktorskit.sigma2.no) | [G8](https://group8-jp.wiktorskit.sigma2.no) | [G9](https://group9-jp.wiktorskit.sigma2.no) | [G10](https://group10-jp.wiktorskit.sigma2.no) | [G11](https://group11-jp.wiktorskit.sigma2.no) | [G12](https://group12-jp.wiktorskit.sigma2.no) | [G13](https://group13-jp.wiktorskit.sigma2.no) | [G14](https://group14-jp.wiktorskit.sigma2.no) | [G15](https://group15-jp.wiktorskit.sigma2.no) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Status  | O | X | X | X | X | O | X | X | X | O | X | X | X | X | X |
| Jupyter | O | X | X | O | X | O | X | X | X | O | X | O | O | O | X |
| Spark   | O | X | O | X | O | O | X | O | X | O | X | X | X | X | X |

