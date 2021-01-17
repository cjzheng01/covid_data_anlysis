# COVID-19 Data Collection and Visualization

In this project, data were scraped from certain COVID-19 data summary websites. The number of confirmed cases (of the COVID-19 virus) in China varied across the country and were categorized accordingly to the severeness (or number of cases), and were presented by varying shades of a colour (on an interactive map), with the darker shade indicating a high number of cases and the lighter shade indicating a low number of cases.

Libraries used in this project were ``requests``, ``map_draw``, ``etree``, ``openpyxl``, ``pyecharts`` , and ``json``.

Except the file ``translation.py``, the core code of thsi project is not avaliable at this point in time. The results of this project is availiable at my personal website, and can be accessed
<a href="https://student.cs.uwaterloo.ca/~j243zhen/coronavirus/">here<a>. This webiste would be updated regularly, and all csv, xlsx, and json file could be downloaded for further analysis. <br>
Sample EXCEL file: <br>
 <a href="https://student.cs.uwaterloo.ca/~j243zhen/coronavirus/data/data.xlsx">EXCEL Workbook for COVID-19 Statistics<a>

The number of confirmed cases (of the COVID-19 virus) in China varied across the country and were categorized accordingly to the severeness (or number of cases), and were presented by varying shades of a colour (on an interactive map), with the darker shade indicating a high number of cases and the lighter shade indicating a low number of cases. 

Maps are also available on my site. However, please note that since the displaying language of the library ``pyecharts`` was Chinese, so some label of the maps are in Chinese. Only China's detailed data for each city is available on the [site](https://voice.baidu.com/act/newpneumonia/newpneumonia/) was scraped , so the visualization through maps are only available for China's COVID-19 statistics now. I am actively looking for new website to replace the one I am currently using.

These visualizations are inspired by a project on gitee.com
