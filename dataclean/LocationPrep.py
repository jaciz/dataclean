import re

def valid_zip_codes(df, col='ZIP', pattern='^[0-9]{5}(-[0-9]{4})?$'):
    zip_list = list(df[col].unique())

    yes_list = []
    no_list = []

    p = pattern
    for eachnumber in zip_list:
        if result := re.match(p, eachnumber):
            yes_list.append(eachnumber)
        else:
            no_list.append(eachnumber)
    print(f"There are {len(no_list)} entries that don't match zip code format")
    return no_list

def strip_character(string: str):
    """Strips special characters. Use it on columns by using the pandas apply function (e.g. loc['Street'].apply(strip_character))

    Args:
        dataCol (str): string with special characters you want removed

    Returns:
        str: string with removed special characters
    """
    r = re.compile(r'[^A-Za-z\s0-9]+')
    return r.sub('', string)