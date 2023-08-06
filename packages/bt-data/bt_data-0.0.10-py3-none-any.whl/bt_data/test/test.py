import akshare as ak


if __name__ == '__main__':
    df = ak.stock_info_a_code_name()
    list=df.to_dict('records')
    print(list)