import akshare as ak


if __name__ == '__main__':


    df = ak.stock_sse_summary()
    df['selector']=df['项目']
    df['stocks'] = df['股票']
    df['main'] = df['主板']
    df['kechuang'] = df['科创板']
    list = df.to_dict('records')
    print(list)