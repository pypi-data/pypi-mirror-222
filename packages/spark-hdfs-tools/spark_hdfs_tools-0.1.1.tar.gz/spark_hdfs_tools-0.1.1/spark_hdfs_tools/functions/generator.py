def hdfs_creating_directory(spark=None, path=None):
    from spark_hdfs_tools import get_color, get_color_b

    sc = spark.sparkContext
    fs = spark._jvm.org.apache.hadoop.fs.FileSystem.get(spark._jsc.hadoopConfiguration())
    if path in ("", None):
        raise Exception(f'required variable path')
    if not fs.exists(sc._jvm.org.apache.hadoop.fs.Path(f'{path}')):
        fs.mkdirs(sc._jvm.org.apache.hadoop.fs.Path(f'{path}'))
        print(f"{get_color('Directory Created:')} {get_color_b(path)}")
    else:
        print(f"{get_color('Directory Exists:')} {get_color_b(path)}")


def get_last_day_of_month(current_date):
    from datetime import timedelta
    if current_date.month == 12:
        return current_date.replace(day=31)
    return current_date.replace(month=current_date.month + 1, day=1) - timedelta(days=1)


def validate_exist_cutoff_date(spark, table_pathname):
    sc = spark.sparkContext
    URI = sc._gateway.jvm.java.net.URI
    Path = sc._gateway.jvm.org.apache.hadoop.fs.Path
    FileSystem = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
    Configuration = sc._gateway.jvm.org.apache.hadoop.conf.Configuration
    fs = FileSystem.get(spark._jsc.hadoopConfiguration())

    hdfs_path_one = [str(file.getPath().getName()) for file in fs.listStatus(Path(f"{table_pathname}"))
                     if not str(file.getPath().getName()).startswith("_")
                     if not str(str(file.getPath().getName()).split("=")[0]) in ("gf_cutoff_date", "cutoff_date")]
    return hdfs_path_one


def validate_list_cutoff_date(spark, table_pathname):
    sc = spark.sparkContext
    URI = sc._gateway.jvm.java.net.URI
    Path = sc._gateway.jvm.org.apache.hadoop.fs.Path
    FileSystem = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
    Configuration = sc._gateway.jvm.org.apache.hadoop.conf.Configuration
    fs = FileSystem.get(spark._jsc.hadoopConfiguration())

    hdfs_path_one = sorted([str(file.getPath().getName()) for file in fs.listStatus(Path(f"{table_pathname}"))
                            if not str(file.getPath().getName()).startswith("_")
                            if str(str(file.getPath().getName()).split("=")[0]) in ("gf_cutoff_date", "cutoff_date")])
    return hdfs_path_one


def hdfs_generated_partition_dates(spark=None, table_pathname=None):
    import os
    hdfs_path_one = validate_exist_cutoff_date(spark=spark, table_pathname=table_pathname)

    table_relative = str(table_pathname.split("/")[-1])
    path_list = list()
    path_dict = dict()
    if len(hdfs_path_one) > 0:
        for part in hdfs_path_one:
            table_name_two = os.path.join(table_pathname, part)
            hdfs_files = validate_list_cutoff_date(spark=spark, table_pathname=table_name_two)
            if table_name_two not in path_dict.keys():
                path_dict[table_name_two] = dict()
            table_partition_date = sorted([date.split("=")[1] for date in hdfs_files])
            path_dict[table_name_two]["table_name"] = table_relative
            path_dict[table_name_two]["table_name_subpartition"] = part
            path_dict[table_name_two]["table_pathname"] = table_name_two
            path_dict[table_name_two]["table_partition_date"] = table_partition_date

        path_list.append(path_dict)

    else:
        table_name_two = os.path.join(table_pathname)
        hdfs_files = validate_list_cutoff_date(spark=spark, table_pathname=table_name_two)
        if table_name_two not in path_dict.keys():
            path_dict[table_relative] = dict()
        table_partition_date = sorted([date.split("=")[1] for date in hdfs_files])
        path_dict[table_relative]["table_name"] = table_relative
        path_dict[table_relative]["table_name_subpartition"] = ""
        path_dict[table_relative]["table_pathname"] = table_name_two
        path_dict[table_relative]["table_partition_date"] = table_partition_date
        path_list.append(path_dict)

    return path_list


def hdfs_calculate_calendar(year=None, month=None):
    import datetime
    import pandas as pd
    import calendar
    from spark_hdfs_tools.utils.calendar import holidays_pe
    from spark_hdfs_tools.utils.calendar import days_habil

    start_date = datetime.date(year, month, 1)
    _, last_days = calendar.monthrange(year, month)
    end_date = datetime.date(year, month, last_days)
    date_range = pd.date_range(start_date, end_date)
    date_holidays = holidays_pe(year=year)
    date_habils = days_habil()
    calendar_habil = list()
    calendar_normal = list()
    for date in date_range:
        current_date = date.strftime('%Y-%m-%d')
        weekday_date = date.strftime('%A')
        if current_date not in date_holidays:
            calendar_normal.append(current_date)
        if weekday_date in date_habils and current_date not in date_holidays:
            calendar_habil.append(current_date)
    return calendar_normal, calendar_habil


def get_max_partition(spark=None, table_path_name=None):
    table_name = str(table_path_name.split("/")[-1])
    partition_dates = hdfs_generated_partition_dates(spark=spark, table_pathname=table_path_name)
    max_partition = max(partition_dates[0][table_name]["table_partition_date"])
    return max_partition


def get_all_partition_without_process_date(spark=None, table_path_name=None):
    table_name = str(table_path_name.split("/")[-1])
    partition_dates = hdfs_generated_partition_dates(spark=spark, table_pathname=table_path_name)
    all_partition = partition_dates[0][table_name]["table_partition_date"]
    return all_partition


def get_max_monthly_partition_with_process_date(spark=None, table_path_name=None, process_date=None):
    from datetime import datetime

    from dateutil.relativedelta import relativedelta

    name_list = get_all_partition_without_process_date(spark, table_path_name)

    current_process_date = datetime.strptime(process_date, '%Y-%m-%d')
    current_month_process_date = current_process_date.month
    current_year_process_date = current_process_date.year
    current_date_list = list()
    if current_month_process_date == 1:
        subtract_one_month_process_date = current_process_date - relativedelta(months=1)
        subtract_one_month_process_date = get_last_day_of_month(subtract_one_month_process_date)
        subtract_initial_process_date = datetime(subtract_one_month_process_date.year, 1, 1)
        for date_partition in name_list:
            date_partition2 = datetime.strptime(date_partition, '%Y-%m-%d')
            if subtract_initial_process_date <= date_partition2 <= subtract_one_month_process_date:
                current_date_list.append(date_partition)
    else:
        subtract_initial_process_date = datetime(current_year_process_date, 1, 1)
        subtract_one_month_process_date = current_process_date - relativedelta(months=1)
        subtract_one_month_process_date = get_last_day_of_month(subtract_one_month_process_date)
        for date_partition in name_list:
            date_partition2 = datetime.strptime(date_partition, '%Y-%m-%d')
            if subtract_initial_process_date <= date_partition2 <= subtract_one_month_process_date:
                current_date_list.append(date_partition)
    if len(current_date_list) > 0:
        max_current_date_list = max(current_date_list)
    else:
        max_current_date_list = []
    return max_current_date_list


def get_max_daily_partition_with_process_date(spark=None, table_path_name=None, process_date=None):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    name_list = get_all_partition_without_process_date(spark, table_path_name)
    current_process_date = datetime.strptime(process_date, '%Y-%m-%d')
    current_date_list = list()
    subtract_one_daily_process_date = current_process_date - relativedelta(days=1)
    for date_partition in name_list:
        date_partition2 = datetime.strptime(date_partition, '%Y-%m-%d')
        if date_partition2 <= subtract_one_daily_process_date:
            current_date_list.append(date_partition)
    if len(current_date_list) > 0:
        max_current_date_list = max(current_date_list)
    else:
        max_current_date_list = []
    return max_current_date_list


def get_list_partitions_incremental_monthly_twelve_last_year(spark=None, table_path_name=None, process_date=None):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    name_list = get_all_partition_without_process_date(spark, table_path_name)

    current_process_date = datetime.strptime(process_date, '%Y-%m-%d')
    current_month_process_date = current_process_date.month
    current_year_process_date = current_process_date.year
    current_date_list = list()
    if current_month_process_date == 1:
        subtract_one_month_process_date = current_process_date - relativedelta(months=2)
        subtract_one_month_process_date = get_last_day_of_month(subtract_one_month_process_date)
        subtract_initial_process_date = datetime(subtract_one_month_process_date.year, 1, 1)
        for date_partition in name_list:
            date_partition = datetime.strptime(date_partition, '%Y-%m-%d')
            if subtract_initial_process_date <= date_partition <= subtract_one_month_process_date:
                current_date_list.append(date_partition)
    else:
        subtract_initial_process_date = datetime(current_year_process_date, 1, 1)
        subtract_one_month_process_date = current_process_date - relativedelta(months=2)
        subtract_one_month_process_date = get_last_day_of_month(subtract_one_month_process_date)
        for date_partition in name_list:
            date_partition = datetime.strptime(date_partition, '%Y-%m-%d')
            if subtract_initial_process_date <= date_partition <= subtract_one_month_process_date:
                current_date_list.append(date_partition)

    if len(current_date_list) > 0:
        current_date_list = current_date_list
    else:
        current_date_list = []
    return current_date_list


def get_list_partitions_incremental_daily_month_last_year(spark=None, table_path_name=None, process_date=None):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    name_list = get_all_partition_without_process_date(spark, table_path_name)

    current_process_date = datetime.strptime(process_date, '%Y-%m-%d')
    current_year_process_date = current_process_date.year
    current_month_process_date = current_process_date.month
    current_day_process_date = current_process_date.day
    current_date_list = list()
    if current_month_process_date == 1 and current_day_process_date == 1:
        subtract_one_day_process_date = current_process_date - relativedelta(days=2)
        subtract_initial_process_date = get_first_day_of_month(subtract_one_day_process_date)
        print(subtract_one_day_process_date, subtract_initial_process_date)
        for date_partition in name_list:
            date_partition = datetime.strptime(date_partition, '%Y-%m-%d')
            if subtract_initial_process_date <= date_partition <= subtract_one_day_process_date:
                current_date_list.append(date_partition)
    else:
        subtract_initial_process_date = datetime(current_year_process_date, 1, 1)
        subtract_one_day_process_date = current_process_date - relativedelta(days=2)
        for date_partition in name_list:
            date_partition = datetime.strptime(date_partition, '%Y-%m-%d')
            if subtract_initial_process_date <= date_partition <= subtract_one_day_process_date:
                current_date_list.append(date_partition)

    if len(current_date_list) > 0:
        current_date_list = current_date_list
    else:
        current_date_list = []
    return current_date_list
