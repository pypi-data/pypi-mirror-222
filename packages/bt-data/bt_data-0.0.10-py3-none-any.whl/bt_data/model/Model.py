import akshare

from  bt_data.model.akshare.AKShareStockInfoACodeName import AKShareStockInfoACodeName


def get_akshare_stock_info_a_code_name() -> list[AKShareStockInfoACodeName]:
    df = akshare.stock_info_a_code_name()
    df_list = df.to_dict('records')
    res_list = []
    for ak_dict in df_list:
        data = AKShareStockInfoACodeName.parse_obj(ak_dict)
        res_list.append(data)
    return res_list
