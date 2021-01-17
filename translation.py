import pandas as pd
'''
As mentioned in README.md, the data are scraped from a Chinese COVID-19 summary website, so it is necessary to translate
 all data to English for more people's convenience. 
'''
def xlsx_translate():
    xls = pd.ExcelFile('data.xlsx')
    df_china = pd.read_excel(xls, 'COVID-19 in China')
    df_asia = pd.read_excel(xls, 'Asia')
    df_europe = pd.read_excel(xls, 'Europe')
    df_africa = pd.read_excel(xls, 'Africa')
    df_oceania = pd.read_excel(xls, 'Oceania')
    df_na = pd.read_excel(xls, 'North America')
    df_sa = pd.read_excel(xls, 'South America')
    df_others = pd.read_excel(xls, 'Others')
    df_popular = pd.read_excel(xls, 'Popular')

    df_china_translate = ['Tibet', 'Macao', 'Qinghai', 'Taiwan', 'Hong Kong', 'Guizhou', 'Jilin', 'Xinjiang', 'Ningxia', 'Inner Mongolia', 'Gansu', 'Tianjin', 'Shanxi', 'Liaoning', 'Heilongjiang', 'Hainan', 'Hebei', 'Shaanxi', 'Yunnan', 'Guangxi', 'Fujian', 'Shanghai', 'Beijing', 'Jiangsu', 'Sichuan', 'Shandong', 'Jiangxi',  'Chongqing', 'Anhui', 'Hunan', 'Henan', 'Guangdong', 'Zhejiang', 'Hubei']
    df_asia_translate = ['Tajikistan', 'United Arab', 'Emirates', 'Yemen', 'Laos', 'Myanmar', 'Syria', 'East Timor', 'Kyrgyzstan', 'Uzbekistan', 'Kazakhstan', 'Turkey', 'Mongolia', 'Cyprus', 'Brunei', 'Bangladesh', 'Maldives', 'Bhutan', 'Palestine', 'Saudi Arabia', 'Jordan', 'Indonesia', 'Armenia', 'Qatar', 'Azerbaijan', 'Georgia', 'Pakistan', 'Oman', 'Afghanistan', 'Bahrain', 'Kuwait', 'Iraq', 'Lebanon', 'Iran', 'India', 'Philippines', 'Sri Lanka', 'Cambodia', 'Nepal', 'Vietnam', 'South Korea', 'Malaysia', 'Japan', 'Singapore', 'Thailand']
    df_europe_translate = ['Channel Islands', 'lsle of Man', 'Montenegro', 'Faroe Islands','Albania','Bulgaria','Moldova','Malta','Slovakia','Vatican','Serbia','Gibraltar','Liechtenstein', 'Bosnia and Herzegovina','Hungary','Slovenia','Poland','Ukraine','Latvia','Portugal','Andorra','Czech','Ireland','Luxembourg',
'San Marino', 'Monaco','Iceland','Belarus','Lithuania','Netherlands','Estonia','Denmark','Romania','Northern Macedonia','Norway','Greece','Switzerland', 'Croatia','Austria','Belgium','Spain','Sweden','Russia','UK','Italy','Finland','Germany', 'France']
    df_africa_translate = ['Lesotho', 'Comoros', 'Sao Tome and Principe', 'South Sudan', 'Malawi', 'Burundi', 'Sierra Leone', 'Botswana', 'Guinea-Bissau', 'Mali', 'Libya', 'Mozambique', 'Eritrea', 'Uganda', 'Angola', 'Madagascar', 'Zimbabwe', 'Cape Verde', 'Niger', 'Chad', 'Mauritius', 'Zambia', 'Djibouti', 'Gambia', 'Benin', 'Somalia', 'Florida', 'Liberia', 'Mayotte', 'Colombia', 'Central African Republic', 'Seychelles', 'Equatorial Guinea', 'Namibia', 'Rwanda', 'Swaziland', 'Mauritania', 'Sudan', 'Guinea', 'Ethiopia', 'Kenya', 'Gabon', 'Ghana', 'Reunion Island', 'Cote d\'Ivoire', 'Congo (DRC)', 'Burkina Faso', 'Togo', 'Cameroon', 'South Africa', 'Tunisia', 'Senegal', 'Morocco', 'Nigeria', 'Egypt', 'Algeria']
    df_oceania_translate = ['Micronesia', 'Independent State of Samoa', 'Republic of Vanuatu', 'Marshall Islands', 'Wallis and Futuna Islands', 'Solomon Islands', 'Papua New Guinea', 'New Caledonia', 'Fiji', 'French Polynesia', 'New Zealand', 'Australia']
    df_na_translate = ['Saint Pierre', 'Bermuda', 'The British Virgin Islands', 'Anguilla', 'Grenada', 'Saint Kitts and Nevis', 'Turks and Caicos Islands', 'Belize', 'Dominica', 'Montserrat', 'Haiti', 'Salvador', 'Nicaragua', 'Barbados', 'Greenland', 'Bahamas', 'Guadeloupe', 'Cayman Islands', 'Aruba', 'Curacao', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Antigua and Barbuda', 'Guatemala', 'Trinidad and Tobago', 'Cuba', 'Honduras', 'Saint Martin', 'St. Barthelemy', 'Jamaica', 'Panama', 'Martinique', 'Costa Rica', 'Dominica', 'Mexico', 'Canada', 'United States']
    df_sa_translate = ['Malvinas Islands', 'Guyana Cooperative Republic', 'Suriname', 'Uruguay', 'Venezuela', 'Bolivia', 'French Guiana', 'Paraguay', 'Colombia', 'Peru', 'Argentina', 'Chile', 'Ecuador', 'Brazil']
    df_others_translate = ['Diamond Princess Cruise']
    df_popular_translate = ['Turkey', 'Iran', 'Netherlands', 'Belgium', 'Spain', 'United Kingdom', 'Italy', 'Germany', 'France', 'United States']
    for i in range(len(df_china)):
        df_china.loc[i, 'Province'] = df_china_translate[i]
    for i in range(len(df_asia)):
        df_asia.loc[i, 'Country'] = df_asia_translate[i]
    for i in range(len(df_europe)):
        df_europe.loc[i, 'Country'] = df_europe_translate[i]
    for i in range(len(df_africa)):
        df_africa.loc[i, 'Country'] = df_africa_translate[i]
    for i in range(len(df_oceania)):
        df_oceania.loc[i, 'Country'] = df_oceania_translate[i]
    for i in range(len(df_na)):
        df_na.loc[i, 'Country'] = df_na_translate[i]
    for i in range(len(df_sa)):
        df_sa.loc[i, 'Country'] = df_sa_translate[i]
    for i in range(len(df_others)):
        df_others.loc[i, 'Country'] = df_others_translate[i]
    for i in range(len(df_popular)):
        df_popular.loc[i, 'Country'] = df_popular_translate[i]

    with pd.ExcelWriter('data.xlsx') as writer:
        df_china.to_excel(writer, 'COVID-19 in China', index=False)
        df_asia.to_excel(writer, 'Asia', index=False)
        df_europe.to_excel(writer, 'Europe', index=False)
        df_africa.to_excel(writer, 'Africa', index=False)
        df_oceania.to_excel(writer, 'Oceania', index=False)
        df_na.to_excel(writer, 'North America', index=False)
        df_sa.to_excel(writer, 'South America', index=False)
        df_others.to_excel(writer, 'Others', index=False)
        df_popular.to_excel(writer, 'Popular', index=False)

    df_china.to_csv('csv/COVID-19inChina.csv', index=False)
    df_asia.to_csv('csv/Asia.csv', index=False)
    df_europe.to_csv('csv/Europe.csv', index=False)
    df_africa.to_csv('csv/Africa.csv', index=False)
    df_oceania.to_csv('csv/Oceania.csv', index=False)
    df_na.to_csv('csv/North America.csv', index=False)
    df_sa.to_csv('csv/South America.csv', index=False)
    df_others.to_csv('csv/Others.csv', index=False)
    df_popular.to_csv('csv/Popular.csv', index=False)

    print("Done.")







