def get_current_drivers_data(sample):
    current_datetime = datetime.now(config.tz)
    date_str = current_datetime.strftime("%Y-%m-%d")
    amazon_sites_df_raw = amazon_sites.create_amazon_sites_df(
        db=db_connector.connect_to_db(db_name='whizzard'))
    amz_sites_fpath = f'/home/ubuntu/atom/{PROJECT_NAME}/amazon_sites.xlsx' \
        if config.ON_SERVER else f'../{PROJECT_NAME}/amazon_sites.xlsx'
    amazon_sites_df = toolkit.save_or_retrieve_df_excel(
        input_df=amazon_sites_df_raw, fpath=amz_sites_fpath)
    service_area_id_df = get_service_area_id()
    sites_service_id_df = pd.merge(toolkit.snake_case_the_cols(amazon_sites_df),
                                   service_area_id_df[[
                                       'site_code', 'service_area_id']],
                                   on='site_code', how='left')

    stn_code_id_list = sites_service_id_df[[
        'site_code', 'service_area_id']].to_numpy().tolist()
    print(f'Total Number of Sites found : {len(stn_code_id_list)}')
    stn_code_id_list = [row for row in stn_code_id_list if row[0] in [
        'HYDC', 'HYBH']] if sample else stn_code_id_list
    print(f'Sample Size (Number of Sites) : {len(stn_code_id_list)}') if sample else print(
        end='')
    drivers_df_list = []
    num = 0
    for stn, s_area_id in stn_code_id_list:
        num += 1
        try:
            drivers_df = get_drivers_data(
                yyyy_mm_dd=date_str, service_area_id=s_area_id)
            if not drivers_df.empty:
                drivers_df.insert(loc=0, column='date', value=date_str)
                drivers_df.insert(loc=1, column='updated_timestamp',
                                  value=current_datetime.strftime("%d/%m/%Y %H:00"))
                drivers_df.insert(loc=2, column='station_code', value=stn)
                drivers_df_list.append(drivers_df)
                print(f'{num}. {stn} - success', end=' ')
            else:
                print(f'{num}. {stn} - no_data', end=' ')
        except Exception as err:
            error_name = type(err).__name__
            print(f'{num}. {stn} - {error_name}', end=' ')
        if num % 8 == 0:
            print()
    print()

    if drivers_df_list:
        defaulters_df_raw = pd.concat(drivers_df_list)
    else:
        raise custom_errors.NoDataError

    defaulters_df = manipulate_the_data(input_df=defaulters_df_raw)

    site_details_df_raw = amazon_sites_df.drop(columns='Client Site Code')
    site_details_df = site_details_df_raw.rename(
        columns={'Site Code': 'station_code'})
    site_details_df = toolkit.snake_case_the_cols(input_df=site_details_df)
    defaulters_df_final = pd.merge(
        defaulters_df, site_details_df, on='station_code', how='left')
    splitted_dfs = split_the_df(input_df=defaulters_df_final)
    # splitted_dfs['inactive_drivers_df'].columns = ['Site', 'Updated Time', 'Driver ID', 'Name', 'Status',
    #                                                'Amz Login Time', 'Inactive From', 'Shift Hours Left',
    #                                                'Total Stops', 'Completed Stops', 'Stops at Risk',
    #                                                'Packages at Risk', 'OM', 'RM', 'Client']
    # splitted_dfs['not_departed_drivers_df'].columns = ['Site', 'Updated Time', 'Driver ID', 'Name', 'Amz Login Time',
    #                                                    'Total Stops', 'Completed Stops', 'OM', 'RM', 'Client']
    # splitted_dfs['behinders_df'].columns = ['Site', 'Updated Time', 'Driver ID', 'Name', 'Amz Login Time',
    #                                         'Shift Ends at', 'Shift Hours Left', 'Inactive Hours', 'Total Stops',
    #                                         'Completed Stops', 'Stops at Risk', 'OM', 'RM', 'Client']
    # splitted_dfs['deliveries_df'].columns = ['Site', 'Updated Time', 'Driver ID', 'Name', 'Amz Login Time',
    #                                          'Delivered', 'RTS Done', 'Reattemptable', 'Total Stops',
    #                                          'Completed Stops', 'OM', 'RM', 'Client']
    return {'defaulters_df_final': defaulters_df_final,
            'defaulters_df_raw': defaulters_df_raw,
            'inactive_drivers_df': splitted_dfs['inactive_drivers_df'],
            'not_departed_drivers_df': splitted_dfs['not_departed_drivers_df'],
            'behinders_df': splitted_dfs['behinders_df'],
            'deliveries_df': splitted_dfs['deliveries_df']}
