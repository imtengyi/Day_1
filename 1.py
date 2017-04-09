province_city_region = {'GuangDong':{'Guangzhou':['Tianhe','Liwan','Yuexiu'],'ShaoGuan':['Quba','Wengyuan','xxxyyy'],'Maoming':['Xue','LIN','KIN']},
                        'Beijing':{'chaoyang':['chao1','chao2','chao3'],'shijing':['shi1','shi2','shi3'],'haidian':['hai1','hai2','hai3']},
                        'Shanghai':{'Jingan':['jing1','jing2','jing3'],'xuhui':['xu1','xu2','xu3'],'putuo':['pu1','pu2','pu3']}
                        }
list_province = {}
list_region = {}
sum = 1
sum_a = 1


for i in province_city_region.keys():
        print('%d : %s' % (sum,i))
        list_province[sum] = i
        sum +=1
province_choose = input('请选择省份(1/2/3) \n')

for j in province_city_region[list_province[int(province_choose)]].keys():

        print('%d : %s' % (sum_a,j))
        list_region[sum_a] = j
        sum_a +=1

region_choose = input('请选择区(1/2/3) \n')

for k in province_city_region[list_province[int(province_choose)]][list_region[int(region_choose)]]:

    print('--->' +k)

