


#创建订单
BUSINESS_CREATE_OREDER="'BUSINESS_CREATE_OREDER'+'_'+str(request.user.userid)+'_'+str(request.data_format.get('down_ordercode'))"

#自己更改余额
PAY_SELF_UPD_BAL="'PAY_SELF_UPD_BAL'+'_'+str(request.user.userid)"

#管理员修改余额
PAY_ADMIN_UPD_BAL="'PAY_SELF_UPD_BAL'+'_'+str(request.data_format.get('userid'))"

#二维码表
LOAD_QRCODE = "'LOAD_QRCODE'+'_'"