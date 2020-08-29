# 104 人力銀行爬蟲

簡易的 104 爬蟲程式，方便快速瀏覽職缺。

## Quick Start

### Example

搜尋 Data scientist  
最低薪資 40000/月  
最高薪資 80000/月  
地區 台北市(6001001000)  

```
python 104-Crawler \
    --key_word "Data scientist" \
    --min_salary 40000 \
    --max_salary 80000 \
    --area "6001001000"
```

## Result

爬取結果儲存至 104-Crawler\output

|jobName|salaryLow|salaryHigh|appearDate|jobAddrNoDesc|jobAddress|applyDesc|custName|coIndustryDesc|
|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|自然語言處理工程師 / NLP engineer|0040000|0080000|20200820|台北市松山區|復興北路167號14樓之4|11~30人應徵|萬達人工智慧科技股份有限公司|電腦軟體服務業|
|Research Scientist|0040000|0065000|20200824|台北市中正區|新生南路一段158號6樓|30人以上應徵|柏瑞克股份有限公司|化學原料製造業|
|Python 後端資料工程師|0045000|0070000|20200827|台北市內湖區||11~30人應徵|九七科技股份有限公司|網際網路相關業|
|全端工程師 Full Stack Developer|0050000|0080000|20200810|台北市中山區|長春路152號3樓|0~5人應徵|圍棋人科技股份有限公司|電腦軟體服務業|
