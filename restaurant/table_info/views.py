from django.shortcuts import render
from create_reservation.models import Reservation
from datetime import datetime, time

def reservation_list(request):
    # 获取当前日期
    current_date = datetime.now().date()

    # 需要檢查的固定時間點
    fixed_times = [(time(17, 0), time(18, 0)), (time(18, 0), time(19, 0)), (time(19, 0), time(20, 0))]

    # 创建一个空的字典来存储每个桌次的状态
    table_info_data = []

    # 遍历每个固定時間點
    for start_time, end_time in fixed_times:
        # 查找特定時間區間的預訂信息
        reservations = Reservation.objects.filter(date=current_date, time__gte=start_time, time__lt=end_time)

        # 获取所有桌次
        table_numbers = range(2, 9, 2)  # 假设有6张桌子

        # 檢查每個桌次
        for table_number in table_numbers:
            # 查找特定桌次的预订信息
            reservation = reservations.filter(table=table_number).first()

            # 确定桌次的状态
            if reservation:
                status = "已預訂"
            else:
                status = "可用"

            # 将桌次号、日期、時間和状态添加到列表
            table_info_data.append({
                'date': current_date.strftime("%Y-%m-%d"),
                'start_time': start_time.strftime("%H:%M"),
                'end_time': end_time.strftime("%H:%M"),
                'table_number': table_number,
                'status': status
            })

    # 在模板中渲染数据
    return render(request, 'table_info/table_info.html', {'table_info_data': table_info_data})
