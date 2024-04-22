
### Probando las capacidades de Bigquery 
#### Ejecutar la siguiente consulta :
select language,title,
sum(views) as views
from
bigquery-samples.wikipedia_benchmark.Wiki10B
group by  
language,title
order by views desc;