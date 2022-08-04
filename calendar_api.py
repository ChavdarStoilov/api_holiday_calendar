import requests


def specify_date_func(the_data, the_month):
    counter = 0
    matching = 0
    for _ in the_data:
        specify_date = str(the_data[counter]['date']).split("-")
        if specify_date[1] == the_month:
            print(f"\n{the_data[counter]['date']}:\n"
                  f"The holidays is: {the_data[counter]['name']}")
            matching += 1
        counter += 1

    if matching == 0:
        print("\nThere no have holiday")


def normal_date_fun(the_data):
    counter = 0
    for _ in the_data:
        print(f"\n{the_data[counter]['date']}:\n"
              f"The holidays is: {the_data[counter]['name']}")
        counter += 1


def response_func(years, month, code):
    all_country = {'Andorra': 'AD'
        , 'Albania': 'AL', 'Argentina': 'AR', 'Austria': 'AT', 'Australia': 'AU', 'Åland Islands': 'AX',
                   'Bosnia and Herzegovina': 'BA'
        , 'Barbados': 'BB', 'Belgium': 'BE', 'Bulgaria': 'BG', 'Benin': 'BJ', 'Bolivia': 'BO', 'Brazil': 'BR',
                   'Bahamas': 'BS', 'Botswana': 'BW'
        , 'Belarus': 'BY', 'Belize': 'BZ', 'Canada': 'CA', 'Switzerland': 'CH', 'Chile': 'CL', 'China': 'CN',
                   'Colombia': 'CO'
        , 'Costa Rica': 'CR', 'Cuba': 'CU', 'Cyprus': 'CY', 'Czechia': 'CZ', 'Germany': 'DE', 'Denmark': 'DK',
                   'Dominican Republic': 'DO'
        , 'Ecuador': 'EC', 'Estonia': 'EE', 'Egypt': 'EG', 'Spain': 'ES', 'Finland': 'FI', 'Faroe Islands': 'FO',
                   'France': 'FR'
        , 'Gabon': 'GA', 'United Kingdom': 'GB', 'Grenada': 'GD', 'Guernsey': 'GG', 'Gibraltar': 'GI',
                   'Greenland': 'GL', 'Gambia': 'GM'
        , 'Greece': 'GR', 'Guatemala': 'GT', 'Guyana': 'GY', 'Honduras': 'HN', 'Croatia': 'HR', 'Haiti': 'HT',
                   'Hungary': 'HU', 'Indonesia': 'ID'
        , 'Ireland': 'IE', 'Isle of Man': 'IM', 'Iceland': 'IS', 'Italy': 'IT', 'Jersey': 'JE', 'Jamaica': 'JM',
                   'Japan': 'JP', 'South Korea': 'KR'
        , 'Liechtenstein': 'LI', 'Lesotho': 'LS', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Latvia': 'LV',
                   'Morocco': 'MA', 'Monaco': 'MC', 'Moldova': 'MD'
        , 'Montenegro': 'ME', 'Madagascar': 'MG', 'North Macedonia': 'MK', 'Mongolia': 'MN', 'Montserrat': 'MS',
                   'Malta': 'MT', 'Mexico': 'MX'
        , 'Mozambique': 'MZ', 'Namibia': 'NA', 'Niger': 'NE', 'Nigeria': 'NG', 'Nicaragua': 'NI', 'Netherlands': 'NL',
                   'Norway': 'NO', 'New Zealand': 'NZ'
        , 'Panama': 'PA', 'Peru': 'PE', 'Papua New Guinea': 'PG', 'Poland': 'PL', 'Puerto Rico': 'PR', 'Portugal': 'PT',
                   'Paraguay': 'PY', 'Romania': 'RO'
        , 'Serbia': 'RS', 'Russia': 'RU', 'Sweden': 'SE', 'Singapore': 'SG', 'Slovenia': 'SI',
                   'Svalbard and Jan Mayen': 'SJ', 'Slovakia': 'SK'
        , 'San Marino': 'SM', 'Suriname': 'SR', 'El Salvador': 'SV', 'Tunisia': 'TN', 'Turkey': 'TR', 'Ukraine': 'UA',
                   'United States': 'US'
        , 'Uruguay': 'UY', 'Vatican City': 'VA', 'Venezuela': 'VE', 'Vietnam': 'VN', 'South Africa': 'ZA',
                   'Zimbabwe': 'ZW'
                   }

    if code not in all_country.keys():
        print("\nThere have not this country")
    else:
        the_code = all_country.get(code)
        response = requests.get(f"https://date.nager.at/api/v3/publicholidays/{years}/{the_code}")

        data = response.json()

        if month.lower() == "all":
            normal_date_fun(data)
        else:
            the_moth = int(month)
            if the_moth <= 9:
                specify_date_func(data, f"0{month}")
            else:
                specify_date_func(data, str(month))


enter_year = int(input("Enter Year: "))
enter_month = input("Enter month or all for full list of holiday: ")
country_code = input("Enter Country: ")

response_func(enter_year, enter_month, country_code)
