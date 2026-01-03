def date_parser(date):
    """Adjusting the date to be like 'YYYY-MM-DD'"""
    date_list = reversed(date.split('/'))
    new_date = ""
    
    for info in date_list:
        new_date += info + '-'
    
    return new_date.strip('-')