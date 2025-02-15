import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import pandas as pd
from PriceDashBoard.models import *
from GetAPI import get_price_data
from django.db import transaction

def bulk_price_data(price_dataframe: pd.DataFrame, material_name: str):
    # MaterialsModel 객체 생성
    try:
        material_id = MaterialsModel.objects.get(material_name=material_name)
        
    except:
        print('잘못된 값 입니다.')
        return
        
    # MaterialPriceModel 데이터 생성
    # 모델에 데이터를 bulk하는 로직
    with transaction.atomic():
        price_data_list = []
        for index, row in price_dataframe.iterrows():
            price_data = MaterialsPriceModel(material_name=material_id,
                                            date=index,
                                            price=row['USD'])
            
            price_data_list.append(price_data)
            
        MaterialsPriceModel.objects.bulk_create(price_data_list)
        
    return

# 최초 bulk
def main():
    gold_price_data = get_price_data('gold')
    silver_price_data = get_price_data('silver')
    
    bulk_price_data(gold_price_data, 'Gold')
    bulk_price_data(silver_price_data, 'Silver')
    
    print('bulk 완료')