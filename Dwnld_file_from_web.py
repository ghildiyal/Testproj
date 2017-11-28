from urllib import request
ms_url='http://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv'

def download_ms(csv_url):
    response=request.urlopen(csv_url)
    csv=response.read()
    csv_str=str(csv)
    lines=csv_str.split("\\n")
    desturl= r'ms_url.csv'
    fx=open(desturl,'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()
download_ms(ms_url)